"""
程序名称：numpy_linear_algebra.py
作者：黄乐源
日期：2026-07-14
描述：NumPy 矩阵运算、广播机制、向量点积、矩阵乘法与范数计算实战
"""

# 导入numpy包和pytorch包
import numpy as np
import torch

import pytorch

print("================= 任务 1：数据类型转换与等差/等比数列创建 =================")

# 1. 类型转换 astype
arr1 = np.array([1.2, 2.8, 3.5],dtype= np.float32)      # 原浮点数组
arr2 = arr1.astype(np.int32)    # 转为整数数组（向下取整）
print(f"原浮点数组：{arr1} -> 现整数数组：{arr2}")

# 2. 创建等差与等比数列
arr3 = np.linspace(0, 10, 5)    # 创建等差数列数组，从0到10生成5个等差数（包左包右）
arr4 = np.logspace(0, 2, 3)     # 创建等比数列数组，注意：这里的开始值和起始值都是10的幂指数，即从10^0到10^2生成3个等比数
print(f"等差数列：{arr3}")
print(f"等比数列：{arr4}")


print("\n================= 任务 2：广播计算与按轴求和 =================")

# 1. 广播机制演示 ---> 当两个形状不同的数组进行逐元素运算时，torch会自动在长度为 1 的维度上进行隐式扩展，从而避免不必要的内存复制。
a = torch.arange(3).reshape(3, 1)    # 3行1列
b = torch.arange(4).reshape(1, 4)    # 1行4列
broadcast_sum = a + b
print("列向量a(3x1) + 行向量b(1x4)广播相加结果(3x4)：\n", broadcast_sum)

# 2. 按特定轴求和
X = torch.tensor([[1, 2 ,3], [4, 5, 6]], dtype=torch.float32)
print(f"原始矩阵：\n", X)
print(f"按axis = 0求和：\n", X.sum(axis = 0))
print(f"按axis = 1且保持维度求和：\n", X.sum(axis = 1, keepdim = True))


print("\n================= 任务 3：向量点积、矩阵乘法与范数计算 =================")

# 1. 向量点积 (Dot Product)
u = torch.tensor([1.0, 2.0, 3.0])
v = torch.tensor([4.0, 5.0, 6.0])
dot_product = torch.dot(u, v)
print("向量u和v的点积：", dot_product)

# 2. 矩阵乘法（行列数不相同）
A = torch.tensor([[1, 2], [3, 4], [5, 6]])
B = torch.tensor([[7, 8, 9], [10, 11, 12]])
C = torch.mm(A, B)      # 同C = A @ B
print("向量A(3x2) @ 向量B(2x3)结果：\n", C)

# 3. 范数计算
l2_norm = torch.norm(u)
print(u)
print("向量u的L2范数（模长）：", l2_norm)

print("\n🏁 Day17 NumPy 矩阵计算与线性代数实战完成！")