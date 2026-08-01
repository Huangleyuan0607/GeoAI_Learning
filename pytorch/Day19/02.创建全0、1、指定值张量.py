"""
案例：
    演示如何创建全0、1、指定值的张量

涉及到的函数如下：
    torch.ones 和 torch.ones_like(基于你的形状) 创建全1张量
    torch.zeros 和 torch.zeros_like(基于你的形状) 创建全0张量
    torch.full 和 torch.full_like(基于你的形状) 创建全为指定值张量

需要你掌握的函数：
    zeros(), full()
"""

# 导包
import torch

# 场景1：torch.ones 和 torch.ones_like(基于你的形状) 创建全1张量
t1 = torch.ones(2, 3)   # 创建2行3列全1张量
print(f"t1：{t1}, type:{type(t1)}")
print("-" * 30)

# t2：3行2列
t2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(f"t2：{t2}, type:{type(t2)}")

# t3 -> 基于t2的形状创建全1张量
t3 = torch.ones_like(t2)
print(f"t3：{t3}, type:{type(t3)}")
print("*" * 30)

# 场景2：torch.zeros 和 torch.zeros_like(基于你的形状) 创建全0张量
t1 = torch.zeros(2, 3)   # 创建2行3列全0张量
print(f"t1：{t1}, type:{type(t1)}")
print("-" * 30)

# t2：3行2列
t2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(f"t2：{t2}, type:{type(t2)}")

# t3 -> 基于t2的形状创建全0张量
t3 = torch.zeros_like(t2)
print(f"t3：{t3}, type:{type(t3)}")
print("*" * 30)

# 场景3：torch.full 和 torch.full_like(基于你的形状) 创建全为指定值张量
t1 = torch.full(size = (2, 3), fill_value = 255)   # 创建2行3列全255张量
print(f"t1：{t1}, type:{type(t1)}")
print("-" * 30)

# t2：3行2列
t2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(f"t2：{t2}, type:{type(t2)}")

# t3 -> 基于t2的形状创建全255张量     
t3 = torch.full_like(t2, 255)       # 题外话：RGB颜色通道的值为0~255，越接近0越黑，越接近255越白
print(f"t3：{t3}, type:{type(t3)}")











