# 字典 dict
# 定义字典存储
dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}

print(dict1)
print(type(dict1))

# key必须得是不可变类型
dict2 = {0:670, 1.5:608, (1, 2):580}
print(dict2)

# 访问
print(dict1["王林"])      # 获取值
dict1["王林"] = 680       # 修改值
print(dict1)


# 字典常用操作
# 添加数据：字典名称[Key] = value （key若存在就是修改）
dict1["涛哥"] = 550
print(dict1)

# 修改指定key对应值：字典名称[key] = value （key若不存在就是添加）
dict1["涛哥"] = 620
print(dict1)

# 根据key获取value：字典名称[key] / 字典名称.get(key)
print(dict1["涛哥"])
print(dict1.get("涛哥"))

# 获取所有key：字典名称.keys()
print(dict1.keys())

# 获取所有value：字典名称.values()
print(dict1.values())

# 获取所有的键值对：字典名称.items()
print(dict1.items())

# 删除指定key并返回对应value：字典名称.pop(key)
score = dict1.pop("徐立国")
print(score)
print(dict1)

# 删除指定键值对：del 字典名称[key] （注意：获取不到对应值）
del dict1["韩立"]
print(dict1)


# 遍历输出字典
for k in dict1.keys():      # 通过key值遍历输出
    print(f"{k}：{dict1[k]}")

for item in dict1.items():      # 通过items方法遍历输出
    print(f"{item[0]}：{item[1]}")

for k , v in dict1.items():     # 通过解包遍历输出
    print(f"{k}：{v}")


# 字典案例
# 案例1：通过控制台菜单与用户交互。具体功能如下:开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，

# shopping_cart = dict()       # 定义购物车字典
#
# while True:      # 当没有选择退出购物车时一直循环
#     # 1、制作菜单
#     print("###### 欢迎使用购物车管理系统 ######")
#     print("#         1、添加购物车          #")
#     print("#         2、修改购物车          #")
#     print("#         3、删除购物车          #")
#     print("#         4、查询购物车          #")
#     print("#         5、退出购物车          #")
#     print("#################################")
#     choice = int(input("请选择要执行的操作(1-5)："))
#
#     match choice:
#         case 1:
#             # 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#             print("欢迎使用添加购物车功能~")
#             good_name = input("请输入要添加的商品名称：")
#             good_price = float(input("请输入要添加的商品价格："))
#             good_num = int(input("请输入要添加的商品数量："))
#
#             # 如果商品存在，则不执行添加，提示信息
#             if good_name in shopping_cart:
#                 print("该商品已存在，请重新选择~")
#             else:
#                 shopping_cart[good_name] = {"price": good_price, "num": good_num}       # 这里的value实质就是一个字典
#                 print(f"商品{good_name}添加完毕~")
#
#         case 2:
#             # 修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#                 print("欢迎使用修改购物车功能~")
#                 good_name = input("请输入要修改的商品名称：")
#                 # 如果商品不存在，则提示错误信息
#                 if good_name not in shopping_cart:
#                     print("该商品不存在，请重新选择~")
#                     continue    # 中断本次循环，直接进入下一次循环
#
#                 good_price = float(input("请输入要修改的商品价格："))
#                 good_num = int(input("请输入要修改的商品数量："))
#                 shopping_cart[good_name] = {"price": good_price, "num": good_num}   # 执行修改（实际上代码与添加相同）
#                 print(f"商品{good_name}修改完毕~")
#
#         case 3:
#             # 删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#                 print("欢迎使用删除购物车功能~")
#                 good_name = input("请输入要删除的商品名称：")
#                 # 如果商品不存在，则提示错误信息
#                 if good_name not in shopping_cart:
#                     print("该商品不存在，请重新选择~")
#                 else:
#                     del shopping_cart[good_name]    # 执行删除操作
#                     print(f"商品{good_name}删除完毕~")
#
#         case 4:
#             # 查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
#             print("欢迎使用查询购物车功能~")
#             for goods in shopping_cart.keys():
#                 good_info = shopping_cart[goods]
#                 print(f"查询成功！商品名称：{goods}，商品价格：{good_info["price"]}，商品数量：{good_info["num"]}")
#
#         case 5:
#             # 退出购物车
#             print("Bye~")
#             break
#
#         case _:     # 用于匹配其他所有情况
#             print("非法操作，不支持！！！")


#案例2：开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
# 1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生:遍历所有学生信息并输出。
# 6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7.退出系统。

# 1、制作菜单并定义空字典
print("欢迎使用教务管理系统~")
menu = '''
########### 教务管理系统 ##########
1、添加学生信息
2、修改学生信息
3、删除学生信息
4、查询学生信息
5、获取全体学生信息
6、统计班级成绩
7、退出系统
'''

students_info = {
    "张欣怡": {"chinese": 92, "math": 85, "english": 78},
    "李浩宇": {"chinese": 67, "math": 94, "english": 88},
    "王思睿": {"chinese": 73, "math": 61, "english": 96},
    "刘雨桐": {"chinese": 88, "math": 79, "english": 82},
    "陈泽洋": {"chinese": 95, "math": 90, "english": 74},
    "赵可欣": {"chinese": 81, "math": 76, "english": 91}
}

# 2、输出菜单并输入选择
while True:
    print(menu)
    choice = int(input("请选择要执行的操作(1-7)："))

    match choice:
        case 1:
            # 添加学生信息
            print("欢迎使用添加学生信息功能~")
            stu_name = input("请输入要添加的学生姓名：")

            # 如果学生信息存在，则不执行添加，提示信息
            if stu_name in students_info:
                print("该学生信息已存在，请重新选择~")
            else:
                stu_chinese = int(input("请输入语文成绩："))
                stu_math = int(input("请输入数学成绩："))
                stu_english = int(input("请输入英语成绩："))
                students_info[stu_name] = {"chinese": stu_chinese, "math": stu_math, "english": stu_english}
                print(f"学生{stu_name}信息添加完毕~")

        case 2:
            # 修改学生信息
            print("欢迎使用修改学生信息功能~")
            stu_name = input("请输入要修改的学生姓名：")

            # 如果学生信息不存在，则不执行修改，提示信息
            if stu_name not in students_info:
                print("该学生信息不存在，请重新选择~")
                continue

            stu_chinese = int(input("请输入语文成绩："))
            stu_math = int(input("请输入数学成绩："))
            stu_english = int(input("请输入英语成绩："))
            students_info[stu_name] = {"chinese": stu_chinese, "math": stu_math, "english": stu_english}
            print(f"学生{stu_name}信息修改完毕~")

        case 3:
            # 删除学生信息
            print("欢迎使用删除学生信息功能~")
            stu_name = input("请输入要删除的学生姓名：")

            # 如果学生信息不存在，则不执行修改，提示信息
            if stu_name not in students_info:
                print("该学生信息不存在，请重新选择~")
                continue

            del students_info[stu_name]  # 执行删除操作
            print(f"学生{stu_name}信息删除完毕~")

        case 4:
            # 查询学生信息
            print("欢迎使用查询学生信息功能~")
            stu_name = input("请输入要查询的学生姓名：")

            # 如果学生信息不存在，则不执行修改，提示信息
            if stu_name not in students_info:
                print("该学生信息不存在，请重新选择~")
                continue

            stu_info = students_info.get(stu_name)      # 存放查询学生姓名对应的value字典
            print(f"查询成功！学生姓名：{stu_name}，语文成绩：{stu_info["chinese"]}，数学成绩：{stu_info["math"]}，英语成绩：{stu_info["english"]}")

        case 5:
            # 列出所有学生
            for stu in students_info.keys():
                stu_info = students_info.get(stu)
                print(f"查询成功！学生姓名：{stu}，语文成绩：{stu_info["chinese"]}，数学成绩：{stu_info["math"]}，英语成绩：{stu_info["english"]}")

        case 6:
            # 统计班级成绩
            chinese_scores = []     # 定义存放语文成绩的列表
            math_scores = []     # 定义存放数学成绩的列表
            english_scores = []     # 定义存放英语成绩的列表
            max_chinese = "0"
            max_math = "0"
            max_eng = "0"
            min_chinese = "0"
            min_math = "0"
            min_eng = "0"

            for stu_name, stu_scores in students_info.items():        # 用解包遍历获取每个学生的成绩
                chinese_scores.append(stu_scores.get("chinese"))
                math_scores.append(stu_scores.get("math"))
                english_scores.append(stu_scores.get("english"))

                # 获取各个科目最高分与最低分学生姓名
                if stu_scores.get("chinese") == max(chinese_scores):
                    max_chinese = stu_name
                if stu_scores.get("math") == max(math_scores):
                    max_math = stu_name
                if stu_scores.get("english") == max(english_scores):
                    max_eng = stu_name
                if stu_scores.get("chinese") == min(chinese_scores):
                    min_chinese = stu_name
                if stu_scores.get("math") == min(math_scores):
                    min_math = stu_name
                if stu_scores.get("english") == min(english_scores):
                    min_eng = stu_name



            print(f"语文成绩最高分：{max(chinese_scores)}，由{max_chinese}同学取得，最低分：{min(chinese_scores)}，由{min_chinese}同学取得，平均分：{sum(chinese_scores) / len(chinese_scores):.2f}")
            print(f"数学成绩最高分：{max(math_scores)}，由{max_math}同学取得，最低分：{min(math_scores)}，由{min_math}同学取得，平均分：{sum(math_scores) / len(math_scores):.2f}")
            print(f"英语成绩最高分：{max(english_scores)}，由{max_eng}同学取得，最低分：{min(english_scores)}，由{min_eng}同学取得，平均分：{sum(english_scores) / len(english_scores):.2f}")

        case 7:
            print("Bye~")
            break

        case _:  # 用于匹配其他所有情况
            print("非法操作，不支持！！！")




