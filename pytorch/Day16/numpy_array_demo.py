"""
程序名称：numpy_array_demo.py
作者：黄乐源
日期：2026-07-13
描述：NumPy 数组基础操作、数据预处理与 PyTorch Tensor 相互转换实战，开启第二阶段深度学习入门
"""

# 导入所需的库
import numpy as np
import torch

print("================= 任务 1：NumPy 数组创建、属性查看与索引切片 =================")

# 1. 创建模拟遥感高程/像元数据的二维 ndarray
geo_data = np.array([
    [102.5, 105.0, 110.2],
    [98.0, 100.5, 104.8],
    [95.2, 97.1, 99.6]]
, dtype = np.float32)        # 创建一个二维的3行3列的数组

print(f"遥感数组内容：{geo_data}")
print("数组维度：",geo_data.ndim)    # 2
print("数组形状：",geo_data.shape)   # (3,3)
print("数组数据类型：",geo_data.dtype)     # float32

# 2. 数组索引与切片练习：提取右上角 2x2 子区域
sub_region = geo_data[0:2, 1:3]
print("提取右上角 2x2 子区域切片：")
print(sub_region)

# 3. 基础数值预处理：模拟缺失值替换与标准化处理
raw_val = np.array([10.0, 20.0, np.nan, 40.0], dtype = np.float32)      # 缺失部分数值的原始数据
print("原始数据包含缺失值：", raw_val)

# 使用均值填充 NaN 缺失值
nan_mask = np.isnan(raw_val)        # np.isnan()作用：判断数组中的每个元素是不是NaN。所以得到nan_mask =[False False True False]
mean_val = np.nanmean(raw_val)      # 计算非缺失值平均值，自动忽略NaN，只计算有效数据。这里就是(10 + 20 + 40) / 3 = 23.333333
raw_val[nan_mask] = mean_val        # raw_val[nan_mask]表示：找到所有True的位置。然后使用均值填充
print("通过均值插值填充后的数据：", raw_val)


print("\n================= 任务 2：PyTorch Tensor 创建与 NumPy 数组相互转换 =================")

# 1. 使用 torch.arange 与 torch.zeros 创建基础 Tensor
x_tensor = torch.arange(12, dtype=torch.float32).reshape((3, 4))
print("创建的Pytorch Tensor(3x4)：", x_tensor)
print("Tensor元素总数：", x_tensor.numel())
print("Tensor形状：", x_tensor.shape)

# 2. NumPy ndarray 转换为 PyTorch Tensor ---> torch.from_numpy()
np_array = np.ones((2,3), dtype = np.float32)
converted_tensor = torch.from_numpy(np_array)   # 从NumPy的ndarray转换为PyTorch的tensor
print("从NumPy ndarray数组转换为PyTorch Tensor张量：",converted_tensor)

# 3. PyTorch Tensor 转回 NumPy ndarray ---> converted_tensor.numpy()（converted_tensor是待转换tensor的名称）
back_to_ndarray = converted_tensor.numpy()
print("从PyTorch Tensor张量转换为NumPy ndarray数组：", back_to_ndarray)

# 4. 验证内存共享（修改原 NumPy 数组观察 Tensor 变化）
np_array[0, 0] = 99.0
print(f"修改原NumPy ndarray数组后，共享内存的PyTorch Tensor相应变为:{converted_tensor}")

print("\n🏁 Day16 NumPy 数组基础与 Tensor 互转测试完毕，第二阶段深度学习顺利启航！")