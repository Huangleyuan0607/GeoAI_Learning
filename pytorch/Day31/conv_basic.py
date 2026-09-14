# 导包
import torch
import torch.nn as nn


# 1.定义函数，手动实现：二维互相关（卷积）运算
def corr2d(X, K):           # X：输入；K：卷积核
    """计算二维互相关运算"""
    h, w = K.shape          # 获取卷积核K的高度和宽度
    Y = torch.zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))       # 初始化输出矩阵
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i : i + h, j : j + w] * K).sum()           # 互相关运算
    return Y


# 2.定义类，自定义二维卷积层
class Conv2D(nn.Module):
    def __init__(self, kernel_size):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(kernel_size))            # 生成偏置矩阵，即卷积核本身
        self.bias = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        return corr2d(x, self.weight) + self.bias


# 3.编写主函数
def main():
    # 3.1 测试基础卷积计算
    X = torch.tensor([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
    K = torch.tensor([[0.0, 1.0], [2.0, 3.0]])
    print("基础互相关运算结果：")
    print(corr2d(X, K))

    # 3.2 应用：图像垂直边缘检测
    X_edge = torch.ones((6, 8))
    X_edge[:, 2:  6] = 0
    print("边缘检测输入矩阵：")
    print(X_edge)
    K_edge = torch.tensor([[1.0, -1.0]])
    print("边缘检测卷积核：")
    print(K_edge)
    Y_edge = corr2d(X_edge, K_edge)
    print("边缘检测响应结果：")
    print( Y_edge)



# 4.测试
if __name__ == "__main__":
    main()