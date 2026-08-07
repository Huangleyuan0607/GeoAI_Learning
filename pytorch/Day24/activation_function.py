"""
程序名称：activation_function.py
作者：黄乐源
日期：2026-07-21
描述：PyTorch 常用激活函数特性对比 (Sigmoid, Tanh, ReLU, Softmax) 与参数初始化 (Xavier / Kaiming) 实战
"""

# 导包
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

print("================= 任务 1：Sigmoid, Tanh 与 ReLU 激活函数可视化对比 =================")

# 生成区间 [-6, 6] 的连续数据
x = torch.linspace(-6, 6, 300)

# 实例化激活函数模块
y_sigmoid = nn.Sigmoid()
y_tanh = nn.Tanh()
y_relu = nn.ReLU()

# 绘制三图对比
fig, axes = plt.subplots(1,3)

# 1. Sigmoid
axes[0].plot(x, y_sigmoid(x))
axes[0].set_title('sigmoid')
axes[0].set_xlabel('Input x')
axes[0].set_ylabel('Output y')
axes[0].grid(True)
axes[0].legend()

# 2. Tanh
axes[1].plot(x, y_tanh(x))
axes[1].set_title('Tanh')
axes[1].set_xlabel('Input x')
axes[1].set_ylabel('Output y')
axes[1].grid(True)
axes[1].legend()

# 3. ReLU
axes[2].plot(x, y_relu(x))
axes[2].set_title('ReLU')
axes[2].set_xlabel('Input x')
axes[2].set_ylabel('Output y')
axes[2].grid(True)
axes[2].legend()

plt.tight_layout()
plt.show()

print("\n================= 任务 2：Softmax 多分类概率转换实验 =================")

# 假设神经网络对 3 个样本的 4 分类 Logits 输出
logits = torch.tensor([
    [2.0, 1.0, 0.1, 0.5],
    [0.5, 3.2, 0.1, 0.2],
    [-1.0, 0.0, 2.5, 1.1]
])

softmax = nn.Softmax(dim = 1)       # 按列计算（dim=0则按行计算）
probabilities = softmax(logits)

print("原始logits得分：", logits)
print("经过Softmax激活函数处理后的类别概率：", probabilities)
print("每个样本所有类别概率之和：", probabilities.sum(dim = 1))      # 等同于torch.sum(probabilities, dim = 1)

print("\n================= 任务 3：PyTorch 参数初始化实战 =================")

class CustomNet(nn.Module):
    def __init__(self):
        super(CustomNet, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(20, 5)

        # 执行参数初始化
        self._init_weights()

    def _init_weights(self):
        # 对 Linear 层做 Kaiming 正态分布初始化（针对 ReLU 激活）
        nn.init.kaiming_normal_(self.fc1.weight, nonlinearity = 'relu')

        # 使用固定值初始化来对fc1层偏置进行初始化
        nn.init.constant_(self.fc1.bias, 0.0)

        # 对最后一层输出层做 Xavier 均匀分布初始化
        nn.init.xavier_uniform_(self.fc2.weight)

        # 使用固定值初始化来对fc2层偏置进行初始化
        # nn.init.constant_(self.fc2.bias, 0.0)
        nn.init.zeros_(self.fc2.bias)       # 效果同上

    def forward(self, x):
        x = self.relu(self.fc1(x))
        out = self.fc2(x)
        return out

net = CustomNet()
print("自定义网络权重shape：", net.fc1.weight.shape)
print("fc1层权重前2行初始化数值实例：", net.fc1.weight[:2])
print("fc1层偏置前5项初始化数值实例：", net.fc1.bias[:5])

print("\n🏁 Day24 激活函数与参数初始化实验成功完成！")