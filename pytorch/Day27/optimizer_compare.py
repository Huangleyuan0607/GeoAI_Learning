"""
程序名称：optimizer_compare.py
作者：黄乐源
日期：2026-07-24
描述：PyTorch 常见优化器（SGD, Momentum, AdaGrad, RMSProp, Adam）在同一神经网络任务上的性能对比与收敛曲线分析
"""

# 导包
import torch
import torch.nn as nn
import torch.optim as optim

# 1. 构造合成数据集（模拟回归任务）
torch.manual_seed(42)       # 设置随机种子
X = torch.randn(500, 20, dtype=torch.float32)
# 假设真实权重与偏置
w_true = torch.randn(20, 1, dtype=torch.float32)
y = torch.matmul(X, w_true) + 0.1 * torch.randn(500, 1, dtype=torch.float32)

# 2. 定义简单的多层感知机（MLP）模型
class simpleMLP(nn.Module):
    def __init__(self):
        super(simpleMLP, self).__init__()
        self.net = nn.Sequential(       # Sequential表示一个顺序容器，模块将按顺序执行
            nn.Linear(20, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )       # 线性层 + ReLU 激活函数 + 线性层 + ReLU 激活函数 + 线性层

    def forward(self, x):
        return self.net(x)

# 3. 编写通用训练函数
def train(optimizer_name, lr = 0.01, epochs = 100):     # 参1: 优化器名称；参2: 学习率；参3: 迭代轮数
    model = simpleMLP()
    criterion = nn.MSELoss()

    # 根据配置初始化优化器
    if optimizer_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr = lr)
    elif optimizer_name == "Momentum":
        optimizer = optim.SGD(model.parameters(), lr = lr, momentum = 0.9)
    elif optimizer_name == "AdaGrad":
        optimizer = optim.Adagrad(model.parameters(), lr =lr)
    elif optimizer_name == "RMSProp":
        optimizer = optim.RMSprop(model.parameters(), lr = lr, alpha = 0.99)
    elif optimizer_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr = lr, betas = (0.9, 0.999))
    else:
        raise ValueError("不支持的优化器名称")

    loss_history = []       # 存储每次迭代的损失值

    for epoch in range(epochs):
        model.train()           # 设置模型为训练模式
        optimizer.zero_grad()   # 清空梯度

        preds = model(X)                # 前向传播，得到预测值
        loss = criterion(preds, y)      # 计算损失值

        loss.backward()         # 反向传播，计算梯度
        optimizer.step()        # 更新参数

        loss_history.append(loss.item())    # 存储每次迭代的损失值

    return loss_history

# 4. 执行多优化器对比实验
print("================= 常见优化器性能对比实验 (Epochs=100, LR=0.01) =================")

optimizers = ["SGD", "Momentum", "AdaGrad", "RMSProp", "Adam"]
results = {}

for optim_name in optimizers:
    history = train(optim_name, lr = 0.01, epochs = 100)
    results[optim_name] = history
    print(f"优化器：{optim_name} | 初始loss：{history[0]:.4f} | 第50轮loss：{history[49]:.4f} | 最终loss：{history[-1]:.4f}")

print("\n================= 观察分析结果 =================")
print("1、朴素SGD收敛最慢，容易陷入局部极小或平坦区域")
print("2、Momentum引入动量积累，大幅加快了SGD的收敛速度")
print("3、RMSProp与Adam具备自适应学习率调整机制，在前20个Epoch内loss快速下降")
print("4、Adam综合性能优秀，在复杂非凸优化中能够兼顾收敛速度与平稳性")

print("\n🏁 Day27 优化器与梯度下降对比实验成功完成！")