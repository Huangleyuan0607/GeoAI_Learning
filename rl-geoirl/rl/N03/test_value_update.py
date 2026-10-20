"""
来源：论文官方开源代码 geoirl-official
原始文件：causal_maxent.py
函数名：stochastic_value_iteration

描述：
    原样节选作者函数的计算逻辑，增加中文注释。
    用同一组两状态输入，对照标准Bellman评估和作者更新。

数学公式：
    标准评估：v_new = r + gamma * (P @ v_old)。
    作者更新：v_new = r + mean(gamma * (P @ v_old))。
    P形状为(2, 2)，r和v形状为(2,)，作者mean得到公共标量。

本日输入：
    P = [[0, 1], [1, 0]]，r = [0, 1]，gamma = 0.5。
    标准解为[2/3, 4/3]，作者固定点为[0.5, 1.5]。

注意：
    这是固定策略下的小矩阵对照，不求最优动作，不学习奖励。
    仅节选函数，不导入官方模块，不修改原文件，不读写实验数据。
"""


# 导包
import numpy as np


# 1.定义原函数：随机策略价值迭代
def stochastic_value_iteration(transition, reward, discount, eps = 1e-5):
    """
        迭代式策略评估：作者实现的价值迭代/策略评估变体（固定策略小矩阵对照）

        参数：
            transition: 状态转移矩阵，形状为 (状态数, 状态数)，索引为[当前状态, 下一状态]
            reward: 即时奖励向量，形状为 (状态数, )
            discount: 折扣因子（取值范围在 0 - 1 之间）
            eps: 收敛阈值（当两轮迭代的价值变化量小于该值时停止循环）

        返回值：
            v: 收敛后的状态价值数组，形状为 (状态数, )
        """
    # 获取状态总数，本例 transition 的形状为 (2, 2)，因此 transition.shape[0] = 2
    # 注意：这里取的是状态数，不是动作数
    n_states = transition.shape[0]
    v = np.zeros(n_states)          # 初始化状态价值为全 0，形状为 (状态数, )，本例为 (2, )

    delta = np.inf          # 定义误差，设定正无穷大的初始误差，保证 while 循环第一次一定能进入循环
    while delta > eps:
        # 1.保留本轮更新前的向量
        # 后面的 v = reward + ... 会生成新数组，因此这里不会改掉 v_old
        v_old = v

        # 2.按转移矩阵加权后续价值，再乘折扣
        # transition 是 (2, 2)，v 是 (2, )，所以 q 是 (2, )
        q = discount * (transition @ v)

        # 3.axis = 0在一维 q 上取平均，结果是一个标量
        # 标量广播到reward的每一项
        v = reward + np.average(q, axis = 0)

        # 4.取各状态变化绝对值的最大值，作为停止判断，当这个值小于eps阈值时，我们视为收敛，循环停止
        delta = np.max(np.abs(v_old - v))

    return v


# 2.定义主函数：先检查输入，再逐轮对照，最后分别验证固定点
def main():
    np.set_printoptions(precision = 6, suppress = True)         # numpy的打印设置，保留6位小数，不使用科学计数法

    # 1.构造两栋建筑交替访问的合成例子，默认使用float64
    transition = np.array([[0.0, 1.0], [1.0, 0.0]])         # 状态转移矩阵
    reward = np.array([0.0, 1.0])           # 奖励
    gamma = 0.5             # 折扣因子
    eps = 1e-10             # 收敛阈值
    max_iter = 1000         # 最大迭代次数

    # 2.形状和概率检查，避免(2, )与(2, 1)广播出不同计算
    assert transition.shape == (2, 2)
    assert reward.shape == (2,)
    assert np.isfinite(transition).all() and np.isfinite(reward).all()
    assert (transition >= 0).all()
    np.testing.assert_allclose(transition.sum(axis = 1), [1.0, 1.0])
    assert 0 <= gamma < 1
    print("状态转移矩阵：\n", transition)
    print("奖励向量:", reward, "折扣因子:", gamma, "收敛阈值:", eps, "最大迭代次数:", max_iter)

    # 3.只跟踪前三轮，分别保留两种更新各自的旧向量
    # 本段用于手算对照，不代替下面的收敛检查
    standard_trace = np.zeros(2)        # 标准方法的 V 向量 [0, 0]
    source_trace = np.zeros(2)          # 作者方法的 V 向量 [0, 0]
    for step in range(1, 4):            # 循环3轮
        # 标准更新Standard
        old_standard = standard_trace.copy()        # copy保证同步更新，用的是上一轮的旧值
        standard_trace = reward + gamma * (transition @ old_standard)

        # 源码更新source
        old_source = source_trace.copy()            # copy保证同步更新，用的是上一轮的旧值
        source_q = gamma * (transition @ old_source)        # 计算未来的折扣价值
        shared_term = np.average(source_q, axis = 0)        # 核心：把所有状态算出来的未来价值，全局求平均
        assert np.ndim(shared_term) == 0, "本例平均项应为标量"
        source_trace = reward + shared_term                 # 把同一个均值，加给所有状态

        print(f"step {step}: standard = {standard_trace}; source = {source_trace}; shared term = {shared_term:.6f}")

    # 4.标准Bellman迭代评估：每个状态保留自己的后续价值
    # max_iter只限制这里自写的标准对照，未改变原函数
    standard = np.zeros(2)
    for iteration in range(1, max_iter + 1):
        old_standard = standard.copy()
        standard = reward + gamma * (transition @ old_standard)
        delta = np.max(np.abs(standard - old_standard))
        if delta <= eps:
            break
    else:       # else 块里的代码，只有在循环没有被 break 打断（即循环正常结束）时才会执行
        raise RuntimeError("标准评估未在限定轮数内收敛")
    print(f"标准评估收敛于 {iteration} 轮：{standard}")

    # 5.用线性方程独立检查标准结果
    # v = r + gamma * P @ v -> (I - gamma * P) @ v = r
    # solve直接求方程解，本日不需要展开矩阵求逆推导
    exact_standard = np.linalg.solve(np.eye(2) - gamma * transition, reward)
    manual_standard = np.array([2.0 / 3.0, 4.0 / 3.0])
    # 断言验证（核心测试）
    # assert_allclose 是 NumPy 里专门用来做浮点数对比测试的函数
    # atol：绝对误差容忍度；1e-8；rtol：相对误差容忍度
    np.testing.assert_allclose(standard, exact_standard, atol = 1e-8, rtol = 1e-8)
    np.testing.assert_allclose(standard, manual_standard, atol = 1e-8, rtol = 1e-8)

    # 6.调用原代码中的函数
    # 本日固定小输入、行随机矩阵和gamma = 0.5用于受控验证
    source =  stochastic_value_iteration(transition, reward, gamma, eps = eps)
    manual_source = np.array([0.5, 1.5])
    np.testing.assert_allclose(source, manual_source, atol = 1e-8, rtol = 1e-8)     # 数值验证
    assert standard.shape == source.shape == (2, )                                  # 形状检查
    assert np.isfinite(standard).all() and np.isfinite(source).all()                # 有效性检查

    # 7.分别代回各自更新式，检查固定点残差
    # 残差小表示满足各自方程，不代表两种方程相同
    standard_residual = np.max(np.abs(standard - (reward + gamma * (transition @ standard))))
    source_residual = np.max(np.abs(source - (reward + np.average(gamma * (transition @ source)))))
    assert standard_residual < 1e-8
    assert source_residual < 1e-8
    assert not np.allclose(standard, source, atol = 1e-6, rtol = 1e-6)

    # 8.打印可复查结果
    print("标准迭代轮数:", iteration)
    print("标准算法结果:", standard)
    print("标准精确解:", exact_standard)
    print("源码算法结果:", source)
    print("标准方程残差:", standard_residual)
    print("源码方程残差:", source_residual)
    print("源码结果 - 标准结果:", source - standard)
    print("验证通过")


# 3.测试
if __name__ == "__main__":
    main()