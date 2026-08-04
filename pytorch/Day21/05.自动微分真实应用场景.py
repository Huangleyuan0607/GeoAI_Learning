"""
案例：
    演示自动微分的真实应用场景

结论：
    1.先前向传播（正向传播），计算出预测值z
    2.基于损失函数，结合预测值z和真实值y，来计算梯度
    3.结合权重更新公式：W新 = W旧 - 学习率 * 梯度，来更新权重
"""

# 导包
import torch

# 1.定义x，表示：特征（输入数据），假设：2行5列，全1矩阵
x = torch.ones(2, 5)
print("x:", x)

# 2.定义y，表示：标签（真实值），假设：2行3列，全0矩阵
y = torch.zeros(2, 3)
print("y:", y)

# 3.初始化（可自动微分）的权重和偏置
w = torch.randn(5, 3, requires_grad = True)     # x @ w + b
print("w:", w)

b = torch.randn(3, requires_grad = True)        # 1列1个b
print("b:", b)

# 4.前向传播（正向传播），计算出预测值z
z = torch.matmul(x, w) + b
# z = x @ w + b     # 效果同上
print("z:", z)

# 5.定义损失函数
criterion = torch.nn.MSELoss()      # nn =neural network：神经网络
loss = criterion(z, y)      # loss = 损失
print("loss:", loss)

# 6.进行自动微分，求导，结合反向传播，更新权重
loss.backward()

# 7.打印w, b用来更新的梯度
print("w的梯度:", w.grad)
print("b的梯度:", b.grad)

# 后续就是：W新 = W旧 - 学习率 * 梯度，来更新权重
w.data = w.data - 0.01 * w.grad
b.data = b.data - 0.01 * b.grad
print(f"权重初始值：{w}，(0.01 * w.grad)：{0.01 * w.grad}，loss：{loss:.5f}")
print(f"偏置初始值：{b}，(0.01 * b.grad)：{0.01 * b.grad}，loss：{loss:.5f}")





