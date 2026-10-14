"""
来源：geoir1-official（原论文官方开源代码库提取）
原始文件：transitions.py
函数名：simple_gravity

描述：
    本函数是从 geoir1-official 源码中单独提取出来的转移矩阵构建模块。
    用于根据建筑物的坐标和建筑面积，基于简单重力模型（Simple Gravity Score, SGS）计算建筑物之间的初始转移概率矩阵。
    数学公式为：SGS_ij = V_j / D_ij^2（当 i ≠ j），对角线元素为 0。其中 V_j 为终点建筑 j 的建筑面积，D_ij 为建筑 i 与 j 之间的欧几里得距离。

    实现细节：
        参数 beta 硬编码为 2，对应公式中的距离平方。
        使用 PyTorch 的 cdist 计算坐标间的欧几里得距离，并取 beta 次方。
        将对角线距离（0）替换为 1e5，避免除零错误。
        计算 scores = 建筑面积 / 距离^2，并将对角线置 0。
        对 scores 进行行归一化（每行除以该行总和），得到每行和为 1 的转移矩阵。

    注意：
        原函数名 simple_gravity 直接对应论文中的简单重力得分（SGS），但源码中 beta 固定为 2，且未提供可配置参数。
        返回的转移矩阵为稠密矩阵，后续论文中会进行稀疏化至 10% 密度以减轻计算负载。

        此外，论文中的SGS公式为：SGS_ij = V_i / D_ij^2，但在源码中的实际执行是：SGS_ij = V_j / D_ij^2，这里我们以源码为准。

参考文献：
    - 论文：Generating geospatial trajectories with incomplete data using graph inverse reinforcement learning
    - 代码仓库：https://doi.org/10.6084/m9.figshare.29554394
"""


# 导包
import numpy as np
import pandas
import pandas as pd
import torch


# 1.定义函数，实现：简单重力模型
# 参数buildings:一个包含建筑物信息的 pandas DataFrame（需包含 x, y 坐标和 floorspace 建筑面积）
def simple_gravity(buildings: pd.DataFrame):
    """
    计算建筑物之间的转移概率矩阵，基于简单重力模型（Simple Gravity Score, SGS）
    参数：
        buildings: 一个包含建筑物信息的 pandas DataFrame，需包含 x, y 坐标和 floorspace 建筑面积
    返回值：
        transition: 一个形状为 (N, N) 的转移概率矩阵，表示建筑物之间的转移概率
    """
    # 1.定义距离衰减参数 beta
    beta = 2        # 对应公式 SGS_ij = V_j / (D_ij)^beta 中的指数。论文中 beta = 2，即距离的平方

    # 2.从 DataFrame 中提取 "x" 和 "y" 两列数据
     # 形状为 (N, 2)，N 为建筑物总数。每一行是一个建筑的二维坐标
    coor = torch.tensor(buildings.loc[:, ["x", "y"]].to_numpy())

    # 3.提取 "floorspace" 列（建筑面积）
     # 形状为 (N,)。对应公式中的 V_j（终点建筑的体积/面积）
    vol = torch.tensor(buildings.floorspace.to_numpy())

    # 4.计算所有建筑物两两之间的欧几里得距离（p=2）
    # 形状为 (N, N) 的矩阵。然后再取 beta 次方（即平方），对应公式中的 D_ij^2
    distance = torch.cdist(coor, coor, p=2).pow(beta)
    # 当距离为0时（即自己到自己，或坐标完全相同的情况），替换为1e5，避免除零错误
    distance[distance == 0] =1e5

    # 5.计算SGS得分，核心公式计算：SGS_ij = V_j / D_ij^2
    # 利用 PyTorch 的广播机制，vol (N,) 会广播到 distance (N, N) 的每一行
    # 结果 scores 的形状为 (N, N)，scores[i][j] 表示从 i 到 j 的原始重力得分
    scores = vol.div(distance)      # score = vol / distance = V_i / D_ij^2

    # 6.将矩阵的对角线元素置为 0
    # 对应公式中：当 i = j 时，SGS_ij = 0（即建筑不能转移到自身）
    scores = scores.fill_diagonal_(0)

    # 7.行归一化：将原始得分转化为转移概率
    # torch.sum(scores, 1) 对每一行求和，view(-1, 1) 将其变为 (N, 1) 的列向量
    # scores.div(...) 将每一行的每个元素除以该行的总和，使得每一行的概率之和为 1
    transition = scores.div(torch.sum(scores, 1).view(-1, 1))

    return transition       # 最终返回合法的状态转移矩阵 transition


# 2.定义主函数，用于：测试simple_gravity函数
# 核心逻辑：构造一个只有3栋建筑的极简合成数据集，手动算出理论上的转移概率，然后断言（assert）程序计算的结果与手算结果一致。
def main():
    # 构造一个包含3栋建筑的合成 DataFrame
    # x, y 是坐标（都在x轴上），floorspace 是建筑面积
    # 建筑0: 坐标(0,0), 面积10；建筑1: 坐标(1,0), 面积20；建筑2: 坐标(3,0), 面积30
    buildings = pd.DataFrame({
        "x": [0.0, 1.0, 3.0],
        "y": [0.0, 0.0, 0.0],
        "floorspace": [10.0, 20.0, 30.0],
    })

    # 调用 simple_gravity 函数，计算转移矩阵
    transition = simple_gravity(buildings)

    # 将 PyTorch 张量转换为 NumPy 数组，方便后续用 numpy 的测试工具进行断言和打印。
    values = transition.detach().cpu().numpy()      # .detach() 断开计算图，.cpu() 移动到CPU，.numpy() 转为数组

    # 断言测试部分
    # 1. 验证矩阵形状是 (3, 3)
    assert values.shape == (3, 3)
    # 2. 验证矩阵中所有元素都是有限数（没有 NaN 或 Inf，验证 1e5 替换 0 的操作有效）
    assert np.isfinite(values).all()
    # 3. 验证所有概率都是非负数
    assert (values >= 0).all()
    # 4. 验证对角线元素全为 0（建筑不能转移到自身）
    np.testing.assert_allclose(np.diag(values), 0.0, atol = 1e-8)
    # 5. 验证每一行的概率之和为 1（行归一化正确）
    np.testing.assert_allclose(values.sum(axis = 1), 1.0, atol = 1e-8)

    # 手动计算验证（第一次）
    # 从建筑0出发，手动计算理论概率：
    # 注意：根据 simple_gravity 的代码，scores[i,j] = vol[j] / distance[i,j]^2
    # 建筑0到建筑1：距离=1，分数 = 20 / 1^2 = 20
    # 建筑0到建筑2：距离=3，分数 = 30 / 3^2 = 30/9 = 10/3
    # 总分 = 20 + 10/3 = 70/3
    # 归一化：建筑0->1 概率 = 20 / (70/3) = 60/70 = 6/7
    #        建筑0->2 概率 = (10/3) / (70/3) = 10/70 = 1/7
    manual_before = np.array([0.0, 6.0 / 7.0, 1.0 / 7.0])

    # 断言：程序计算出的第一行（建筑0出发）与手算结果一致
    # 参1：程序计算出的第一行（建筑0出发）；参2：手算结果；参3：相对容差；参4：绝对容差
    np.testing.assert_allclose(values[0], manual_before, rtol = 1e-6, atol = 1e-8)

    # 手动计算验证（第二次：改变目的建筑面积）
    # 只改变目的建筑2的面积（30 -> 60），其他条件保持不变
    changed = buildings.copy()
    changed.loc[2, "floorspace"] = 60.0

    # 重新计算转移矩阵
    values_after = simple_gravity(changed).detach().cpu().numpy()

    # 手动计算新的概率：
    # 建筑0到建筑1：分数 = 20 / 1^2 = 20
    # 建筑0到建筑2：分数 = 60 / 3^2 = 60/9 = 20/3
    # 总分 = 20 + 20/3 = 80/3
    # 归一化：建筑0->1 概率 = 20 / (80/3) = 60/80 = 3/4
    #        建筑0->2 概率 = (20/3) / (80/3) = 20/80 = 1/4
    manual_after = np.array([0.0, 3.0 / 4.0, 1.0 / 4.0])

    # 断言：改变面积后，第一行的结果与新的手算结果一致
    np.testing.assert_allclose(values_after[0], manual_after, rtol = 1e-6, atol = 1e-8)

    # 断言：建筑2面积增加后，从建筑0转移到建筑2的概率应该变大（1/4 > 1/7）
    assert values_after[0, 2] > values[0, 2]

    # 打印输出部分
    print("合成输入：")
    print(buildings.to_string(index = False))

    print("原转移矩阵：")
    print(values)

    print("各行之和：", values.sum(axis=1))

    print("第一行修改前：", values[0])
    print("第一行修改后：", values_after[0])

    print("与手算的最大误差：",np.max(np.abs(values[0] - manual_before)), np.max(np.abs(values_after[0] - manual_after)))

    print("上述断言全部通过！")


# 3.测试
if __name__ == "__main__":
    main()






















