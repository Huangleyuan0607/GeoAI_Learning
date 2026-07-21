"""
程序名称：main_pipeline.py
作者：黄乐源
日期：2026-07-10
描述：GeoAI 生产流水线主程序，跨目录导入自定义 utils 工具包并执行强类型安全审计
"""

# 跨目录安全导入自定义工具包内的 geo_math 模块
from utils import geo_math

print("================= 任务 1：跨模块调用与强类型注解防御审计 =================")

# 显式使用强类型注解定义一组待审计的多源遥感影像元数据字典
# 这可以防止后期被师兄或后续脚本注入错误的列表或字符串
target_patch_info: dict = {
    "patch_id": "华师城环科学会堂_B1",
    "total_polygon_area": 4096.0,
    "pyramid_max_level": 4
}

# 提取关键参数，并使用静态类型提示绑定
area_val: float = target_patch_info["total_polygon_area"]
level_val: int = target_patch_info["pyramid_max_level"]

print(f"主流水线成功加载要素：{target_patch_info["patch_id"]}")
print("启动多尺度空间特征金字塔自适应递归解算机制...")

# 调用跨包模块内的递归函数（执行栈在内存中层层压入）
final_leaf_area = geo_math.resolve_spatial_pyramid(area_val, level_val)

print("\n-- 华中师范大学城市与环境科学学院GeoAI空间金字塔审计汇报 --")
print(f"1、原始宏观地物多边形总面积：{area_val:.2f}平方米")
print(f"2、金字塔最大向下剖分深度：{level_val}层")
print(f"3、送入深度学习前单切片（leaf Tile）基准控制面积：{final_leaf_area:.4f}平方米")

print("\n🏁 Day13 递归自组织算法与模块化工程包开发全面交付，版本控制准备就绪！")