"""
案例：
    演示二分类任务的交叉熵损失函数

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

二分类交叉熵损失函数：BCELoss
    公式：
        Loss = - ylog(y^) - (1 - y)log(1 - y^)
    细节：
        因为公式中没有包含Sigmoid激活函数，所以使用BCELoss的时候还需要手动指定Sigmoid
"""

# 导包
import torch
import torch.nn as nn

# 1.定义函数，演示：二分类任务损失函数
def dm01():
    # 1.设置样本的真实值 -> 上述公式中的y
    y_true = torch.tensor([0, 1, 0], dtype = torch.float)

    # 2.设置样本的预测值(概率) -> 上述公式中的y^
    y_pred = torch.tensor([0.6901, 0.5423, 0.2639], requires_grad = True, dtype = torch.float)

    # 3.创建二分类交叉熵损失函数
    criterion = nn.BCELoss()       # 平均损失，来源于参数：reduction: str = "mean"

    # 4.计算损失值
    # loss = criterion(y_pred, y_true).detach().numpy()       # 转numpy前需要先detach复制一份，因为求导后无法直接转换
    loss = criterion(y_pred, y_true)
    print(f"损失值：{loss}")


# 2.测试
if __name__ == '__main__':
    dm01()


























