# 面向对象基础
# 类与对象
# # 定义类 ---> 不推荐 动态地为对象添加属性
# class Car:      # 类名的命名规范：每个单词的首字母都是大写，单词之间没有分隔符
# 	pass
#
# # 创建对象
# c1 = Car()
# # 动态地为对象添加属性（不推荐！！！！会降低代码的可读性、可维护性，增加开发难度）
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "x5"
# c1.price = 500000
#
# print(c1)       # 输出：<__main__.Car object at 0x00000144DA818440>，其中at后的数字串表示的是对象的内存地址（每次输出都不相同）
# print(c1.__dict__)      # 将对象中的所有属性以字典的形式输出
# print(c1.brand)     # 获取对象中某一属性的值


# # 定义类 ---> 定义类时指定实例属性（推荐写法）
# class Car:
#     # __init__：初始化方法，对象创建后自动调用，主要用于设置对象的初始状态（ 设置对象属性）
#     # self是方法的第一个参数，表示当前创建的实例对象。
#     def  __init__ (self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕~")
#
# # 创建对象
# c1 = Car ("红色", "BMW","X7", 800000)
# print(c1.__dict__)
#
# c2 = Car("白色", "Benz", "E300", 450000)
# print(c2.__dict__)


# # 实例方法
# # 定义类
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕~")
#
#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶...")
#
#     def total_cost(self, discount, rate = 0.1):
#         """
#         计算提车的总费用，包含两个部分：车的价格，税费
#         :param discount:折扣
#         :param rate:税率
#         :return:提车的总费用
#         """
#         return self.price * discount + self.price * rate
#
# # 创建对象
# c1 = Car ("红色", "BMW","X7", 800000)
#
# # 调用类中方法 ---> self表示当前实例对象，方法调用时无需传递
# c1.running()
#
# total_cost1 = c1.total_cost(0.9, 0.1)
# print(f"提车总价为:{total_cost1:.1f}")
#
# total_cost2 = c1.total_cost(0.9)
# print(f"提车总价为:{total_cost2:.1f}")


# # 魔法方法
# class Car:
#     # 初始化方法 ---> 也是魔法方法
#     def __init__(self, color, brand, name, price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕~")
#
#     # 实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶...")
#
#     # 魔法方法
#     def __str__(self):      # 字符串表示的方法
#         return f"{self.brand} {self.name} {self.price}"
#
#     def __eq__(self, other):        # 基于属性比较两对象是否相等
#         return self.price == other.price and self.name == other.name and self.brand == other.brand and self.color == other.color
#
#     def __lt__(self, other):        # 支持比较两个对象的大小，这里是小于（less than）
#         return self.price < other.price
#
# # 测试
# c1 = Car ("白色", "BYD","汉",180000)
# print(c1)       # 默认输出出来的是对象的内存地址(16进制)，但添加__str__方法后，则会根据__str__方法的返回值输出结果
#
# c2 = Car ("白色", "BYD","汉",180001)
# print(c2)       # 默认输出出来的是对象的内存地址(16进制)，但添加__str__方法后，则会根据__str__方法的返回值输出结果
#
# print (c1 == c2)    # 默认是基于对象的内存地址进行比较，所以会输出False，但添加__eq__方法后，则会根据属性值比较，这里最终会输出True
#
# print(c1 < c2)      # 默认自定义的对象之间不可以进行大小比较，但添加__lt__方法后，则会根据属性值比较小于是否成立，这里最终会输出False


# 实例属性与类属性
class Car:
    # 类属性 ---> 所有实例对象共享
    wheel = 4       # 轮胎数量
    tax_rate = 0.1      # 购置税税率


    # 初始化方法 ---> 也是魔法方法
    def __init__(self, color, brand, name, price):
        # 实例属性
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price
        self.wheel = 2
        print("Car类型的对象初始化完毕，对象属性已经添加完毕~")

    # 实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶...")

    # 魔法方法
    def __str__(self):      # 字符串表示的方法
        return f"{self.brand} {self.name} {self.price}"

    def __eq__(self, other):        # 基于属性比较两对象是否相等
        return self.price == other.price and self.name == other.name and self.brand == other.brand and self.color == other.color

    def __lt__(self, other):        # 支持比较两个对象的大小，这里是小于（less than）
        return self.price < other.price

# 测试
c1 = Car ("白色", "BYD","汉",180000)
print(c1)
print(c1.brand)
print(c1.wheel)     # 通过实例对象查找属性时，会先查找实例属性；实例属性不存在，再查找类属性

# 通过类名访问类属性
print(Car.wheel)
print(Car.tax_rate)


# c2 = Car ("白色", "BYD","汉",180001)
# print(c2)


























