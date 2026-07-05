# if...else案例

# 需求：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现(正确账号和密码为18888888888/666888)
# # 正确的账号密码
# correct_id = "18888888888"
# correct_psd = "666888"
#
# # 从键盘获取用户输入的账号密码
# print("欢迎来到哔哩哔哩！")
# input_id = input("请输入您的帐号：")
# input_psd = input("请输入您的密码：")
#
# # 判断账号密码是否全部正确，如果都正确则登录成功，进入B站首页
# if input_id == correct_id and input_psd == correct_psd:
#     print("登录成功！欢迎来到B站首页！")
# else:
# # 只要账号密码不是全部正确就登录失败
#     print("账号或密码错误！请检查后重新输入！")


# 需求:根据用户输入的年份，判断这一年是闰年还是平年。
# 非整百年份，且能被4整除的年份是闰年。整百年份（如1900年、2000年）必须能被400整除才是闰年
# print("欢迎使用闰平年判断器~")
# year = int(input("请输入年份："))
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f"{year}年是闰年。")
# else:
#     print(f"{year}年是平年。")

# if...elif...else案例
# 需求3:根据用户输入的数字，判断该数字是正数还是负数还是0
# print("欢迎使用数字判断器~")
# num = float(input("请输入数字："))
# if num > 0:
#     print(f"{num}是一个正数。")
# elif num < 0:
#     print(f"{num}是一个负数。")
# else:
#     print(f"{num}是0。")


# 需求：根据输入用户名、密码进行登录系统。
# 用户名、密码为 admin/666888 或root/547527 或zhangsan/123456,则输出登录成功
# 否则就提示用户名或密码错误
# print("欢迎来到本系统~")
# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# if username == 'admin' and password == '666888':
#     print(f"{username}用户，欢迎登陆~")
# elif username == 'root' and password == '547527':
#     print(f"{username}用户，欢迎登陆~")
# elif username == 'zhangsan' and password == '123456':
#     print(f"{username}用户，欢迎登陆~")
# else:
#     print("账号或密码错误！请检查后重新输入！")


# # 需求：根据输入的考试成绩，判断成绩等级。大于等于85分为优秀，60-85分为及格，否则就是不及格。
# print("欢迎使用成绩等级计算器~")
# points = int(input("请输入您的考试成绩："))
#
# if points >= 85:
#     print("您的成绩等级为优秀！")
# elif points >= 60 and points <= 85:
#     print("您的成绩等级为合格！")
# else:
#     print("您的成绩不合格！")
#
# # 需求：购物折扣计算:根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# # 金额>=500:8折
# # 300<=金额<500:9折
# # 100<=金额<300:95折
# # 金额<100:无折扣
# print("欢迎使用购物折扣计算器~")
# buy_count = float(input("请输入您的购物金额："))
#
# if buy_count >= 500:
#     print("您的购物折扣为8折！")
# elif buy_count >= 300 and buy_count < 500:
#     print("您的购物折扣为9折！")
# elif buy_count >= 100 and buy_count < 300:
#     print("您的购物折扣为95折！")
# else:
#     print("很抱歉，您的购物金额小于100元，无法享受购物折扣！")

# 需求：三角形类型判断:根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
line1 = int(input("请输入边长1："))
line2 = int(input("请输入边长2："))
line3 = int(input("请输入边长3："))

# maxline = max(line1, line2, line3)
# minline = min(line1, line2, line3)

if line1 + line2 > line3 and line2 + line3 > line1 and line1 + line3 > line2:
    if line1 == line2 == line3:
        print(f"{line1}、{line2}、{line3}三条边构成了一个等边三角形！")
    elif line1 == line2 or line2 == line3 or line1 == line3:
        print(f"{line1}、{line2}、{line3}三条边构成了一个等腰三角形！")
    else:
        print(f"{line1}、{line2}、{line3}三条边构成了一个普通三角形！")
else:
    print(f"{line1}、{line2}、{line3}三条边不能构成三角形！")