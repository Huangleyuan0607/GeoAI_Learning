"""
需求：
    把贝尔曼方程用两种方法解出来：解析解（线性方程组）与迭代解（不动点），并用谱半径解释收敛
"""


# 导包
import numpy as np


# 1.造材料：n = 40 的随机行归一化转移矩阵P与随机奖励向量R（均值0，方差1）
def make_random_mrp(n = 40, seed = 2026):
    """
    参数：
        n: 状态数
        seed: 随机种子
    返回值：
        P: 转移矩阵，形状为 (状态数, 状态数)
        R: 奖励向量，形状为 (状态数, )
    """
    rng = np.random.default_rng(seed)       # 固定随机种子
    P = rng.random((n, n))
    P = P / P.sum(axis = 1, keepdims = True)                # 行归一化：每行是一个“下一状态”的概率分布
    R = rng.normal(loc = 0.0, scale = 1.0, size = n)        # 状态奖励：均值0，方差1
    # R = np.random.rand(n)                                 # 如果把R奖励改为全正数，那么‖V‖∞就会更大，因为没有坏奖励了
    # R = np.ones(n)
    return P, R

# 2.解法一（解析）：V = R + γPV -> (1 - γP)V = R，直接解线性方程组
def bellman_exact(P, R, gamma):
    """
    陷阱1：用np.linalg.solve而不是np.linalg.inv(A) @ R -- 显式求逆更慢，数值更不稳（条件数差时误差被放大）
    参数：
        P: 转移矩阵，形状为 (状态数, 状态数) -> (当前状态, 下一状态)
        R: 奖励向量，形状为 (状态数, ) -> (当前状态, )
        gamma: 折扣因子，标量
    返回值：
        V: 状态价值向量，形状为 (状态数, ) -> (当前状态, )
    """
    # 1. 构造系数矩阵 A = (I - γP)
    A = np.eye(P.shape[0]) - gamma * P      #  np.eye()：构建与P长宽相同的单位矩阵，P.shape[0]就是状态数

    # 2. 解方程 A * V = R，求出未知数 V
    V = np.linalg.solve(A, R)
    return V        # 返回每个状态的最终价值V

# 3.解法二（迭代）：V <- R + γPV，不动点反复代，直到整轮最大变化 < tol
def bellman_iterate(P, R, gamma, tol = 1e-12, max_iter = 20000):
    """
    官方 stochastic_value_iteration 就是这个结构：gamma 是折扣银子、tol 对应它的 eps阈值、循环体那一行就是更新式。
    陷阱二：判据用"最大变化"（上确界范数），不是总和；
    陷阱三：V 是列向量，写 P @ V，不是 V @ P。
    参数：
        P: 转移矩阵，形状为 (状态数, 状态数)
        R: 奖励向量，形状为 (状态数, )
        gamma: 折扣因子，标量
        tol: 容差，标量
        max_iter: 最大迭代次数，标量
    返回值：
        V: 状态价值向量，形状为 (状态数, )
        k: 迭代轮数，标量
    """
    V = np.zeros(len(R))
    for k in range(1, max_iter + 1):        # 相比源代码添加了一个最大迭代次数的限制，防止程序卡死
        V_next = R + gamma * (P @ V)        # 即源代码中的v = reward + discount * np.average(transition @ v, axis = 0)
        delta = np.abs(V_next - V).max()    # 即源代码中的delta = np.max(np.abs(v_old -v))
        V = V_next
        if delta < tol:     # 和源代码中的while delta > eps:虽然写法不同，但是最终目的都是当delta < tol时停止迭代
            return V, k
    raise RuntimeError(f"{max_iter}轮仍未收敛，最后单轮最大变化{delta:.3e}")

# 4.谱半径：迭代解的收敛开关（G08 发散实验的伏笔）
# 参数M：在强化学习里，这个 M 通常就是 γP（折扣因子乘转移矩阵），也就是传播误差的矩阵
def spectral_radius(M):
    """
    求传播误差矩阵γP的特征值，然后求出绝对值最大的特征值，这个值即谱半径ρ
    参数：
        M: 矩阵
    返回值：
        M的谱半径
    """
    return float(np.abs(np.linalg.eigvals(M)).max())    # np.linalg.eigvals(M) 算的是矩阵 M 的所有特征值

# 5.测试
if __name__ == "__main__":
    n = 40
    P, R = make_random_mrp(n)       # 构造 n = 40 的随机行归一化转移矩阵P与随机奖励向量R（均值0，方差1）

    print("=" * 60)
    print("材料自检")
    print("=" * 60)
    print(f"P 形状：{P.shape}")
    print(f"行和 min / max：{P.sum(axis = 1).min():.12f} / {P.sum(axis = 1).max():.12f}")    # axis = 1按行求和
    print(f"R 样本均值 / 标准差：{R.mean():.3f} / {R.std():.3f}")
    print(f"ρ(P)：{spectral_radius(P):.6f}（行随机矩阵必有ρ = 1，因为行随机矩阵行和为1，所以必有特征值λ = 1）")

    print()
    print("=" * 60)
    # γ 越大，奖励回传的 "半衰期" 就越长，价值函数需要经历更多的轮次（迭代）才能把未来微小的奖励波动抹平（收敛）
    print("两种解法对照（γ越大 -> 未来越重要 -> 迭代越慢）")
    print("=" * 60)
    # ‖V‖∞ 表示的是状态价值向量 V 的“无穷范数，即向量里所有元素绝对值最大的那个值
    # 即：在当前环境下，价值最高的那个状态，它的绝对值到底有多大。它代表了整个价值体系的 "量级（Scale）"。
    print(f"{'r':>6}{'ρ(γP)':>10}{'迭代轮数':>10}{'两解最大误差':>10}{'‖V‖∞':>8}")
    for gamma in (0.5, 0.9, 0.99):       # 分别测试不同gamma的迭代效果
        """
        用解析法（bellman_exact）算出一个绝对精确的价值V_exact
        用迭代法（bellman_iterate）算出一个近似价值V_iter，并记录迭代次数iters
        比较两者的误差，并把关键指标打印成一张对齐的表格
        """
        V_exact =   bellman_exact(P, R, gamma)
        V_iter, iters = bellman_iterate(P, R, gamma)
        err = np.abs(V_exact - V_iter).max()
        print(f"{gamma:>6.2f}{spectral_radius(gamma * P):>10.4f}{iters:>10}{err:>16.2e}{np.abs(V_exact).max():>10.3f}")

    # 5.1 附加实验：把行归一化去掉（行和 1.05 ~ 1.6），ρ(γP)可能大于1
    print()
    print("=" * 60)
    print("附加实验：行和不为1的'坏矩阵'")
    print("=" * 60)
    rng = np.random.default_rng(7)      # 固定随机种子
    # P_bad的每一行和不再是1，而是变成了1.05 ~ 1.6。这在物理上意味着概率质量凭空增加了（比如每一步有 150% 的概率去往下一个状态）
    P_bad = P * rng.uniform(1.05, 1.6, size = (n, 1))
    print(f"P_bad 行和 min / max：{P_bad.sum(axis = 1).min():.3f} / {P_bad.sum(axis = 1).max():.3f}")
    for gamma in (0.5, 0.99):
        rho = spectral_radius(gamma * P_bad)
        if rho >= 1.0:      # 也就是ρ(γP)大于1，即误差放大器的齿轮大于 1；结果完美验证了理论：谱半径大于等于 1，迭代必然发散
            print(f"γ = {gamma:.2f} ρ(γP_bad) = {rho:.4f} ≥ 1 -- 理论预言发散，硬跑{20000}轮：")
            try:
                bellman_iterate(P_bad, R, gamma, max_iter = 20000)
                print("竟然收敛了？回头检查代码")
            except RuntimeError as e:
                print(f"{e}")
        else:
            V_iter, iters = bellman_iterate(P_bad, R, gamma)
            err = np.abs(bellman_exact(P, R, gamma) - V_iter).max()
            print(f"γ = {gamma:.2f} ρ(γP_bad) = {rho:.4f} < 1 -- 仍收敛：{iters}轮，误差 {err:.2e}")

    # 一句话结论（写进笔记）：决定迭代收不收敛的不是 γ 单独，而是乘积 γP 的谱半径；
    # 行随机时 ρ(P) = 1，所以 ρ(γP) = γ < 1 必收敛；行和一旦超过 1，γ = 0.99 也能把 ρ 顶过 1，
    # 不动点直接不吸引——论文 §2.1.6 的全部焦虑就是这一个不等式。

# 强化学习（以及所有迭代法）最底层的数学铁律：
# 1、转移矩阵 P 必须行归一化（每行和为 1）。这不仅仅是为了满足物理概率守恒，更是为了保证 ρ(P) = 1
# 2、折扣因子 γ是唯一的"安全阀门"。因为 ρ(γP) = γρ(P) = γ x 1 = γ，只要γ < 1，迭代必定收敛
# 3、如果破坏了 P 的行和（比如代码里的 P_bad），ρ(P_bad) > 1，这时候如果不调小 γ（比如降到 0.5 勉强救回来），
# 一旦 γ 稍微大一点（比如 0.99），γ x ρ(P_bad) > 1，算法直接原地爆炸。











