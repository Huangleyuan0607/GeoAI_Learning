# match...case模式匹配案例
# 需求：判断用户输入星期几对应的日程
# day = int(input("请输入星期几（1-7）："))
# match day:
#     case 1:
#         print("周一：工作会议日")
#     case 2:
#         print("周二：学习培训日")
#     case 3:
#         print("周三：项目开发日")
#     case 4:
#         print("周四：代码审查日")
#     case 5:
#         print("周五：总结规划日")
#     case 6 | 7:     # 这里的|表示或的关系，匹配多个模式中的任意一个，其作用等效于or
#         print("周末：休息放松日")
#     case _:     # 匹配其他所有情况，类似于else
#         print("输入格式错误！")

# 需求：实现一个计算器，可以实现+-*/运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
num1 = float(input("请输入数字1："))
num2 = float(input("请输入数字2："))
oper = input("请输入运算符（+ - * /）：")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:   #还需要考虑当num2 = 0时不允许除法
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("运算符输入有误！请检查后重新输入。")








