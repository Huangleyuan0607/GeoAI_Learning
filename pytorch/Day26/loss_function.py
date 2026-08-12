"""
程序名称：loss_function.py
作者：黄乐源
日期：2026-07-23
描述：PyTorch 常见损失函数（CrossEntropyLoss, BCEWithLogitsLoss, MSELoss, L1Loss, SmoothL1Loss）使用规范与计算逻辑实战
"""

# 导包
import torch
import torch.nn as nn
from torch.nn import SmoothL1Loss

print("================= 任务 1：多分类交叉熵损失 (CrossEntropyLoss) =================")

# 模拟网络输出（即预测值y_pred）：3个样本，3个类别（未经 Softmax 的原始 Logits）
logits = torch.tensor([
    [2.0, 1.0, 0.1],        # 预测样本0最可能是类别0
    [0.5, 3.0, 0.2],        # 预测样本1最可能是类别1
    [0.1, 0.8, 2.5]         # 预测样本2最可能是类别2
], dtype = torch.float32)

# 真实类别标签（真实值）：维度为 (N,)，元素类型必须为 torch.int64 (Long)
y_true = torch.tensor([0, 1, 2], dtype = torch.long)

# 实例化损失函数
criterion = nn.CrossEntropyLoss()

# 计算损失
loss = criterion(logits, y_true)

print("多分类预测值y_pred：\n", logits)
print(f"真实值y_true：{y_true}")
print(f"nn.CrossEntropyLoss计算结果：{loss.item():.4f}")


print("\n================= 任务 2：二分类交叉熵损失 (BCELoss) =================")

# 模拟二分类网络输出：4个样本（未经过 Sigmoid 的 Logits）
binary_logits = torch.tensor([0.5, 0.7, 0.3, 0.8], requires_grad = True, dtype = torch.float)

# 真实标签：0 或 1
binary_targets = torch.tensor([1, 0, 1, 0], dtype = torch.float)

# 使用BCELoss
criterion = nn.BCELoss()
loss = criterion(binary_logits, binary_targets)

print("二分类logits：\n", binary_logits)
print("真实标签targets：", binary_targets)
print(f"nn.BCELoss计算结果：{loss.item():.4f}")


print("\n================= 任务 3：回归损失函数对比 (MSE, MAE, Smooth L1) =================")

# 模拟回归任务预测值与真实值（例如地表温度预测，单位：摄氏度）
pred_regression = torch.tensor([23.5, 18.0, 30.2, 15.0], dtype = torch.float32)
target_regression = torch.tensor([23.9, 20.0, 25.0, 15.2], dtype = torch.float32)       # 注意：第3个样本差距较大(5.2)，属于离群点

# 1. 平均绝对误差损失 L1Loss (MAE)
l1_loss = nn.L1Loss()
loss_mae = l1_loss(pred_regression, target_regression)

# 2. 均方误差损失 MSELoss
l2_loss = nn.MSELoss()
loss_mse = l2_loss(pred_regression, target_regression)

# 3. 平滑 L1 损失 SmoothL1Loss
smooth_l1_loss = nn.SmoothL1Loss()
loss_smooth_l1 = smooth_l1_loss(pred_regression, target_regression)

# 4.打印结果
print("预测值：", pred_regression)
print("真实值：", target_regression)
print("-" * 30)
print(f"1、L1 Loss(MAE)：{loss_mae.item():.4f}")
print(f"2、L2 Loss(MSE)：{loss_mse.item():.4f}")
print(f"3、Smooth L1 Loss(Smooth L1)：{loss_smooth_l1.item():.4f}")

print("\n🏁 Day26 深度学习损失函数实战与对比成功完成！")