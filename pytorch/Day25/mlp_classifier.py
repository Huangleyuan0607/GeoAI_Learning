"""
程序名称：mlp_classifier.py
作者：黄乐源
日期：2026-07-22
描述：PyTorch 多层感知机 (MLP) 网络结构搭建、前向传播与模型参数分析实战
"""

# 导包
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plt
from torchsummary import summary

"""
print("================= 任务 1：构建分类数据集 =================")

# 随机生成 3 簇 2 维分类数据（模拟 3 分类任务）
torch.manual_seed(42)       # 设置随机种子

n_samples = 300
class_0 = torch.randn(n_samples, 2) + torch.tensor([-2.0, -2.0])   # 先生成300行2列的正态分布数据，再将所有数据向左下偏移2个单位，即生成中心在(-2, -2)的一团点
class_1 = torch.randn(n_samples, 2) + torch.tensor([2.0, 2.0])     # 先生成300行2列的正态分布数据，再将所有数据向右上偏移2个单位，即生成中心在(2, 2)的一团点
class_2 = torch.randn(n_samples, 2) + torch.tensor([-2.0, 2.0])    # 先生成300行2列的正态分布数据，再将所有数据向左上偏移2个单位，即生成中心在(-2, 2)的一团点

x = torch.cat([class_0, class_1, class_2], dim = 0)     # 按行合并三个类别的数据
y = torch.cat([torch.zeros(n_samples), torch.ones(n_samples), torch.full((n_samples,), 2)], dim = 0).long()   # 生成类别编号，类型为int64

# 划分训练集与测试集 (8:2) -> 把前面生成的900个样本随机打乱，然后按照8:2比例划分为训练集和测试集。
# 训练集（train set）：用于模型学习参数
indices = torch.randperm(x.size(0))     # 生成一个随机排列的整数序列当作索引，数量与x的第0维大小相同。
x, y = x[indices], y[indices]           # 按随机索引重新排列数据

train_size = int(0.8 * len(x))      # 定义训练集大小，这里为：0.8 * 900 = 720；从而得到测试集大小为900 - 720 = 180
x_train, x_test = x[:train_size], x[train_size:]        # 取x的前720个为训练集，后180个为测试集
y_train, y_test = y[:train_size], y[train_size:]        # 同步划分标签，取y的前720个为训练标签，后180个为测试标签

# 构造 Dataset -> DataLoader
train_dataset = TensorDataset(x_train, y_train)
# 参1：数据集对象；参2：批次大小（每批样本数量）；参3：是否打乱数据（如果不打乱，多轮训练时每轮拿到的值是一样的）（训练集打乱，测试集不打乱）
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)

print(f"训练集样本数：{len(x_train)}，测试集样本数：{len(x_test)}")
"""

print("\n=================任务1：创建模拟输入数据=================")

data = torch.randn(size=(5,3))

print("输入数据：", data)
print("输入数据shape:", data.shape)


print("\n================= 任务 2：搭建 MLP 分类网络 =================")

class MLPClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes):
        super(MLPClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, num_classes)

        # 参数初始化
        nn.init.kaiming_normal_(self.fc1.weight, nonlinearity='relu')
        nn.init.kaiming_normal_(self.fc2.weight, nonlinearity='relu')

    def forward(self, x):
        # 第一层 隐藏层：加权求和 + 激活函数ReLU
        x = torch.relu(self.fc1(x))
        # 第二层 隐藏层：加权求和 + 激活函数ReLU
        x = torch.relu(self.fc2(x))
        # 第三层 输出层：加权求和 + 激活函数Softmax（因为本案例做的是三分类）
        output = torch.softmax(self.output(x), dim = -1)  # dim = -1在此处表示按行计算，一条样本一条样本地处理
        return output
print("MLP分类网络搭建完成！")

print("\n================= 任务 3：模型前向传播实验 =================")

# 1. 创建模型
my_model = MLPClassifier(input_dim = 3, hidden_dim = 16, num_classes = 3)
print("网络结构：", my_model)

# 2. 创建模拟输入数据
# 5个样本，每个样本3个特征
data = torch.randn(size=(5, 3))
print("\n输入数据:", data)
print("\n输入数据形状:", data.shape)

# 3. 模型进入预测模式
my_model.eval()

# 4. 前向传播
with torch.no_grad():
    output = my_model(data)

print("\n模型输出:", output)
print("\n输出形状:", output.shape)

# 5. 查看每个样本预测概率
for i in range(len(output)):
    print(f"\n第{i + 1}个样本:")
    print("类别概率:", output[i])

    # 最大概率对应类别
    pred_class = torch.argmax(output[i])
    print("预测类别:", pred_class.item())
    print("-" * 30)

print("\n================= 任务 4：模型参数分析 =================")

print("==================计算模型参数==================")
# 参1：（神经网络）模型对象；参2：输入数据的维度(5, 3)
summary(my_model, input_size=(5, 3))        # 此处input_size的shape与输入数据集data相同。在输出结果的Output Shape中，-1代表自动计算，表示不确定

print("==================查看模型参数==================")
for name, param in my_model.named_parameters():
    print("name：", name)
    print("param：", param)
    print()

print("\n🏁 Day25 MLP 分类网络训练实战成功完成！")