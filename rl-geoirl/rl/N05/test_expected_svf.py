"""
来源：论文官方开源代码 geoirl-official
原始文件：causal_maxent.py
函数名：expected_svf_from_policy

学习目标：
    给定初始分布、转移与内部行动概率，观察作者的状态访问统计。
    比较没有转移与存在简单连接时的输出。

说明：
    原函数及其原注释保持原样，中文学习说明放在这里和主函数中。
    本例p_initial使用一维(2,)，返回res也为(2,)。
    terminal是终止状态索引；原docstring中的initial states字样保留原文。
    零转移是用于观察“没有流动”的边界输入，不是常规行随机转移矩阵。
    p_action人为给定，不在本日重复训练策略或奖励模型。
"""


# 导包
import torch


# 1.定义源代码函数
def expected_svf_from_policy(p_transition, p_initial, terminal, p_action, eps =1e-5):
    """
    计算当前策略下的期望状态访问频次（Expected SVF，即智能体在各状态停留的期望频次）

    强化学习里的状态访问频次公式：
        μ = μ0 + P^T * μ
        (当前状态的访问频次 = 初始状态频次 + 从其他状态转移过来的频次)

    参数：
        p_transition: 环境状态转移概率矩阵，形状为 (状态数, 状态数)，意思是 (当前状态, 下一状态)
        p_initial: 初始状态分布概率，形状为 (状态数, 1)
        terminal: 终止状态的索引（智能体到达该状态后不再转移）
        p_action: 当前策略下的动作概率矩阵，形状为 (状态数, 状态数)
        eps: 迭代收敛的误差阈值

    返回值：
        res: 收敛后的状态访问频次，形状为 (状态数, 1)
        laplaciab_max_eigval: 拉普拉斯矩阵的最大特征值（用于理论分析）
    """
    n_states, n_actions = p_transition.shape        # 获取环境参数，这里实际没有用上

    # 1.克隆转移矩阵，避免修改原始环境参数
    p_transition = p_transition.clone()

    # 2.屏蔽终止状态的流出：到达终止状态后不再向任何状态转移
    p_transition[terminal, :] = 0.0

    delta = 1e20            # 初始误差，保证第一次进入循环
    res = p_initial         # 初始访问频次等于初始状态分布
    d_ = None               # 存储每个迭代中算出的 "流入量" 矩阵（中间变量）
    save_p_action = False   # 无实际作用的占位变量
    num = 0

    # 3.迭代求解（幂迭代法），不断逼近无穷时间下的真实访问频次
    while delta > eps:
        # 3.1 计算流入量：状态-动作对频次，经过转移矩阵反向传播，得到下一步的频次分布
        # res 是我们当前对状态访问频次的估计
        # p_action * res: 算出当前在状态 s 执行动作 a 的总频次
        # p_transition.T @ ...: 利用矩阵转置乘法，把所有状态通过动作流向当前状态的频次加起来，相当于公式中的 P^T * μ
        d_ = p_transition.T @ (p_action * res)

        # 3.2 归一化处理：防止后续除法出现除零错误（NaN）
        # d_.sum(1): 是对每一行求和（算当前状态的总流入量）。加1是为了防止有的状态完全没有流入，导致分母为0
        out_D_inv = (1 / (d_.sum(1) + 1))

        # 3.3 利用广播机制，对流入量进行归一化缩放
        # 把刚才求的 out_D_inv 乘以流入量，也就是做了一次归一化缩放
        # 这一步在标准的 SVF 公式里其实没有，这是这篇论文为了后续求拉普拉斯矩阵特征值而做的一个平滑 / 归一化处理
        d_ = out_D_inv.view(-1, 1) * d_.float()

        # 3.4 更新当前的 SVF：初始频次 + 转移流入的频次
        # 这一步就是公式 μ = μ0 + P^T * μ 的直接实现
        # p_initial 是初始状态分布 μ0；d_.sum(axis = 1) 是把刚才算好的流入量加总，即: P^T * μ
        d = p_initial + d_.sum(axis = 1)

        # 3.5 计算本轮变化量，判断是否收敛
        # 用新的频次 d 减去旧的频次 res，取绝对值最大值作为误差 delta
        # 同时把 res 更新为新的 d
        delta, res = torch.max(torch.abs(d - res)), d

    # 4.计算拉普拉斯矩阵的最大特征值（实部），用于论文中的理论分析
    # d_ 是上文按行缩放后的矩阵，论文将对应处理称为 "左拉普拉斯" 归一化。
    # 根据论文第 2.1.6 节及 Figure 3，该值用于分析期望状态访问量（ESVF）迭代的收敛特性，并比较不同奖励模型的训练表现。
    # 此处在迭代结束后计算并返回该值；本函数仍通过 delta 与 eps 判断是否收敛。
    laplacian_max_eigval = max(torch.linalg.eigvals(d_).real)

    return res, laplacian_max_eigval        # 返回最终收敛的状态访问频次 res 和用于分析的 laplacian_max_eigval


# 2.测试主函数：通过两个调用，观察转移对状态访问统计的作用
def main():
    torch.set_printoptions(precision = 6, sci_mode = False)     # numpy的打印设置，保留6位小数，不使用科学计数法

    # 两个建筑各有一半的初始概率，建筑1为终止状态
    p_initial = torch.tensor([0.5, 0.5], dtype = torch.float32)
    terminal = torch.tensor([1], dtype = torch.long)

    # 为了单独观察访问量计算，先给定一组简单的内部行动概率
    p_action = torch.tensor([[0.5, 0.5], [0.5, 0.5]], dtype = torch.float32)

    print("初始状态分布：", p_initial)
    print("终止建筑索引：", terminal)
    print("给定的内部行动概率：\n", p_action)
    print()

    # 没有转移：观察结果是否只保留初始分布
    zero_transition = torch.zeros((2, 2), dtype = torch.float32)
    with torch.no_grad():
        zero_visits, zero_eigenvalue = expected_svf_from_policy(zero_transition, p_initial, terminal, p_action)

    print("没有转移时的访问统计：", zero_visits)
    print("附带特征值：", zero_eigenvalue.item())
    print()

    # 只换转移输入：函数内部会把终止建筑1的出发行清零
    connected_transition = torch.tensor([[0.0, 1.0], [1.0, 0.0]], dtype = torch.float32)
    with torch.no_grad():
        connected_visits, connected_eigenvalue = expected_svf_from_policy(connected_transition, p_initial, terminal, p_action)

    print("加入连接后的访问统计：", connected_visits)
    print("相比没有转移时的变化：", connected_visits - zero_visits)
    print("访问统计合计：", connected_visits.sum().item())
    print("附带特征值：", connected_eigenvalue.item())
    print("调用后外部的转移矩阵：", connected_transition)


# 3.测试
if __name__ == "__main__":
    main()
