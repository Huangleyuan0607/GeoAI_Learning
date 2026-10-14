"""
需求：
    把论文的MDP写成对象：把RL的五个词换成论文的实体
"""


# 导包
from dataclasses import dataclass, field
import numpy as np


# 1.定义论文MDP的dataclass
@dataclass
class TrajMDP:      # 这个TrajMDP类就是整篇论文的数据容器
    """
    定义论文2.1的那套MDP
    字段与论文的对应关系：
        State状态 -> 一栋建筑（图上节点），全量12318栋 / 学习子集1014栋
        Action行动 -> 从当前建筑前往另一栋建筑，动作空间 = 该行P的非零列
        Transition -> P，由式(1)SGS行归一化而来（论文2.1.3部分）
        Reward奖励 -> W · F 或 MLP / GCN / GraphConv的输出，未知，这正是要反演的东西
        Policy策略 -> Π(a|s)，训练结束后体现为"更新过的转移矩阵"，不是最短路
        Episode -> 一条home-based tour，平均4.92个停留点
    """
    # 状态数 = 建筑物数
    n: int
    # (n, n)行归一化转移矩阵，每一行代表从一个建筑出发，去往其他建筑的概率。行归一化意味着每一行的元素之和等于 1。
    P: np.ndarray
    # (n, ) bool，用来标记哪些建筑是 "终止状态"（论文2.1.4部分）
    terminal: np.ndarray
    # (n, ) 专家（真实人类）在每个建筑上的期待访问次数 = ESVF(Expected State Visit Frequency)的观测版（论文2.1.2部分）
    expert_visits: np.ndarray
    # (n, k) 特征矩阵，reward = F @ W（特征矩阵乘以权重向量）；论文 k = 11说明每栋建筑有 11 个特征；field(default = None)表示这个字段可以不传
    F: np.ndarray = field(default = None)

    # 2.形状体检
    def __post_init__(self):
        # 检查转移矩阵 P 的形状必须是 (n, n)。如果不对，抛出断言错误，并打印具体形状方便调试。
        assert self.P.shape == (self.n, self.n), f"P 形状 {self.P.shape} != ({self.n}, {self.n})"
        # 检查终止状态数组 terminal 的形状必须是长度为 n 的一维数组。
        assert self.terminal.shape == (self.n, ), self.terminal.shape
        # 检查专家访问次数数组 expert_visits 的形状必须是长度为 n 的一维数组。
        assert self.expert_visits.shape == (self.n, ), self.expert_visits.shape
        # 如果传入了特征矩阵F（非None），则检查它的行数必须等于n（即建筑数）。列数k不限制，因为可以是11个特征，也可以自定义其他数量。
        if self.F is not None:
            assert self.F.shape[0] == self.n, self.F.shape

    # 3.自检用的小工具
    # 检查每行概率和是否为 1
    def row_sums(self):
        """每行之和：行归一化是否真的成立，只看这一个数"""
        return self.P.sum(axis = 1)     # axis=1 表示沿着 "行" 的方向求和，即对每一行的所有列元素求和

    # 检查是否真的是 "随机矩阵"
    # tol：容差，默认值为 1e-9
    def is_stochastic(self, tol = 1e-9):
        # 如果所有行之和都等于 1，那么这个矩阵就是随机矩阵（Stochastic Matrix）
        return bool(np.allclose(self.row_sums(), 1.0, atol = tol))

    # 检查对角线是否为 0
    # tol：容差，默认值为 1e-12
    def has_zero_diagonal(self, tol = 1e-12):
        """式(1)规定 i = j 时为 0：'留在原地'不是论文允许的动作"""
        # 论文的式(1)规定，P[i, j] 在 i = j 时必须是 0。意思是智能体留在原地的概率为0，即不能留在原地，必须前往另一栋建筑。
        # .mean()：对布尔矩阵求平均值。True 当作 1，False 当作 0。所以这个平均值就是非零元素占总元素的比例。
        return bool(np.allclose(np.diag(self.P), 0.0, atol=tol))

    # 检查矩阵的稀疏程度
    def density(self):
        """非零元比例：论文把P稀疏化到10%，这个数要一直盯着（论文3.1部分）"""
        return float((self.P > 0).mean())

    # 计算每栋建筑的 "入流"
    def inflow(self):
        """入流 = P的列和 = 这栋建筑被想去的总流量"""
        # P[i, j] 表示从建筑 i 去建筑 j 的概率。所以，列和 Σ_i P[i, j] 就代表所有建筑“想去”建筑 j 的总概率/总流量。
        # 在论文中，这个指标可以用来分析哪些建筑是热门目的地（入流高），哪些是冷门目的地。
        return self.P.sum(axis = 0)     # axis=0 表示沿着 "列" 的方向求和，即对每一列的所有行元素求和

# 4.造一个随机转移矩阵：真正的P由SGS造（见make_transition.py），这里只给dataclass一个框架
# 参1：状态数（建筑数）；参2：随机种子
# 参3：稀疏保留率，意思是矩阵里大约只有 20% 的位置是有概率的，其余 80% 都是 0（不通）。这呼应了论文里稀疏化到 10% 的要求。
def random_transition(n, seed = 42, keep = 0.2):
    rng = np.random.default_rng(seed)   # 固定随机种子
    A = rng.random((n, n))   # 生成一个 (n, n) 的随机矩阵

    # 实现稀疏化的核心操作，随机数大于0.2的概率是80%。也就是说，80%的格子会被选中，然后把A里对应位置的数字强行改成0。
    # 这样，A中只剩下大约20%的非零数字，其余全被抹成0。
    A[rng.random((n, n)) > keep] = 0.0

    np.fill_diagonal(A, 0.0)        # 把矩阵对角线上的数字全变成 0。
    dead = A.sum(axis = 1) == 0     # 检查 "死胡同"。A.sum(axis = 1)：算每一行的和；== 0：找出哪些行的和是 0。
    if dead.any():      # 如果出现死胡同
        A[dead] = 1.0       # 把这一整行全填成1.0。这相当于给这栋建筑临时连上了通往所有建筑的 "虚幻道路"。
        np.fill_diagonal(A, 0.0)        # 再次把对角线变回0（因为刚才填1.0的时候把对角线也填成1了，必须去掉）。4

    # 行归一化，把概率变成真正的“百分比”。最后返回的矩阵，每一行的和都精确等于 1
    # keepdims = True是为了保持二维形状（变成n×1的列向量），这样才能和原矩阵A（n×n）进行除法运算（这叫广播机制）。
    return A / A.sum(axis = 1, keepdims = True)

# 5.测试
if __name__ == "__main__":
    n = 50
    P = random_transition(n, 42)
    #                        terminal今天先全False                      今天还没有专家数据
    mdp = TrajMDP(n, P, terminal = np.zeros(n, dtype = bool), expert_visits = np.zeros(n), F = None)

    print("=" * 60)
    print("TrajMDP自检")
    print("=" * 60)
    print(f"状态数n                   {mdp.n}")
    print(f"转移矩阵形状               {mdp.P.shape}")
    print(f"行和全为1                  {mdp.is_stochastic()}")
    print(f"行和 min / max            {mdp.row_sums().min():.12f} / {mdp.row_sums().max():.12f}")
    print(f"对角全为0                  {mdp.has_zero_diagonal()}")
    print(f"矩阵密度                   {mdp.density():.3f}")
    print(f"终止状态数                 {int(mdp.terminal.sum())}")
    print(f"expert_visits全为0        {bool((mdp.expert_visits == 0).all())}")
    print(f"入流前5（列和降序）        {np.sort(mdp.inflow())[::-1][:5].round(4)}")

    # 留一处问题：terminal 今天填全 False 占位。论文里训练用的初/终态（论文2.1.4部分：终止概率只落在"非信息性"节点上）
    # 与生成轨迹用的初/终态（论文2.2：家作为终止点、终止概率由 Kaplan-Meier 生存概率推出）是两套设定。
    # G14 精读论文2部分时回来收这笔账

