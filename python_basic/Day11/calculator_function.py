"""
程序名称：calculator_function.py
作者：黄乐源
日期：2026-07-08
描述：掌握函数的定义、多参数传递、多返回值及函数嵌套，模拟 GeoAI 要素空间审计与中心解析
"""

print("================= 任务 1：函数定义、参数交互与多返回值系统 =================")

def calculate_centroid_and_area(min_x, min_y, max_x, max_y):
    """
    计算标准建筑物外接矩形(Bounding Box)的几何中心坐标与估算面积

    参数:
    min_x (float): 左下角西经/东经经度坐标
    min_y (float): 左下角南纬/北纬纬度坐标
    max_x (float): 右上角西经/东经经度坐标
    max_y (float): 右上角南纬/北纬纬度坐标

    返回:
    tuple: 包含三个元素的元组 (center_x, center_y, estimated_area)
           - center_x (float): 中心点经度
           - center_y (float): 中心点纬度
           - estimated_area (float): 估算平面面积 (以度为单位的简化模拟计算)
    """
    # 逻辑计算：中心点为两端点的均值
    center_x = (max_x + min_x) / 2
    center_y = (max_y + min_y) / 2

    # 面积计算：宽 * 高
    width = max_x - min_x
    height = max_y - min_y
    estimated_area = width * height

    # 返回多重数据（Python 会自动自动组包为元组）
    return center_x, center_y, round(estimated_area, 2)     # 将面积保留2位小数

# 模拟华师城环学院课题组捕获的某栋新型建筑物矢量边界拓扑参数
b_min_x, b_min_y = 114.3700, 30.5300
b_max_x, b_max_y = 114.3750, 30.5340

print(f"📡 输入建筑物边界: Min({b_min_x}, {b_min_y}) -> Max({b_max_x}, {b_max_y})")

# 调用函数并执行多返回值解包
c_x, c_y, e_a = calculate_centroid_and_area(b_min_x, b_min_y, b_max_x, b_max_y)
print(f"解析成功！中心经度：{c_x}，中心纬度：{c_y}，模拟图层面积：{e_a}")

# 利用 Python 内置 help() 查看我们手工编写的专业函数说明文档
print("打印自定义函数的系统说明文档：")
print(help(calculate_centroid_and_area))

print("\n================= 任务 2：GeoAI 多级函数嵌套调用与深度特征防御审计 =================")


def check_confidence_safety(confidence):
    """底层防御级子函数：校验遥感标签置信度是否达标"""
    if confidence >= 0.85:      # 当置信度大于0.85时视为达标
        return True
    else:
        return False

def audit_geo_feature(block_id, feature_dict):
    """
    中层审计级核心函数：嵌套调用置信度检查函数，并对输入要素进行全方位解构说明
    """
    # 提取字典中的核心属性（使用 Day10 学过的安全机制 get()）
    f_class = feature_dict["class"]
    f_confidence = feature_dict["confidence"]

    # 嵌套调用第一层底层子函数检查置信度是否达标
    is_safe = check_confidence_safety(f_confidence)

    # 根据子函数的布尔返回值，处理本层核心业务逻辑
    if is_safe and f_class == "building":
        safe_report = f"要素安全通过：确认高置信度建筑物要素，准予送入 U-Net 模型进行分割。"
    elif is_safe:
        safe_report = f"要素暂缓：虽置信度达标({f_confidence})，但类别为 [{f_class}]，非主攻建筑物目标。"
    else:
        safe_report = f"威胁拦截：要素置信度({f_confidence})过低，判定为噪点脏数据，拒绝入库！"

    return safe_report

# 模拟课题组待批量清洗处理的 GeoJSON Properties 斑块数据集
mock_tiles = {
    "GEO_PATCH_001": {"class": "building", "confidence": 0.94},
    "GEO_PATCH_002": {"class": "water", "confidence": 0.88},
    "GEO_PATCH_003": {"class": "building", "confidence": 0.62}
}

print("📊 启动多层嵌套函数处理流水线 Pipeline：")
for p_name, p_dict in mock_tiles.items():
    # 执行审计主函数
    report = audit_geo_feature(p_name, p_dict)
    print(f"审计报告 -> {report}\n")

print("🏁 Day11 函数模块化封装与多级调用测试成功，数据流走向非常清晰！")