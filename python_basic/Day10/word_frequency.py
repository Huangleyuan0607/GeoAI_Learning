"""
程序名称：word_frequency.py
作者：黄乐源
日期：2026-07-07
描述：攻克集合高效去重与交并差运算，掌握字典的键值映射与嵌套提取，模拟多源地物标签分析
"""

print("================= 任务 1：集合（Set）的去重与空间拓扑关系运算 =================")
# 模拟从两个不同分类模型中提取出的遥感地物覆盖分类标签列表（存在大量重复与杂质）
model_a_labels = ["building", "water", "building", "vegetation", "road", "barren"]
model_b_labels = ["vegetation", "road", "vegetation", "cropland", "shadow", "water"]

print(f"模型A提取的原始标签：{model_a_labels}")
print(f"模型B提取的原始标签：{model_b_labels}")

# 1. 利用集合天然去重的特性
set_a = set(model_a_labels)     # 利用集合去重特性去除重复元素
set_b = set(model_b_labels)
print(f"模型A提取的原始唯一标签：{set_a}")
print(f"模型B提取的原始唯一标签：{set_b}")

# 2. 集合运算：并集（求两个模型一共捕获了多少种地物类别）
# all_set = set_a.union(set_b)
all_set = set_a & set_b
print(f"两个模型总共提取的地物类别：{all_set}")

# 3. 集合运算：交集（求两个模型达成共识的地物类别）
# inter_set = set_a.intersection(set_b)
inter_set = set_a | set_b
print(f"两个模型均提取到的地物类别：{inter_set}")

# 4. 集合运算：差集（求模型 A 独有而模型 B 没有检测到的地物类别）
# diff_set = set_a.difference(set_b)
diff_set = set_a - set_b
print(f"模型A独有而模型B没有检测到的地物类别：{diff_set}")

print("\n================= 任务 2：字典（Dict）键值映射与要素检索 =================")
# 模拟一个典型的 GIS 矢量建筑物要素（GeoJSON Properties）属性映射
building_feature = {
    "feature_id": 1024,
    "class_name": "building",
    "area_m2": 458.5,
    "height_m": 18.5,
    "coords_wgs84": (114.3721, 30.5312)  # 使用 Day09 学过的元组锁死坐标
}
print(f"原始建筑物要素字典: {building_feature}")

# 1. 字典的访问 (Key 访问)
print(f"要素ID：{building_feature['feature_id']}, 地物类别：{building_feature['class_name']}")

# 2. 字典的修改与添加新键值对
building_feature["feature_id"] = 1025
building_feature["class_name"] = "water"
building_feature["area_m2"] = 529.8
building_feature["height_m"] = 19.2
# building_feature["coords_wgs84"] = (117.5521, 31.0021)    `# 注意：元组不可修改！！！！
building_feature["color"] = "绿色"        # 添加新键值对

print(f"更新后的要素字典: {building_feature}")

# 3. 字典的成员判断与安全获取（防止因 Key 不存在导致报错崩溃）
# 推荐在处理脏数据时使用 get() 方法
sensor_type = building_feature.get("sensor", "未知传感器")
print(f"安全属性查询 -> 传感器源: {sensor_type}")

print("\n================= 任务 3：多案例融合终极实战（多属性嵌套数据综合审计系统） =================")
# 模拟华中师范大学城市与环境科学学院 GeoAI 课题组对不同遥感地物斑块的高级统计结构
geo_database = {
    "BLOCK_01": {"class": "building", "area": 1250.2, "confidence": 0.942, "is_active": True},
    "BLOCK_02": {"class": "water", "area": 8450.0, "confidence": 0.985, "is_active": True},
    "BLOCK_03": {"class": "building", "area": 310.4, "confidence": 0.721, "is_active": False},
    "BLOCK_04": {"class": "vegetation", "area": 15600.8, "confidence": 0.891, "is_active": True}
}

print("📊 待分析的多源嵌套地物特征属性数据库：")
for block_id, block_data in geo_database.items():
    print(f"斑块: {block_id} -> {block_data}")

print("\n--- 🔎 筛选出置信度(confidence) > 0.85 且处于激活状态(is_active) 的建筑物或水体斑块 ---")
for block_id, block_data in geo_database.items():
    class_value = block_data["class"]
    area_value = float(block_data["area"])
    confidence_value = float(block_data["confidence"])
    is_active_value = block_data["is_active"]
    if confidence_value > 0.85 and is_active_value == True:
        print(f"筛选通过！斑块编号：{block_id}，地物类别：{class_value}，置信度：{confidence_value}")

print("\n🏁 Day10 集合去重与字典映射安全系统成功建立，准备进行版本控制！")