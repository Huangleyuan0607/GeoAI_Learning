"""
程序名称：tensor_create.py
作者：黄乐源
日期：2026-07-15
描述：PyTorch 框架基础与 Tensor 基本创建方式实战（结合 GeoAI 遥感/GIS 背景）
"""

# 导入包
import torch

print("================= 任务 1：GeoAI 遥感像素与栅格数据 Tensor 创建 =================")

# 1. 单波段遥感像素点/高程点 (一维张量)
# 模拟一条采样点的高程值 (DEM, 单位: 米)
dem_values = torch.tensor([120.5, 135.0, 128.2, 140.8])
print(f"1维DEM采样高程张量:\n{dem_values}")

# 2. 指定地理数据常用的数据类型 (float32 / int64)
# 模拟 3x3 单波段遥感图像灰度值 (0~255)
landsat_band = torch.tensor([
    [102, 115, 120],
    [98,  110, 125],
    [105, 118, 130]
], dtype=torch.float32)
print(f"2维单波段遥感栅格张量(float32):\n{landsat_band}")

# 3. 模拟多光谱/多波段遥感数据片段 (三维张量: 波段 x 高 x 宽)
# 例如 2 个波段 (红外/近红外), 每个波段 2x2 像素
multispectral_patch = torch.tensor([
    [[10, 20], [30, 40]],  # Red 波段
    [[50, 60], [70, 80]]   # NIR 波段
])
print(f"3维多光谱遥感Patch张量(Bands x H x W):\n{multispectral_patch}")

print("\n🏁 Day18 GeoAI PyTorch 框架与 Tensor 基本创建实战完成！")