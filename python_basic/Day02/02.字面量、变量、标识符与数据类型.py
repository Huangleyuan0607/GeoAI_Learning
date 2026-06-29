# 字面量的写法
# print(100)  # 整数(int)
# print(3.14) # 浮点数/小数(float)
# print(True) # 布尔值(bool)
# print(False)    # 布尔值(bool)
# print("Hello GeoAI")    # 字符串(str) 需要用双引号引起来
# print("---------------------")  # 字符串(str)
# print(None) # 空值(NoneType)
from types import NoneType

# 布尔值本身也是整数类型 (True=1 False=0)
# print(True+1)   # 即等于1+1=2
# print(False-1)  # 即等于0-1=-1

# 变量的写法 --->Python是动态类型语言，变量类型可以在程序运行过程中改变，即一个变量可以接受不同类型的值(但在项目开发中推荐只存储一种变量类型)
# num = 1114.1
# print(num)
#
# num += 1    # 即等于num = num + 1
# print(num)
#
# num = "OK"
# print(num)

# 案例：计算播放量
# basic = 20.7
# increase = 50
# total = basic + increase
# print("未来第一个月播放总量为：",total)
# print("未来第一个月播放总量为：",basic+increase)
# total += increase
# print("未来第二个月播放总量为：",total)
# print("未来第二个月播放总量为：",basic+increase*2)
# print("---------------------------------------")

# 案例 - 升级：一次性定义多个变量
# basic, increase = 20.7, 50
# total = basic + increase
# print("未来第一个月播放总量为：",total)
# print("未来第一个月播放总量为：",basic+increase)
# total += increase
# print("未来第二个月播放总量为：",total)
# print("未来第二个月播放总量为：",basic+increase*2)

# 标识符
# true = 0
# print(true)

# 案例：交换两个变量值
# a = 10
# b = 20
# print("a=",a)
# print("b=",b)
# c = a # 临时变量 此时c = 10 a = 10 b = 20
# a = b   # 此时a = 20 b = 20 c = 10
# b = c   # 此时a = 20 b = 10 c = 10
# print("a=",a)
# print("b=",b)

# 案例 - 升级：交换三个变量值（a = 100, b = 200, c = 300）
# a = 100
# b = 200
# c = 300
# print("a=",a)
# print("b=",b)
# print("c=",c)
# print("---------------------------------------")
# d = a   # 临时变量 此时d = 100 a = 100 b = 200 c = 300
# a = c   # 此时a = 300 b = 200 c = 300 d = 100
# c = b   # 此时a = 300 b = 200 c = 200 d = 100
# b = d   # 此时a = 300 b = 100 c = 200 d = 100
# print("a=",a)
# print("b=",b)
# print("c=",c)

# 查看数据类型 ---> type() 获取指定的数据的类型
# print("Hello World")
# print(type("Hello World"))  # str
# print(type(10))   # int
# print(type(3.14)) # float
# print(type(True))   # bool
# print(type(None))   # NoneType
#
# num = 10
# print(num)
# print(type(num))    # int

# 检查数据是否属于指定类型 ---> isinstance(数据,类型) ---> 返回bool值 ---> 是：返回True，否：返回False
num = 100   # int
print(isinstance(num, int))     # True
print(isinstance(num, float))   # False
print(isinstance(num, str))     # False
print(isinstance(num, bool))    # False
print(isinstance(num, NoneType))    # False