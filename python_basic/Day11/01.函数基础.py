# 函数
# 注意：函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义后调用
# 定义函数
# def out_line():     # 函数名的命名规范与变量名一致（同属于标识符）
#     """
#     输出两条横线
#     :return:无
#     """
#     print("------------------------------")
#     print("------------------------------")
#
# # 调用函数
# out_line()
# print()
# out_line()      # 函数可复用
# print()
# out_line()
#
#
# # 函数的参数与返回值
# # 函数1：计算圆的面积 --> 半径
# def circle_area(r):
#     """
#     根据圆的半径，计算圆的面积
#     :param r: 圆的半径
#     :return: 圆的面积
#     """
#     area = 3.14 * r ** 2
#     return area
#
# help(circle_area)
#
# c_area = circle_area(10)    # 调用函数计算圆面积
# print(c_area)
#
# # 函数2：计算长方形的面积 --> 长, 宽
# def rectangle_area(l, w):
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l: 长方形的长度
#     :param w: 长方形的宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
#
# help(rectangle_area)    # 查看函数说明文档
#
# r_area = rectangle_area(20, 10)     # 调用函数计算长方形面积
# print(r_area)
#
# # 函数3：计算圆的面积与周长 --> 半径 ---> 如果有多个返回值，用逗号分隔 ---> 多个返回值会封装到元组中
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和圆的周长
#     :param r:圆的半径
#     :return:圆的面积，圆的周长
#     """
#     area = 3.14 * r ** 2
#     len = 3.14 * r * 2
#     return round(area, 1), round(len, 1)        # 用round()函数控制小数位数
#
# help(circle_area_len)
#
# c = circle_area_len(10)     # 多个返回值会封装到元组中
# print(c)
# print(type(c))
#
# c_area , c_len = circle_area_len(10)    # 用解包获取函数多个返回值
# print(c_area)
# print(c_len)


# 函数的嵌套调用 --> 遵循栈结构（LIFO,Last In First Out,即后进先出）
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")

function_a()
print("函数调用完毕~")


