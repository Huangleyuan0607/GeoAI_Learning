"""
程序名称：student_management.py
作者：黄乐源
日期：2026-07-12
描述：面向对象空间要素管理系统与异常处理机制实战，完成 Python 基础阶段收官交付
"""

print("================= 任务 1：面向对象空间要素(Building)增删改查管理系统 =================")


# 地理空间要素数据实体类
class GeoFeature:
    def __init__(self, feature_id: str, feature_type: str, area: float):
        self.feature_id:str = feature_id
        self.feature_type:str = feature_type
        self.area:float = area

    # 返回字符串
    def __str__(self):
        return f"要素ID：{self.feature_id} | 要素类型：{self.feature_type} | 要素面积：{self.area:.2f}"

# 空间要素业务管理类：负责CRUD维护
class GeoFeatureManager:
    # 类要素
    system_name = "华中师范大学城环学院GeoAI研究要素管理系统"
    system_version = "1.0.0"

    def __init__(self):
        self.features_list:list[GeoFeature] = []        # 存储GeoFeature对象的列表

    # 添加要素
    def add_feature(self):
        feature_id = input("请输入要素ID：")

        # 检查输入的要素ID是否已经存在于数据库中
        for f in self.features_list:
            if f.feature_id == feature_id:
                print("该要素信息已经存在，添加失败！")
                return

        feature_name = input("请输入要素名称：")
        area = float(input("请输入要素面积："))

        # 判断面积是否大于0
        if area > 0:
            feature = GeoFeature(feature_id, feature_name, area)
            self.features_list.append(feature)
            print(f"成功添加要素：{feature.feature_id}")
        else:
            print("要素面积必须大于0！")

    # 查询全部要素
    def query_all(self):
        print()
        print("---华中师范大学城环学院GeoAI要素数据库清单---")

        # 检查当前数据库是否为空
        if not self.features_list:
            print("数据库当前为空！")
            return

        # 若数据库不为空，则执行查询操作
        for f in self.features_list:
            print(f)    # 这里打印f会调用GeoFeature类中的__str__方法

    # 启动菜单
    def run(self):
        print(f"### 欢迎使用{GeoFeatureManager.system_name} V{GeoFeatureManager.system_version} ###")

        while True:
            print()
            print("#############################################################################")
            print("#                     1、添加要素   2、查询要素   3、退出系统                     #")
            print("#############################################################################")

            choice = int(input("请选择要执行的操作(1-6)："))
            try:
                match choice:
                    case 1:     # 添加要素
                        self.add_feature()
                    case 2:     # 查询要素
                        self.query_all()
                    case 3:     # 退出系统
                        print(f"欢迎下次使用{GeoFeatureManager.system_name}~")
                        break
                    case _:     # 其他情况
                        print("输入错误，请选择1-6之间的菜单功能！")
            except ValueError:
                print("输入的数据有问题，请检查后重新输入！")
            except Exception:
                print("程序运行出错了，请重新选择！")

# 测试：实例化管理器并录入初始数据
if __name__ == "__main__":
    geo_feature_manager = GeoFeatureManager()
    geo_feature_manager.run()


print("\n================= 任务 2：脏数据输入与异常处理(try...except...else...finally)防御 =================")


def parse_remote_sensing_scale(raw_input: str):
    """
    解析用户输入的遥感分辨率比例尺，演示严谨的异常处理装甲
    """
    print(f"正在尝试解析原始分辨率参数字符串：{raw_input}")
    try:
        # 尝试转换为浮点数，若输入非数字字符（如 "invalid"）会引发 ValueError
        scale = float(raw_input)

        # 若数值非法，手动触发 ZeroDivisionError 或 ValueError
        if scale <= 0:
            raise ValueError("分辨率比例尺必须严格大于0！")

        calculated_resolution = 1.0 / scale

    except ValueError as v:
        # 捕获数值转换错误或手动抛出的异常
        print(f"捕获异常！转换失败或参数越界，错误信息：{v}")
        return
    except ZeroDivisionError as z:
        # 捕获除零异常
        print(f"捕获异常！比例尺不能为0，无法计算分辨率！错误信息：{z}")
        return
    except Exception as e:
        # 兜底捕获未知的其他所有异常
        print(f"未知异常！发生未知运行时错误，错误信息：{e}")
        return

    else:
        # 只有在 try 块代码完全正常、没有发生任何异常时才会执行
        print(f"解析成功！算子运行正常，计算得出地面实际分辨率: {calculated_resolution:.4f}米/像素")
        return calculated_resolution
    finally:
        # 无论是否发生异常都会执行的资源清理/日志收尾工作
        print("系统日志：本次分辨率参数解析审计完毕，释放通道资源~")

# 测试 1：正常输入合法数据
res1 = parse_remote_sensing_scale("0.5")

# 测试 2：输入包含非法字母的脏数据
res2 = parse_remote_sensing_scale("invalid_30m")

# 测试 3：输入非法的零值
res3 = parse_remote_sensing_scale("0")

print("\n🏁 Day15 综合要素管理与异常防爆系统测试完毕，第一阶段 Python 基础圆满收官！")