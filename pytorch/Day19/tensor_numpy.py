"""
程序名称：tensor_numpy.py
作者：黄乐源
日期：2026-07-16
描述：PyTorch Tensor 常用创建进阶、数据类型转换与 NumPy 双向转换实战（结合 GeoAI 遥感/GIS 背景）
"""
# 导包
import numpy as np
import torch

print("================= 任务 1：指定值、线性与随机 Tensor 创建 =================")

# 1. 创建全 0 掩码矩阵 (如遥感图像背景 Mask)
mask_zeros = torch.zeros((3, 3), dtype = torch.uint8)       # 数据类型为8位无符号整型
print("3x3全0掩码张量:", mask_zeros)

# 2. 创建特定初始值的张量 (如初始化偏置项或特定高程填充)
padding_tensor = torch.full(size = (2, 4), fill_value = -9999.0)
print("指定填充值(-9999.0)张量:", padding_tensor)

# 3. 线性等差序列 (如波段波长采样点或时间序列索引)
wavelengths = torch.linspace(400, 900 ,6)
print("400nm - 900nm线性采样波段序列:", wavelengths)

# 4. 正态分布随机数 (模拟遥感影像传感器高斯噪声或权重初始化)
gaussian_noise = torch.randn((2, 3))
print("标准正态分布随机噪声张量:", gaussian_noise)

print("\n================= 任务 2：Tensor 数据类型（Dtype）转换 =================")

# 模拟原始 8 位无符号整型遥感单波段数据 (0-255)
raw_raster = torch.tensor([[50, 120, 200], [80, 150, 220]], dtype = torch.uint8)    # 数据类型为8位无符号整型
print("原始unit8栅格张量类型：", raw_raster)

# 归一化输入前需转换为 float32 浮点型
float_raster = raw_raster.type(torch.float32)
# float_raster = raw_raster.float()     # 这种写法也可以

print("转换并归一化后的float32栅格张量：", float_raster)
print("新张量数据类型：", float_raster.dtype)

print("\n================= 任务 3：Tensor 与 NumPy 数组互转及内存共享校验 =================")

# 1. NumPy Array -> PyTorch Tensor
np_array = np.array([101.5, 102.8, 104.3], dtype = np.float32)
tensor_from_np1 = torch.from_numpy(np_array)     # 共享内存
tensor_from_np2 = torch.tensor(np_array)     # 不共享内存
print("从Numpy数组转换得到的Tensor（共享内存）：", tensor_from_np1)
print("从Numpy数组转换得到的Tensor（不共享内存）：", tensor_from_np2)

# 2. PyTorch Tensor -> NumPy Array
tensor_data = torch.ones((2, 2), dtype = torch.float32)
np_from_tensor1 = tensor_data.numpy()    # 共享内存
np_from_tensor2 = tensor_data.numpy().copy()    # 不共享内存
print("从Tensor转换得到的Numpy数组（共享内存）：", np_from_tensor1)
print("从Tensor转换得到的Numpy数组（不共享内存）：", np_from_tensor2)

# 3. 验证内存共享特性
np_array[0] = 999.0
print("修改后的Numpy数组结果：", np_array)
print("（torch.from_numpy(np_array)方法 -> 共享内存）Tensor同步更新结果：", tensor_from_np1)
print("（torch.tensor(np_array)方法 -> 不共享内存）Tensor同步更新结果：", tensor_from_np2)

print("\n🏁 Day19 GeoAI Tensor 进阶创建与 NumPy 互转实战完成！")