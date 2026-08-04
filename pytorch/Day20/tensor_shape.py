"""
程序名称：tensor_shape.py
作者：黄乐源
日期：2026-07-17
描述：PyTorch Tensor 基础运算、索引切片与维度变换实战（结合 GeoAI 遥感/GIS 维度转换背景）
"""

# 导包
import torch

print("================= 任务 1：Tensor 基础运算与矩阵乘法 =================")

# 1. 逐元素运算
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
print(f"逐元素相加：", a + b)
# print(f"逐元素相加：", a.add(b))    # 效果同上
print(f"逐元素相减：", a - b)
# print(f"逐元素相加：", a.sub(b))    # 效果同上
print(f"逐元素相乘：", a * b)
# print(f"逐元素相乘：", a.mul(b))    # 效果同上
print(f"逐元素相除：", a / b)
# print(f"逐元素相除：", a.div(b))    # 效果同上

# 2. 矩阵乘法 (matmul / @)
print("矩阵乘法结果：", a @ b)
print("矩阵乘法结果：", torch.matmul(a, b))

# 3. 统计运算 (如计算多光谱波段均值)
spectral_data = torch.tensor([[120, 150, 200], [80, 90, 110]], dtype=torch.float)
print("按列求波段均值：", spectral_data.mean(dim = 0))      # dim = 0表示按列，dim = 1表示按行
print("按行求波段均值：", spectral_data.mean(dim = 1))      # dim = 0表示按列，dim = 1表示按行

print("\n================= 任务 2：Tensor 索引与切片操作 =================")

# 模拟单波段 4x4 遥感栅格高程/DN值
raster = torch.tensor([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
])

# 切片获取中间 2x2 ROI 区域
roi = raster[1:3, 1:3]
print("提取中间2x2 ROI区域数据：", roi)

# 布尔掩码提取 (提取高程大于 35 的所有样点)
mask = raster > 35
print("提取高程大于 35 的掩码矩阵：", mask)     # 结果为一个布尔矩阵
print("符合条件的样点值：", raster[mask])

print("\n================= 任务 3：维度变换（Reshape, Squeeze, Permute）=================")

# 1. 模拟 GDAL/OpenCV 读取的多光谱遥感影像: Height=256, Width=256, Channels=4 (RGB+NIR)
rs_img = torch.randn(256, 256, 4)       # 随机生成正态分布的张量(256, 256, 4)
print("原始遥感影像形状（H x W x C）：", rs_img.shape)     # (256, 256, 4)

# 2. 将 H x W x C 转换为 PyTorch CNN 所需的 C x H x W
rs_img_chw = rs_img.permute(2, 0, 1)
print("经permute函数转换后的形状：", rs_img_chw.shape)    # (4, 256, 256)

# 3. 增加 Batch 维度，供深度学习网络输入 (1 x C x H x W)
input_tensor = rs_img_chw.unsqueeze(0)      # 在第0维新增维度
print("经unsqueeze函数增加Batch维度后形状", input_tensor.shape)       # (1, 4 ,256, 256)

# 4. 模拟网络输出，降维 (Squeeze)
output_tensor = input_tensor.squeeze()
print("经squeeze函数挤压Batch维度后形状：", output_tensor.shape)       # (4, 256, 256)

# 5. Reshape 与 Contiguous / View 试验
flat_features = rs_img_chw.reshape(4, -1)       # 展开空间维度，这里的-1表示：让Python根据数组的总元素个数和已知维度（这里是4），自动计算出另一个维度应该是多少。
print("展平空间维度后的形状 (C x H*W):", flat_features.shape)         # (4, 256*256)

# 验证 non-contiguous 内存转换
premuted_t = rs_img.permute(2, 0, 1)
print("permute后内存是否连续？", premuted_t.is_contiguous())        # False
contiguous_t = premuted_t.contiguous()
print("contiguous后内存是否连续？", contiguous_t.is_contiguous())   # True

print("\n🏁 Day20 GeoAI Tensor 运算与维度变换实战完成！")