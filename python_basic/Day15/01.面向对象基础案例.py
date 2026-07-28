# 案例：采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下:
# 1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
# 3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
# 5.展示全部学生成绩:展示出系统中所有学生的成绩

# 学生类
# class Student:
#     def __init__(self, name, chinese, math, english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#
#     def __str__(self):
#         return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"
#
#     # 修改学生成绩
#     def update_score(self, chinese = None, math = None, english = None):    # 设置默认值后可以支持仅修改一门或两门成绩的操作
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english
#
# # 教务管理系统类
# class EduManagement:
#     # 类属性
#     system_version = "1.0"
#     system_name = "教务管理系统"
#
#     def __init__(self):
#         # 实例属性
#         self.student_list = []      # 列表，记录的是在校学生的成绩
#
#     # 添加学生成绩
#     def add_student(self):
#         name = input("请输入学生姓名：")
#
#         # 判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
#         for i in self.student_list:
#             if i.name == name:
#                 print("该学生信息已经存在，添加失败！")
#                 return
#
#         chinese = int(input("请输入语文成绩："))
#         math = int(input("请输入数学成绩："))
#         english = int(input("请输入英语成绩："))
#
#         # 判断分数是否在0-100之间
#         if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#             stu = Student(name, chinese, math, english)
#             self.student_list.append(stu)
#             print(f"学生{name}信息添加成功~")
#         else:
#             print("各科成绩必须在0-100之间！")
#
#
#     # 修改学生成绩
#     def update_student(self):
#         name = input("请输入要修改的学生姓名：")
#
#         # 判断学生姓名是否存在，如果存在，则执行修改操作
#         for i in self.student_list:
#             if i.name == name:
#                 print(f"当前成绩：{i}")
#
#                 chinese = int(input("请输入修改后的语文成绩："))
#                 math = int(input("请输入修改后的数学成绩："))
#                 english = int(input("请输入修改后的英语成绩："))
#
#                 # 判断分数是否在0-100之间
#                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                     i.update_score(chinese, math, english)
#                     print(f"学生{name}信息修改成功~")
#                     print(f"修改后成绩：{i}")
#                     return
#                 else:
#                     print("各科成绩必须在0-100之间！")
#                     return
#
#         # 学生不存在则弹出提示信息
#         print("未找到该学生，修改失败！")
#
#     # 删除学生信息
#     def delete_student(self):
#         name = input("请输入要删除的学生姓名：")
#
#         # 判断学生姓名是否存在，如果存在，则执行删除操作
#         for i in self.student_list:
#             if i.name == name:
#                 self.student_list.remove(i)
#                 print(f"学生{name}信息删除成功~")
#                 return
#
#         # 学生不存在则弹出提示信息
#         print("未找到该学生，删除失败！")
#
#
#     # 查询指定学生成绩
#     def query_student(self):
#         name = input("请输入要查询的学生姓名：")
#
#         # 判断学生姓名是否存在，如果存在，则执行查询操作
#         for i in self.student_list:
#             if i.name == name:
#                 print(f"学生信息：{i}")
#                 return
#
#         # 学生不存在则弹出提示信息
#         print("未找到该学生，查询失败！")
#
#     # 展示所有学生成绩
#     def list_student(self):
#         for i in self.student_list:
#             print(i)
#
#     # 运行系统
#     def run(self):
#         print(f"欢迎使用{EduManagement.system_name} {EduManagement.system_version}")
#
#         while True:
#             print()
#             print("############################################################################")
#             print("1、添加学生   2、修改学生   3、删除学生   4、查询指定学生   5、查询所有学生   6、退出系统")
#             print("############################################################################")
#             print()
#
#             choice = int(input("请选择要执行的操作(1-6)："))
#             try:
#                 match choice:
#                     case 1:     # 添加学生
#                         self.add_student()
#                     case 2:     # 修改学生
#                         self.update_student()
#                     case 3:     # 删除学生
#                         self.delete_student()
#                     case 4:     # 查询指定学生
#                         self.query_student()
#                     case 5:     # 查询所有学生
#                         self.list_student()
#                     case 6:     # 退出系统
#                         print("欢迎下次使用~")
#                         break
#                     case _:     # 其他情况
#                         print("输入错误，请选择1-6之间的菜单功能！")
#             except ValueError:
#                 print("输入的数据有问题，请检查后重新输入！")
#             except Exception:
#                 print("程序运行出错了，请重新选择！")
#
# # 测试
# if __name__ == '__main__':
#     edu_management = EduManagement()
#     edu_management.run()


# 练习：采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车

# 商品类
class Good:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name} | 价格：{self.price} | 数量：{self.num}"

    # 修改商品信息
    def update_good(self, price = None, num = None):    # 设置默认值后可以支持仅修改数量或价格的操作
            if price is not None:
                self.price = price
            if num is not None:
                self.num = num

# 购物车管理系统类
class ShopCarManegement:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        # 实例属性
        self.good_list = []      # 列表，记录的是购物车中商品信息

    # 添加购物车
    def add_good(self):
        name = input("请输入商品名称：")

        # 判断商品是否存在，如果存在，则添加失败（不能重复添加）
        for i in self.good_list:
            if i.name == name:
                print("该商品信息已经存在，添加失败！")
                return

        price = float(input("请输入商品价格："))
        num = int(input("请输入商品数量："))

        # 判断价格和数量是否>0
        if price >= 0 and num >= 0:
            good = Good(name, price, num)
            self.good_list.append(good)
            print(f"商品{name}信息添加成功~")
        else:
            print("商品价格和数量都必须大于0！")

    # 修改购物车
    def update_good(self):
        name = input("请输入要修改的商品名称：")

        # 判断商品是否存在，如果存在，则执行修改操作
        for i in self.good_list:
            if i.name == name:
                print(f"该商品当前信息：{i}")

                price = float(input("请输入修改后的商品价格："))
                num = int(input("请输入修改后的商品数量："))

                # 判断价格和数量是否>0
                if price >= 0 and num >= 0:
                    i.update_good(price, num)
                    print(f"商品{name}信息修改成功~")
                    print(f"修改后商品信息：{i}")
                    return
                else:
                    print("商品价格和数量都必须大于0！")
                    return

        # 商品不存在则弹出提示信息
        print("未找到该商品信息，修改失败！")

    # 删除购物车
    def delete_good(self):
        name = input("请输入要修改的商品名称：")

        # 判断商品是否存在，如果存在，则执行删除操作
        for i in self.good_list:
            if i.name == name:
                self.good_list.remove(i)
                print(f"商品{name}信息删除成功！")
                return

        # 商品不存在则弹出提示信息
        print("未找到该商品信息，删除失败！")

    # 查询购物车
    def list_good(self):
        for i in self.good_list:
            print(i)

    # 运行系统
    def run(self):
        print(f"欢迎使用{ShopCarManegement.system_name} {ShopCarManegement.system_version}")

        while True:
            print()
            print("#################################################################")
            print("1、添加购物车   2、修改购物车   3、删除购物车   4、查询购物车   5、退出购物车")
            print("#################################################################")
            print()

            choice = int(input("请选择要执行的操作(1-5)："))
            try:
                match choice:
                    case 1:     # 添加购物车
                        self.add_good()
                    case 2:     # 修改购物车
                        self.update_good()
                    case 3:     # 删除购物车
                        self.delete_good()
                    case 4:     # 查询购物车
                        self.list_good()
                    case 5:     # 退出系统
                        print("欢迎下次使用购物车管理系统~")
                        break
                    case _:     # 其他情况
                        print("输入错误，请选择1-5之间的菜单功能！")
            except ValueError:
                print("输入的数据有问题，请检查后重新输入！")
            except Exception:
                print("程序运行出错了，请重新选择！")


# 测试
if __name__ == "__main__":
    shop_car_manegement = ShopCarManegement()
    shop_car_manegement.run()






