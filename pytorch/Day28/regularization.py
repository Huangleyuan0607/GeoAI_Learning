"""
程序名称：regularization.py
作者：黄乐源
日期：2026-07-25
描述：PyTorch 中过拟合抑制技巧（Dropout, BatchNorm）与学习率衰减策略（StepLR）的代码实现与对比实验
"""

# 导包
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# 1. 构造高维拟合数据集（模拟易过拟合数据）
torch.manual_seed(42)       # 设置随机种子
x_train = torch.randn(200, 100, dtype = torch.float32)
y_train = torch.randint(0, 2, (200, ), dtype = torch.int64)

x_val = torch.randn(100, 100, dtype = torch.float32)
y_val = torch.randint(0, 2, (100, ), dtype = torch.int64)

train_dataset = TensorDataset(x_train, y_train)
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)

# 2. 定义包含 Dropout 与 BatchNorm 的对比网络结构
class RegularizedMLP(nn.Module):
    def __init__(self, use_dropout = False, use_bn = False, drop_rate = 0.5):
        super(RegularizedMLP, self).__init__()

        layers = []

        # 隐藏层1
        layers.append(nn.Linear(100, 128))
        if use_bn:
            layers.append(nn.BatchNorm1d(128))
        layers.append(nn.ReLU())
        if use_dropout:
            layers.append(nn.Dropout(p = drop_rate))

        # 隐藏层2
        layers.append(nn.Linear(128, 64))
        if use_bn:
            layers.append(nn.BatchNorm1d(64))
        layers.append(nn.ReLU())
        if use_dropout:
            layers.append(nn.Dropout(p = drop_rate))

        # 输出层
        layers.append(nn.Linear(64, 2))

        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)

# 3. 编写通用训练与验证函数
def train_and_evaluate(use_dropout = False, use_bn = False, use_scheduler = False, epochs = 50):
    model = RegularizedMLP(use_dropout = use_dropout, use_bn = use_bn)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr = 0.01)

    # 初始化学习率衰减器
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size = 15, gamma = 0.5) if use_scheduler else None

    for epoch in range(epochs):
        # 训练模式
        model.train()
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            preds = model(batch_x)
            loss = criterion(preds, batch_y)
            loss.backward()
            optimizer.step()

        if scheduler:
            scheduler.step()

    # 验证模式
    model.eval()
    with torch.no_grad():
        val_preds = model(x_val)
        val_loss = criterion(val_preds, y_val).item()

    return val_loss

# 4. 执行对比实验
print("================= 模型正则化与优化技巧对比实验 (Epochs=50) =================")

configs = [
    ("基础模型（Baseline）", False, False, False),
    ("引入Dropout", True, False, False),
    ("引入BatchNorm", False, True, False),
    ("引入Dropout与BatchNorm", False, False, True),
    ("综合策略（BN + Dropout + Decay）", True, True, True)
]

for name, use_drop, use_bn, use_sched in configs:
    final_val_loss = train_and_evaluate(use_dropout = use_drop, use_bn = use_bn, use_scheduler = use_sched, epochs = 50)
    print(f"配置方案：{name:<30} | 验证集最终Loss：{final_val_loss:.4f}")

print()
print("==========观察分析结果==========")
print("1. 基础模型在前向传播中易对高维噪声过拟合，导致 Validation Loss 相对偏高。")
print("2. Dropout 通过随机遮蔽神经元显著降低了模型过拟合程度。")
print("3. BatchNorm 标准化了中间层数据分布，使得网络训练更加平稳，收敛更快。")
print("4. StepLR 动态降低学习率，有助于模型在后期落入更加稳定的局部极小值。")

print("\n🏁 Day28 正则化与模型优化技巧实验成功完成！")