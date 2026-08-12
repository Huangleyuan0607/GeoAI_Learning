"""
案例：
    演示回归任务的交叉熵损失函数

损失函数介绍：
    概述：
        损失函数也叫成本函数，目标函数，代价函数，误差函数，就是用来衡量模型好坏（模型拟合情况）的
    分类：
        分类问题：
            多分类交叉熵损失函数：CrossEntropyLoss
            二分类交叉熵损失函数：BCELoss
        回归问题：
            MAE:Mean Absolute Error，平均绝对误差
            MSE:Mean Squared Error，均方误差
            Smooth L1:结合上述两个的特点做的升级，优化

回归任务常用损失函数：
    MAE：Mean Absolute Error，平均绝对误差
        公式：
            误差绝对值之和 / 样本总数
        类似于L1正则化，权重可以降为0，数据会变得稀疏

        弊端：
            在0点不平滑（不可导），可能错过最小值

    MSE：Mean Squared Error，均方误差
        公式：
            误差平方之和 / 样本总数
        弊端：
            如果差值过大，可能存在梯度爆炸的情况。W新 = W旧 - 学习率 * 梯度

    Smooth L1：结合上述两个的特点做的升级，优化
        就是基于MAE和MSE做的综合，在[-1, 1]段是L2(MSE)，其他段是L1(MAE)
        这样既解决了L1不平滑的问题（0点不可导，可能错过最小值）
        又解决了L2(MSE)的梯度爆炸问题
"""

# 导包
import torch
import torch.nn as nn

# 1.定义函数，演示：MAE损失函数
def dm01():
    # 1.设置样本的真实值
    y_true = torch.tensor([2.0, 2.0, 2.0], dtype = torch.float32)

    # 2.设置样本的预测值(概率)
    y_pred = torch.tensor([1.0, 1.0, 1.9], requires_grad = True, dtype = torch.float32)

    # 3.创建MAE损失函数
    criterion = nn.L1Loss()       # 一般充当其他函数的正则化项，用以调参

    # 4.计算损失值
    # loss = criterion(y_pred, y_true).detach().numpy()       # 转numpy前需要先detach复制一份，因为求导后无法直接转换
    loss = criterion(y_pred, y_true)
    print(f"MAE损失值：{loss}")

# 2.定义函数，演示：MSE损失函数
def dm02():
    # 1.设置样本的真实值
    y_true = torch.tensor([2.0, 2.0, 2.0], dtype = torch.float32)

    # 2.设置样本的预测值(概率)
    y_pred = torch.tensor([1.0, 1.0, 1.9], requires_grad = True, dtype = torch.float32)

    # 3.创建MSE损失函数
    criterion = nn.MSELoss()

    # 4.计算损失值
    # loss = criterion(y_pred, y_true).detach().numpy()       # 转numpy前需要先detach复制一份，因为求导后无法直接转换
    loss = criterion(y_pred, y_true)
    print(f"MSE损失值：{loss}")

# 3.定义函数，演示：Smooth L1损失函数
def dm03():
    # 1.设置样本的真实值
    y_true = torch.tensor([2.0, 2.0, 2.0], dtype = torch.float32)

    # 2.设置样本的预测值(概率)
    y_pred = torch.tensor([1.0, 1.0, 1.9], requires_grad = True, dtype = torch.float32)

    # 3.创建Smooth L1损失函数
    criterion = nn.SmoothL1Loss()       # 回归问题优先用
    # criterion = nn.CrossEntropyLoss()     # 分类问题优先用

    # 4.计算损失值
    # loss = criterion(y_pred, y_true).detach().numpy()       # 转numpy前需要先detach复制一份，因为求导后无法直接转换
    loss = criterion(y_pred, y_true)
    print(f"Smooth L1损失值：{loss}")

# 4.测试
if __name__ == '__main__':
    dm01()      # 损失值：0.699999988079071
    dm02()      # 损失值：0.6700000166893005
    dm03()      # 损失值：0.33500000834465027


























