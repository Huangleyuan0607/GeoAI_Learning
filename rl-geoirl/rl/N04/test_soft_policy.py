"""
来源：论文官方开源代码 geoirl-official
原始文件：causal_maxent.py
函数名：local_causal_action_probabilities

描述：
    节选IRL训练内部的行动概率计算，保留计算逻辑，增加中文注释。
    用两状态、discount = 0的例子，区分普通行动和停止选项。

数学公式：
    普通行动分数：q = reward + discount * P * v_old。
    合并停止项后：v_i = log(sum(exp(各选项分数)))。
    返回普通行动：p_ij = exp(q_ij - v_i)，不返回停止列。

本日输入：
    P = [[0, 1], [1, 0]]，reward = [0, 1]，terminal = [1]。
    非终止行分母为1+e，允许停止行分母为2+e。

注意：
    discount = 0只关闭后续项，reward始终固定，不用v_old替代。
    本例只测试部分状态允许停止；不进行IRL训练或轨迹生成。
"""


# 导包
import numpy
import torch


# 1.定义源代码函数
def local_causal_action_probabilities(p_transition, terminal, reward, discount, eps = 1e-5):
    """
    计算训练内部的局部行动概率（给定建筑奖励等信息，计算从每栋建筑出发时，选择各个下一步行动的概率）
    参数：
        p_transition: 转移矩阵，形状为 (状态数, 状态数)
        terminal: 允许停止的状态索引，本例为整型张量 [1]
        reward: 奖励函数
        discount: 折扣因子
        eps: 收敛阈值

    返回值：
        普通行动概率矩阵，形状为 (状态数, 状态数)
        停止项参与分母计算，但没有作为额外一列返回
    """

    # 从转移矩阵中获取状态数和动作数
    # 行数是当前状态数，列数是候选下一状态数；
    # 作者把选择下一状态视为行动，因此将列数记作 n_actions
    n_states, n_actions = p_transition.shape

    # 1.保留原函数的两个分支：本日只有状态1允许停止，进入else
    # reward_terminal 用来给每个状态设置一个 "停止选项 " 的分数：在哪里允许停止，在哪里屏蔽停止。
    if len(terminal) == n_states:       # 如果整个环境的状态都是终止状态
        reward_terminal = torch.tensor(terminal).float()            # ？
    else:                               # 存在不是终止状态的普通状态
        reward_terminal = -1e20 * torch.ones(n_states)      # 大负数近似屏蔽停止选项，reward_terminal = [-1e20, -1e20]
        reward_terminal[terminal] = 0.0                     # 状态1的停止分数设为0，reward_terminal = [-1e20, 0.0]

    v = -1e20 * torch.ones(n_states)                        # 初始价值向量，本例形状 (2, )
    delta = 1e20                                            # 初始误差，保证第一次进入循环

    while delta > eps:
        # 2.保留旧价值：reward始终是输入的即时奖励，不随本轮v变化
        v_old = v                   # 同步更新
        v = reward_terminal         # 把停止分数作为这一轮算V的基础

        # 3.逐元素乘法，reward和v_old都沿列广播，不是P @ v_old，这样可以保留动作这一维度
        # discount = 0时，每行q均为 [0, 1]，形状为 (2, 2)
        q =reward + discount * p_transition * v_old     # 计算动作价值函数Q(s, a)

        # 4.停止分数变为列向量，与两个普通行动拼接
        # (2, 1) 与 (2, 2) 拼成 (2, 3)，第0列是停止选项
        v = torch.cat([v.unsqueeze(1), q], 1)      # 将停止得分(v)转为列向量，与普通动作得分(q)拼成完整选项表
        v = torch.logsumexp(v, 1)                          # 沿着选项维度计算 log(∑exp)，算出结果形状变回 (2, )
        delta = torch.max(v - v_old)                            # 取新旧价值最大差值判断收敛

    # 5.q.T -v 先按列广播，转置回来后相当于每行减去自己的v_i
    # 指数化得到普通行动概率，不包含之前拼接的停止列
    return torch.exp((q.T - v).T)


# 2.定义测试主函数：先手算分母，再验证输出、停止余量和零边
def main():
    torch.set_printoptions(precision = 6, sci_mode = False)

    transition = torch.tensor(
        [[0.0, 1.0],
         [1.0, 0.0]],
        dtype = torch.float32
    )
    reward = torch.tensor([0.0, 1.0], dtype = torch.float32)
    terminal = torch.tensor([1], dtype = torch.long)
    discount = 0.0       # 按N04安排，先关闭后续项，观察奖励与停止选项

    # 调用原函数：每行是当前建筑，每列是候选目的建筑
    with torch.no_grad():
        probabilities = local_causal_action_probabilities(
            transition, terminal, reward, discount
        )

    print("建筑奖励：", reward)
    print("允许停止的建筑：", terminal)
    print("普通行动概率：\n", probabilities)
    print("普通行动行和：", probabilities.sum(dim = 1))
    print("停止概率余量：", 1.0 - probabilities.sum(dim = 1))

    # 只交换两栋建筑的奖励，观察行动倾向是否随之改变
    changed_reward = torch.tensor([1.0, 0.0], dtype = torch.float32)

    with torch.no_grad():
        changed_probabilities = local_causal_action_probabilities(
            transition, terminal, changed_reward, discount
        )

    print("\n交换奖励后：", changed_reward)
    print("新的普通行动概率：\n", changed_probabilities)
    print("概率变化：\n", changed_probabilities - probabilities)


# 3.测试
if __name__ == '__main__':
    main()






