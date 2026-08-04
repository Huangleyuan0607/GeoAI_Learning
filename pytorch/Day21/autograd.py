"""
程序名称：autograd.py
作者：黄乐源
日期：2026-07-18
描述：PyTorch 张量拼接、自动求导 (Autograd) 机制、梯度更新与计算图截断实战
"""

# 导包
import torch

print("================= 任务 1：张量拼接操作 (cat vs stack) =================")

# 模拟两期遥感单波段 Feature Map (H=4, W=4)
feat_t1 = torch.randn(4, 4)
feat_t2 = torch.randn(4, 4)

# 1. torch.cat 按照现有维度拼接 (通道扩展/特征融合)
cat_res = torch.cat((feat_t1, feat_t2), dim = 0)        # (4, 4) + (4, 4) = (8, 4)
print("torch.cat(dim=0)拼接后形状:", cat_res.shape)      # (8, 4)

# 2. torch.stack 增加新维度拼接 (时间序列维度/Batch维度构建)
stack_res = torch.stack((feat_t1, feat_t2), dim = 0)    # (4, 4) + (4, 4) = (2, 4, 4)
print("torch.stack(dim=0)堆叠后形状:", stack_res.shape)      # (2, 4, 4)

print("\n================= 任务 2：自动求导 (Autograd) 基础流程 =================")

# 假设 w 为待优化参数 (如权重)，x 为输入特征
w = torch.tensor(2.0, requires_grad = True)
b = torch.tensor(1.0, requires_grad = True)
x = torch.tensor(3.0)
y_true = torch.tensor(10.0)     # 真实值

# 1. 正向传播 (Forward)
y_pred = w * x + b      # y = w * x + b
criterion = torch.nn.MSELoss()        # MSE损失
loss = criterion(y_pred, y_true)

print(f"正向传播预测值：{y_pred.item():.2f}, loss：{loss.item():.2f}")

# 2. 反向传播 (Backward)
loss.backward()

# 3. 查看梯度
print("w的梯度:", w.grad)
print("b的梯度:", b.grad)

print("\n================= 任务 3：循环更新参数与梯度清零 (grad.zero_) =================")

# 重新初始化参数
w = torch.tensor(2.0, requires_grad = True)
learning_rate = 0.01        # 设置学习率

print("开始 3 轮循环参数更新模拟:")
for i in range(1, 4):
    # 正向传播
    y_pred = w * x
    loss = (y_pred - y_true) ** 2

    # 手动将梯度清零，防止下一轮梯度累加
    if w.grad is not None:
        w.grad.zero_()

    # 反向传播计算梯度
    loss.backward()

    # 模拟无梯度追踪环境下的参数更新
    with torch.no_grad():
        w.data = w.data - learning_rate * w.grad
        # w.data.sub_(learning_rate * w.grad)  # 效果同上，安全更新

    print(f"Epoch {i} - Loss: {loss.item():.4f}, 当前w的梯度: {w.grad.item():.4f}, 更新后的w: {w.item():.4f}")

print("\n================= 任务 4：计算图截断 (detach 与 no_grad) =================")

x = torch.tensor([2.0], requires_grad=True)
y = x ** 2

# 使用 detach 截断梯度流
y_detached = y.detach()
z = y_detached * 3

print("y_detached的requires_grad状态:", y_detached.requires_grad)      # False
print("z的requires_grad状态:", z.requires_grad)        # False

# 验证 no_grad 上下文
with torch.no_grad():
    m = x * 5

print("no_grad内创建张量的requires_grad状态:", m.requires_grad)     # False

print("\n🏁 Day21 GeoAI PyTorch 自动求导与梯度更新实战完成！")