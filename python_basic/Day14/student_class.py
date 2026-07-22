"""
程序名称：student_class.py
作者：黄乐源
日期：2026-07-11
描述：掌握面向对象编程基础、类与对象实例化、self机制、魔术方法与类属性，构建空间建筑物矢量要素类
"""

print("================= 任务 1：类与对象基础、魔术方法与实例方法 =================")

class SpatialBuilding:
    """
    GeoAI 空间建筑物矢量要素类
    用于封装单个建筑物斑块的几何参数、属性数据及空间运算行为
    """

    # 类属性：被所有 SpatialBuilding 实例共享（华中师范大学城市与环境科学学院空间参考系坐标系统）
    crs_system: str = "EPSG:4326 (WGS84)"
    total_building_count: int = 0  # 类属性：用于累计全局创建的建筑物对象数量

    def __init__(self, building_id: str, footprint_area: float, height: float, is_active: bool = True):
        """
        魔术方法：构造函数，在对象实例化时被自动调用，用于初始化实例属性
        """
        # 实例属性
        self.building_id = building_id      # 建筑物唯一编号
        self.footprint_area = footprint_area        # 占地面积（平方米）
        self.height = height        # 建筑高度（米）
        self.is_active = is_active      # 是否参与分割计算

        # 每创建一个新实例对象，全局类属性计数器加 1
        SpatialBuilding.total_building_count += 1

    def calculate_volume(self) -> float:
        """
        实例方法：根据占地面积与高度，计算该建筑物的估算体量/体积(立方米)
        """
        # 通过 self 访问当前实例对象自身的属性
        volume = self.footprint_area * self.height
        return volume

    def update_footprint(self, new_area: float) -> None:
        """
        实例方法：修改当前建筑物的占地面积属性
        """
        print(f"[修改属性]建筑物{self.building_id}面积更新：{self.footprint_area}m² -> {new_area}m²")
        self.footprint_area = new_area

    def __str__(self) -> str:
        """
        魔术方法：定义对象的打印字符串表示，当使用 print(obj) 时自动触发调用
        """
        status_str = "激活" if self.is_active else "冻结"
        return f"<SpatialBuilding ID={self.building_id} | 面积={self.footprint_area:.1f}m² | 高度={self.height:.1f}m | 状态={status_str}>"

# 实例化第一个建筑物对象 (华师城环科学会堂)
b1 = SpatialBuilding("CCNU_Building_01", 1250.5, 24.0)

# 实例化第二个建筑物对象 (华师图书馆)
b2 = SpatialBuilding("CCNU_Building_02", 3800.0, 32.5, True)

# 打印对象，触发 __str__() 魔术方法
print("打印实例化后的建筑物对象：")
print(b1)
print(b2)

# 调用实例方法计算建筑物几何体量
v1 = b1.calculate_volume()
v2 = b2.calculate_volume()
print(f"建筑物{b1.building_id}估算总体积：{v1:.2f}m³")
print(f"建筑物{b2.building_id}估算总体积：{v2:.2f}m³")


print("\n================= 任务 2：类属性共享机制与实例属性修改操作 =================")

# 访问类属性（推荐使用类名直接访问，也可以使用实例对象访问）
print("华中师范大学城市与环境科学学院研究统一空间参考系：", SpatialBuilding.crs_system)
print("全局创建的建筑物对象数量：", SpatialBuilding.total_building_count)

# 通过实例方法修改属性
b1.update_footprint(1280.7)
print(f"修改后重新计算{b1.building_id}总体积：{b1.calculate_volume():.2f}m³")

print("\n🏁 Day14 面向对象类与对象定义、self机制及魔术方法实验成功交付！")