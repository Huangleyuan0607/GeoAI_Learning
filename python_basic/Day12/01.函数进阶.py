# 函数进阶
# 函数 - 变量的作用域
# 全局变量
num = 100

# 定义函数
def circle_area(r):
    # 局部变量：只能在函数内部使用
    pi =3.14
    area = pi * r * r

    global num
    num = 10000     # 这里的num在不使用global关键字时，实质是局部变量num，与外部定义的全局变量不同
    print("num =", num)     # 全局变量在函数内部也可以访问

    return area

# 局部变量只能在函数内部使用，外部使用会报错 NameError: name 'pi' is not defined
'''
print("pi =", pi)
print("area =", area)
print("r =", r)
'''

# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ",num)     # 全局函数在函数外部可以访问，即使函数内部也定义了num，但其为局部变量，函数外部无法访问


# 函数 - 传参方式
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 传参方式一：位置参数
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

# 传参方式二：关键字参数
stu = reg_stu("王林", age = 28, gender = "男", city = "北京")
print(stu)

stu = reg_stu(age = 20, gender = "女", city = "北京", name = "李慕婉")
print(stu)

# 传参方式三：位置参数 + 关键字参数 ---> 位置参数在前，关键字参数在后
stu = reg_stu("李慕婉", 20, gender = "女", city = "北京")
print(stu)


# 函数 - 默认参数
# 定义函数
def reg_stu(name, age, gender = "男", city = "北京"):      # 默认参数需要放在非默认参数的后面
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu("王林", 28)
print(stu)

stu = reg_stu("李慕婉", 18, "女")
print(stu)

stu = reg_stu("韩立", 22, city = "上海")
print(stu)


# 函数 - 不定长参数
# 案例：定义函数，根据传入的数据，计算这批数据中的最小值、最大值、平均值。

# 位置参数 *args --> 元组
# 定义函数
def calc_data(*args):       #
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)

# 调用函数
data = calc_data(2, 7, 9, 10, 45)
print(data)

data = calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222)
print(data)

# 位置参数 **kwargs --> 字典
# 定义函数
def calc_data(*args, **kwargs):
    """
    根据传入的这批数据，计算这批数据的最小值，最大值和平均值。
    :param args:不定长位置参数，需要计算的这批数据
    :param kwargs:不定长关键字参数
        round:保留的小数位个数
        print:是否打印输出
    :return:最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round"):
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值：{min_data}, 最大值：{max_data}, 平均值：{avg_data}")
    return min_data, max_data, avg_data

# 调用函数
data = calc_data(2, 7, 9, 10, 15, 33, round = 3 , print = True)
print(data)

data = calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round = 3, print = False)
print(data)


# 函数 - 函数作为参数
# 加
def add(x, y):
    return x + y

# 减
def subtract(x, y):
    return x - y

# 乘
def multiply(x, y):
    return x * y

# 除
def divide(x, y):
    return x / y

# 计算操作函数
def calc(x, y, oper):
    return oper(x,y)

# 调用函数
print(calc(10, 20, divide))


# 函数 - 匿名函数（lambda表达式）
# 定义匿名函数 ---> lambda 参数列表 : 函数体
out_line = lambda : print("-------------------------------------")
add = lambda x, y: x + y

out_line()
print(add(100, 200))

# 需求1：打印一个分割线
def out_line():
    print("------------------------------------")

out_line1 = lambda : print("------------------------------------")
out_line()
out_line1()

# 需求2：计算两个数之和
def add(x, y):
    return x + y

add1 = lambda x, y: x + y

print(add(100,200))
print(add1(100, 200))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
data_list.sort()        # 默认排序是按照首字母次序排序（若相同就比后一位）
print(data_list)

data_list.sort(key = lambda item : len(item))   # 匿名函数典型的应用场景（作为高阶函数的参数传递）
print(data_list)


