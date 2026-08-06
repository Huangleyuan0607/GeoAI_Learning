"""
程序名称：mlp_network.py
作者：黄乐源
日期：2026-07-20
描述：PyTorch 神经网络结构探究——搭建简单多层感知机 (MLP) 与 Sigmoid/Tanh 激活函数实战
"""

# 导包
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']      # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False        # 用来正常显示负号

print("================= 任务 1：搭建简单多层感知机 (MLP) （先以了解为主）=================")

class SimpleMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleMLP, self).__init__()
        # 第一层：输入层 -> 隐藏层
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        # 激活函数
        self.sigmoid = nn.Sigmoid()
        # 第二层：隐藏层 -> 输出层
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        out = self.fc1(x)
        out = self.sigmoid(out)
        out = self.fc2(out)
        return out

# 实例化模型
input_size = 10
hidden_size = 20
output_size = 2

model = SimpleMLP(input_size, hidden_size, output_size)
print("自定义 MLP 模型结构:\n", model)

# 测试前向传播
dummy_input = torch.randn(5, input_size)  # Batch Size = 5
output = model(dummy_input)         # 执行前向传播
print(f"输入张量形状: {dummy_input.shape}")
print(f"输出张量形状: {output.shape}")

print("\n================= 任务 2：激活函数特性计算与可视化 =================")

# 生成区间 [-6, 6] 的200个连续数据
x = torch.linspace(-6, 6, 200)

# 计算 Sigmoid 与 Tanh
# 方法1：函数方式 -> 适用于简单计算
# y_sigmoid = torch.sigmoid()
# y_tanh = torch.tanh()

# 方法2：创建激活函数层（Layer方式） -> 适用于搭建神经网络
sigmoid_layer = nn.Sigmoid()
tanh_layer = nn.Tanh()

y_sigmoid = sigmoid_layer(x)
y_tanh = tanh_layer(x)

# 绘制曲线
# 方法1：面向对象写法

fig, axes = plt.subplots(1, 2)
axes[0].plot(x, y_sigmoid, label="sigmoid")
axes[0].set_title("Sigmoid激活函数")
axes[0].set_xlabel("Input x")
axes[0].set_ylabel("Output y")
# axes[0].set_xlim(-20, 20)       # 设置x轴的显示范围,但这里我们设置x的生成范围是(-6, 6)
axes[0].legend()
axes[0].grid()

axes[1].plot(x, y_tanh, label="tanh")
axes[1].set_title("Tanh激活函数")
axes[1].set_xlabel("Input x")
axes[1].set_ylabel("Output y")
# axes[1].set_xlim(-20, 20)       # 设置x轴的显示范围,但这里我们设置x的生成范围是(-6, 6)
axes[1].legend()
axes[1].grid()


# 方法2：pyplot状态机写法
"""plt.subplot(1, 2, 1)
plt.plot(x.numpy(), y_sigmoid.numpy(), color='blue', linewidth=2, label='Sigmoid')
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.axhline(1, color='black', linestyle='--', alpha=0.5)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input x")
plt.ylabel("Output y")
# plt.xlim(-20, 20)       # 设置x轴的显示范围,但这里我们设置x的生成范围是(-6, 6)
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x.numpy(), y_tanh.numpy(), color='red', linewidth=2, label='Tanh')
plt.axhline(-1, color='black', linestyle='--', alpha=0.5)
plt.axhline(1, color='black', linestyle='--', alpha=0.5)
plt.title("Tanh Activation Function")
plt.xlabel("Input x")
plt.ylabel("Output y")
# plt.xlim(-20, 20)       # 设置x轴的显示范围,但这里我们设置x的生成范围是(-6, 6)
plt.grid(True)
plt.legend()"""

plt.tight_layout()      # 自动调整文字布局，防止文字被遮挡
plt.show()

print("\n🏁 Day23 GeoAI 神经网络结构与 MLP 搭建学习完成！")