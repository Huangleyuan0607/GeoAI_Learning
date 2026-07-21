"""
模块名称：geo_math.py
作者：黄乐源
日期：2026-07-10
描述：自定义 GeoAI 工具箱数学模块，包含基于类型注解的多尺度空间递归斑块解算算子
"""

# 定义模块对外暴露的合法函数白名单
__all__ = ['resolve_spatial_pyramid']

def resolve_spatial_pyramid(current_area: float, zoom_level: int) -> float:
    """
    递归函数：模拟高分辨率遥感多尺度空间要素金字塔向下剖分计算
    将大面积斑块层层按四叉树递归降维，直到达到基础解译级别，计算最终叶子斑块的基准面积值
    类型注解说明:
    current_area (float): 当前空间斑块的总平面面积
    zoom_level (int): 当前金字塔所在的缩放层级 (层级递减)
    返回 -> float: 最终最底层解译单元的基准几何面积
    """

    # 1. 递归基 (Base Case)：触及塔底或解译极限分辨率层级，停止递去，开启归来
    if zoom_level <= 1:
        print(f"触及递归基！层级Level1：成功锁死底层叶子斑块基准面积：{current_area:.2f}平方米")
        return current_area

    # 2. 递归单层核心逻辑：层层拆解。模拟当前网格四等分，斑块面积变为当前的 1/4
    sub_patch_area =current_area / 4.0
    print(f"向下递去~层级 Level {zoom_level} -> 剖分为 Level {zoom_level - 1} | 当前分块面积：{sub_patch_area:.2f}平方米")

    # 3. 递归调用自身：将缩小的面积和递减的层级再次压入执行栈
    return resolve_spatial_pyramid(sub_patch_area, zoom_level - 1)

# 本地模块独立防污染自测闸门
if __name__ == '__main__':
    print("========== 模块局部自测启动 ==========")
    test_area: float = 1600.0
    test_level: int = 3
    print(f"开始测试递归解算，输入总面积：{test_area}，剖分层级：{test_level}")
    result = resolve_spatial_pyramid(test_area, test_level)
    print(f"自测圆满通过！最底层斑块面积：{result}平方米")