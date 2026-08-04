"""
案例：
    演示张量的自动微分模块，具体如何求导

回顾：
    权重更新公式：
        W新 = W旧 - 学习率 * 梯度

        梯度 = 损失函数的导数

    关于损失函数的导数，无需我们手动计算，因为非常常用，所以PyTorch模块内置有自动微分模块，专门实现针对于不同的损失函数求导，从而实现结合反向传播，更新权重参数W和偏置参数b

细节：
    只有标量张量才能求导，且大多数底层操作的都是浮点型，记得转型

"""

# 导包
import torch

# 1.定义变量，记录：初始权重w(旧)
# 参1：初始值，参2：是否自动微分（求导），参3：数据类型
w = torch.tensor(10, requires_grad = True, dtype = torch.float)

# 2.定义loss变量，表示损失函数
loss = 2 * w ** 2       # loss = 2w² -> 求导：4w

# 3.打印梯度函数类型（了解）
print("梯度函数类型：", type(loss.grad_fn))    # <class 'MulBackward0'>
print(loss.sum())

# 4.计算梯度 = 损失函数的导数，计算完毕后，会记录到w.grad属性中
# loss.sum().backward()       # 保证loss是一个标量（一个数）
loss.backward()     # 这里因为y本身就是标量，可以不写sum()

# 5.带入权重更新公式：W新 = W旧 - 学习率 * 梯度
w.data = w.data - 0.01 * w.grad     # w新 = 10 - 0.01 * 40 = 10 - 0.4 = 9.6

# 6.打印最终结果
print(f"更新后的权重:{w.data}")








