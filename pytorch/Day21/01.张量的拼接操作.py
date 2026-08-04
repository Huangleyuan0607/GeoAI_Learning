"""
案例：
    演示张量的拼接操作

涉及到的API：
    torch.cat():不改变维度数，拼接张量，除了拼接的那个维度外，其他维度数必须保持一致。
    torch.stack():会改变维度数，拼接张量，所有的维度都必须保持一致

需要你记忆的：
    cat()
"""

# 导包
import torch

# 设置随机种子
torch.manual_seed(24)

# 1.创建2个张量
t1 = torch.randint(1, 10 , (2, 3))
print("t1:", t1,"shape:", t1.shape)

t2 = torch.randint(1, 10 , (2, 3))
print("t2:", t2,"shape:", t2.shape)

# 2.演示张量的拼接
# 思路1：cat()函数拼接张量
# t3 = torch.cat([t1, t2], dim = 0)   # (2, 3) + (2, 3) = (4, 3)解释：除了拼接的那个维度外，其他维度数必须保持一致。此处指除了拼接的第0维外的（第1维）都为3。
# print("t3:", t3,"shape:", t3.shape)

# t4 = torch.cat([t1, t2], dim = 1)   # (2, 3) + (2, 6) = (2, 9)
# print("t4:", t4,"shape:", t4.shape)

# t5 = torch.cat([t1, t2], dim = -1)    # 效果同：torch.cat([t1, t2], dim = 1)
# print("t5:", t5,"shape:", t5.shape)

# t6 = torch.cat([t1, t2], dim = 2)       # 报错：越界 out of range
# print("t6:", t6,"shape:", t6.shape)

print("-" * 30)

# 思路2：stack()函数拼接张量，可以是新维度，但是无论新旧维度，所有维度都必须保持一致
t7 = torch.stack([t1, t2], dim = 0)     # (2, 3) + (2, 3) = (2, 2, 3)
print("t7:", t7,"shape:", t7.shape)

t8 = torch.stack([t1, t2], dim = 1)     # (2, 3) + (2, 3) = (2, 2, 3)
print("t8:", t8,"shape:", t8.shape)

t9 = torch.stack([t1, t2], dim = 2)     # (2, 3) + (2, 3) = (2, 3, 2)
print("t9:", t9,"shape:", t9.shape)

# t10 = torch.stack([t1, t2], dim = 3)     # 报错：越界 out of range
# print("t10:", t10,"shape:", t10.shape)

















