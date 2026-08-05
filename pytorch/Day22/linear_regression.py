"""
程序名称：linear_regression.py
作者：黄乐源
日期：2026-07-19
描述：PyTorch 完整模型训练流程实战——模拟线性回归与 Loss 可视化
"""

# 导包
import torch
from torch.utils.data import TensorDataset      # 构造数据集对象
from torch.utils.data import DataLoader         # 数据加载器
from torch import nn                            # nn(neural network, 即神经网络)模块中有平方损失函数和假设函数
from torch import optim                         # optim模块中有优化器函数
from sklearn.datasets import make_regression    # 创建线性回归模型数据集
import matplotlib.pyplot as plt                 # 可视化，绘制图表

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签（解决中文乱码）
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号

print("================= 任务 1：准备合成数据集 =================")

# 方法1：使用make_regression创建线性回归模型数据集
# 随机生成100个样本x和初始参数coef，并加入噪声构建
x, y, coef = make_regression(
    n_samples = 100,        # 100条样本（100个样本点）
    n_features = 1,         # 1个特征（1个特征点）
    noise = 10,             # 噪声，噪声越大，样本点越散；反之越集中
    coef = True,            # 是否返回系数，默认为False，返回值为None
    bias = 10.0,             # 偏置
    random_state = 3        # 随机种子，随机种子相同，输出数据相同
)

print(type(x))      # <class 'numpy.ndarray'>
print(type(y))      # <class 'numpy.ndarray'>
print(type(coef))   # <class 'numpy.ndarray'>

# 把随机生成的x, y, coef(ndarray)封装成张量
x = torch.tensor(x, dtype = torch.float32)          # 特征
y = torch.tensor(y, dtype = torch.float32)          # 真实值
coef = torch.tensor(coef, dtype = torch.float32)    # 初始权重w，由make_regression随机生成

# 打印结果
print(f"数据集构建完成！x形状：{x.shape}，y形状：{y.shape}")
print(f'x:{x}, y:{y}, coef:{coef}')

# 方法2：使用PyTorch工作流随机生成线性回归模型数据集（用于理解构建随机数据集的原理与流程）
"""
def PyTorch_create_dataset():
    # 真实参数：w = 3.0, b = 2.0
    w_true = 3.0
    b_true = 2.0

    # 使用PyTorch工作流生成100个随机样本x，并加入高斯噪声构建y
    x = torch.randn(100, 1)
    noise = torch.randn(100, 1) * 0.2
    y = w_true * x + b_true + noise     # 即：y = w * x + b (+ noise噪声)

    # 返回结果
    print(f"数据集构建完成！x形状：{x.shape}，y形状：{y.shape}")
    return x, y, w_true, b_true
"""


print("\n================= 任务 2：构建线性回归模型 =================")

# 方法1：使用面向对象的类构建线性回归模型(后面学习会用，现在先了解)
"""
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        # 输入维度和输出维度均为1的全连接线性层
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)
    
model = LinearRegressionModel()
print("模型结构：\n", model)
"""

# 方法2：使用nn.Linear()构建线性回归模型（前期学习便于理解使用，后期选用方法1）
# 1.创建数据集对象，把tensor -> TensorDataset
dataset = TensorDataset(x, y)

# 2.创建数据加载器，把TensorDataset -> DataLoader
dataloader = DataLoader(dataset, batch_size = 16, shuffle = True)

# 3.创建初始的线性回归模型
model = nn.Linear(1, 1)
print("模型结构:\n", model)

print("\n================= 任务 3：配置损失函数与优化器 =================")

# 创建损失函数对象
criterion = nn.MSELoss()

# 创建优化器对象
optimizer = optim.SGD(model.parameters(), lr = 0.01)


print("\n================= 任务 4：开始模型训练循环 =================")

epochs = 100        # 总训练轮数
loss_list = []       # 存放每轮平均损失值的列表
total_loss = 0  # 存放总loss值
total_samples = 0  # 存放批次数，total_loss / total_samples用于计算每轮平均损失值（每轮有16个样本）

# 具体的训练过程
for epoch in range(epochs):
    for train_x, train_y in dataloader:
        optimizer.zero_grad()
        # 1. 前向传播(模型预测)
        y_pred = model(train_x)

        # 2.计算每批平均损失值
        loss = criterion(y_pred, train_y.reshape(-1, 1))    # 这里需要把1行n列的train_y转置成和y_pred一样的n行1列

        # 3.计算总损失和样本数
        total_loss += loss.item()
        total_samples += 1

        # 4.梯度清零
        optimizer.zero_grad()

        # 5.反向传播
        loss.sum().backward()

        # 6.梯度更新
        optimizer.step()

    # 7.把本轮的平均损失值添加到列表中
    loss_list.append(total_loss / total_samples)
    print(f"轮数：{epoch + 1}，平均损失值：{total_loss / total_samples}")

    if epoch % 10 == 0 or epoch == 1:
        # 获取当前学到的参数
        learned_w = model.weight.item()
        learned_b = model.bias.item()
        print(f"Epoch [{epoch:3d}/{epochs}] - Loss: {total_loss / total_samples:.4f} | 学到的 w: {learned_w:.4f}, b: {learned_b:.4f}")

print("真实权重coef:", coef.item())
print("模型权重:", model.weight.item())

print("真实偏置bias:", 10)
print("模型偏置:", model.bias.item())

print("\n================= 任务 5：拟合结果与 Loss 曲线可视化 =================")

# 绘制 Loss 收敛曲线
plt.plot(range(1, epochs + 1), loss_list, color='green', linewidth=2)
plt.xlabel('轮次 Epochs')
plt.ylabel('每轮平均损失值 MSE Loss')
plt.title('损失值曲线变化图')

plt.grid(True)
plt.show()

# 绘制拟合直线与数据点
plt.scatter(x.numpy(), y.numpy(), color='blue')     # 绘制真实数据散点，颜色为蓝色

# 计算预测值
with torch.no_grad():
    predictions = model(x).numpy()
plt.plot(x.numpy(), predictions, color='red', linewidth=2, label='预测值')

# 计算真实值
y_true = torch.tensor(data = [coef * v+ 10 for v in x])
plt.plot(x, y_true, color = "green", label = "真实值")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()        # 图例
plt.grid(True)      # 网格
plt.show()


print("\n🏁 Day22 GeoAI PyTorch 线性回归模型训练实战完成！")