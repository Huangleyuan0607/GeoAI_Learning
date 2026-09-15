# 导包
import torch
import torch.nn as nn


# 1.定义函数，实现：多输入通道互相关运算
def corr2d_multi_in(X, K):
    return sum(corr2d(x, k) for x, k in zip(X, K))

# 2.定义函数，编写：二维互相关基础函数
def corr2d(X, K):
    h, w = K.shape
    Y = torch.zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))       # (x_h - h + 1, x_w - w + 1)
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i : i + h, j : j + w] * K).sum()
    return Y

# 3.定义函数，实现：多输入通道、多输出通道互相关运算
def corr2d_multi_in_out(X, K):
    # K的形状为(c_out, c_in, h, w)
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)

# 4.定义主函数
def main():
    print("=== 1.使用PyTorch官方nn.Conv2d校验Padding与Stride ===")
    # 输入形状：(batch_size, in_channels, height, width)
    x_tensor = torch.randn(1, 1, 8, 8)

    # 验证Padding = 1，Stride = 1
    conv_p1_s1 = nn.Conv2d(in_channels = 1, out_channels = 1, kernel_size = 3, stride = 1, padding = 1)
    out_p1_s1 = conv_p1_s1(x_tensor)
    print("nn.Conv2d输出形状（Padding = 1, Stride = 1）：", out_p1_s1.shape)       # 8 - 3 + 1x2 + 1 = 8

    # 验证Padding = 1，Stride = 2（下采样）
    conv_p1_s2 = nn.Conv2d(in_channels = 1, out_channels = 1, kernel_size = 3, stride = 2, padding = 1)
    out_p1_s2 = conv_p1_s2(x_tensor)
    print("nn.Conv2d输出形状（Padding = 1, Stride = 2）：", out_p1_s2.shape)       # (8 - 3 + 2 + 1) / 2 = 4
    print()

    print("=== 2.多输入通道互相关运算 ===")
    X_multi = torch.tensor([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
                            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]])
    K_multi = torch.tensor([[[0.0, 1.0], [2.0, 3.0]],
                            [[1.0, 2.0], [3.0, 4.0]]])
    print("输入Shape(c_in, h_in, w_in)：", X_multi.shape)
    print("卷积核Shape(c_in, h_in, w_in)：", K_multi.shape)
    print("双通道互相关运算结果：")
    print(corr2d_multi_in(X_multi, K_multi))
    print()

    print("=== 3.多输出通道（多卷积核）运算 ===")
    # 构造3个不同的卷积核形成3个输出通道
    K_multi_out = torch.stack((K_multi, K_multi + 1, K_multi + 2), 0)
    print("输入Shape(c_in, h_in, w_in)：", X_multi.shape)
    print("卷积核Shape(c_out, c_in, h_in, w_in)：", K_multi_out.shape)
    out_multi_channel = corr2d_multi_in_out(X_multi, K_multi_out)
    print("多通道输出Shape(c_out, h_out, w_out)：", out_multi_channel.shape)      # 3 - 2 + 1 = 2

# 5.测试
if __name__ == "__main__":
    main()









