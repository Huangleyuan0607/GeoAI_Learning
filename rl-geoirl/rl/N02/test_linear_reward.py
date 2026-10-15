"""
来源：论文官方开源代码 geoirl-official
原始文件：rewards.py
类名/函数名：Perceptron / Perceptron.forward

描述：
    节选官方的线性奖励模型，将每栋建筑的特征映射为一个奖励标量。
    保留官方类的计算逻辑，额外增加详细注释和三栋建筑的合成测试。

数学公式：
    单栋建筑：r(x) = x1 * w1 + x2 * w2 + b。
    整批建筑：rewards = X @ W.T + b。
    本日 X 的形状是 (3, 2)，W 是 (1, 2)，b 是 (1,)，输出是 (3, 1)。

实现细节：
    nn.Linear(n_features, 1) 包含权重和偏置，默认没有激活函数。
    测试手动将权重固定为 [1, 2]，偏置固定为 0.5，方便先手算再验证。
    再只修改第三栋建筑的一个特征，检查奖励变化是否符合线性公式。

注意：
    这里输出的是即时奖励，不是访问概率、折扣回报、V或Q。
    合成特征没有对应论文中的具体地理属性；本测试不进行IRL训练。
    官方目录保持原样，不直接修改原文件，也不导入整个rewards.py。
"""


# 导包
import numpy as np
import torch
from pyexpat import features
from torch import nn


# 1.定义奖励模型，计算逻辑与官方 Perceptron 一致
class Perceptron(nn.Module):
    # 参2：每栋建筑有多少个特征，即特征矩阵的列数，不是建筑数量；参3：随机种子
    def __init__(self, n_features, seed = 0):
        # 1.初始化
        super().__init__()

        # 2.设置随机种子，影响初始权重w和偏置b
        torch.manual_seed(seed)

        # 3.定义线性层
        self.linear = nn.Sequential(nn.Linear(n_features, 1))

    def forward(self, features):
        # 4.前向传播
        return self.linear(features)

# 2.定义主函数，用合成数据测试线性奖励模型
def main():
    # 1.构造3栋建筑，每栋2个特征的输入，形状为 (3, 2)
    # 第0行代表宿舍，第1行代表教学楼，第2行代表商店
    features = torch.tensor([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0]], dtype = torch.float32)

    # 2.按特征列数创建模型：features.shape[1] = 2
    # features.shape[0]=3 是建筑数量，不能拿它当 n_features
    model = Perceptron(n_features = features.shape[1], seed = 0)

    # 3.找到线性层
    linear_layer = model.linear[0]

    # 4.手动固定权重w和偏置b，不进行训练
    # copy_ 是原位复制，保留线性层原来的参数对象；末尾下划线表示原位操作
    with torch.no_grad():
        # weight 必须是 (输出维数, 输入维数) = (1, 2)
        linear_layer.weight.copy_(torch.tensor([[1.0, 2.0]], dtype = torch.float32))
        # bias 对每栋建筑的输出统一加0.5，形状为 (1,)
        linear_layer.bias.copy_(torch.tensor([0.5], dtype=torch.float32))

        # 5.前向传播
        rewards = model(features)

    # 6.将结果转为 Numpy 数组
    # detach：与计算图分离；cpu：放到CPU；numpy：转换为 NumPy 数组
    # 本次 no_grad 后已没有梯度图，保留此写法也便于以后使用
    values = rewards.detach().cpu().numpy()
    weights = linear_layer.weight.detach().cpu().numpy()
    bias = linear_layer.bias.detach().cpu().numpy()

    # 7.写入独立手算结果，注意保留列向量形状：(3, 1)
    # 建筑0的rewards：r0 = 1 * 0 + 2 * 0 + 0.5 = 0.5
    # 建筑1的rewards：r1 = 1 * 1 + 2 * 0 + 0.5 = 1.5
    # 建筑2的rewards：r2 = 1 * 0 + 2 * 1 + 0.5 = 2.5
    expected = np.array([[0.5], [1.5], [2.5]], dtype = np.float32)

    # 8.分别检查输入、参数、输出的形状，防止把特征维护与建筑数量混淆
    assert tuple(features.shape) == (3, 2), "特征矩阵形状应为(3, 2)"
    assert weights.shape == (1, 2), "权重形状应为(1, 2)"
    assert bias.shape == (1,), "偏置形状应为(1,)"
    assert values.shape == (3, 1), "每栋建筑应输出一个奖励"
    assert np.isfinite(values).all(), "奖励中不能出现 NaN 或 Inf"       # 不能出现 NaN 或无穷大

    # 9.与独立手算结果比较：浮点数用容差判断，不直接要求逐位完全相等
    np.testing.assert_allclose(weights, [[1.0, 2.0]], atol = 1e-6, rtol = 1e-6)
    np.testing.assert_allclose(bias, [0.5], atol = 1e-6, rtol = 1e-6)
    np.testing.assert_allclose(values, expected, atol = 1e-6, rtol = 1e-6)
    max_error = float(np.max(np.abs(values - expected)))

    # 10.只改变第三栋建筑的第二个特征： 1 -> 2
    changed_features = features.clone()
    changed_features[2, 1] = 2.0

    with torch.no_grad():
        changed_rewards = model(changed_features)
    changed_values = changed_rewards.detach().cpu().numpy()

    # 11.再次手算：
    # 建筑2的rewards：r2 = 1 * 0 + 2 * 2 + 0.5 = 4.5
    # 前两栋特征、权重和偏置都没变，所以结果也不会变
    expected_changed = np.array([[0.5], [1.5], [4.5]], dtype = np.float32)
    assert changed_values.shape == (3, 1), "修改特征后输出形状仍应为 (3, 1)"
    assert np.isfinite(changed_values).all(), "修改后的奖励也应为有限数值"
    np.testing.assert_allclose(changed_values, expected_changed, atol = 1e-6, rtol = 1e-6)

    # 12.检查奖励差值：第二个特征增加1，乘以对应权重2，第三栋建筑奖励增加2
    # 前两栋应加0（不变），第三栋应加2
    delta = changed_values - values
    np.testing.assert_allclose(delta, [[0.0], [0.0], [2.0]], atol = 1e-6, rtol = 1e-6)

    # 13.打印需要复查的字段
    # flatten 只用于把打印结果展开，真正的输出仍然是 (3, 1)
    print("features shape:", tuple(features.shape))
    print("features:\n", features.detach().cpu().numpy())
    print("weight shape:", weights.shape, "weight:", weights)
    print("bias shape:", bias.shape, "bias:", bias)
    print("reward shape:", values.shape)
    print("original rewards:", values.flatten())
    print("manual rewards:", expected.flatten())
    print("max absolute error:", max_error)
    print("changed features:\n", changed_features.detach().cpu().numpy())
    print("changed rewards:", changed_values.flatten())
    print("reward delta:", delta.flatten())
    print("测试通过！")


# 3.测试
if __name__ == "__main__":
    main()


