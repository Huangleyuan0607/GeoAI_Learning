# 函数案例
# 1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)。
def triangle_area(l, h):
    """
    根据传入的底和高计算三角形面积的函数
    :param l: 底长
    :param h: 高
    :return: 三角形面积
    """
    return l * h / 2

t_area = triangle_area(30, 20)
print("底长为30，高度为20的三角形面积：", t_area)

# 2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
def count_aeiou(s):
    """
    统计字符串中元音的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    yuanyin = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    # for i in "aeiouAEIOU":
    for i in s:
        if i in yuanyin:
            count += 1
    return count

c_aeiou = count_aeiou("Hello World Hello Python OK")
print(c_aeiou)

# 3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def cul_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)并返回
    :param score_list: 分数列表
    :return: 最高分、最低分、平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)     # 使用round()函数保留1位小数
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = cul_score(s_list)     # 解包获取多个返回值
print("最高分", max_score)
print("最低分", min_score)
print("平均分", avg_score)

# 4.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数>= 90:A
# 分数>=75:B
# 分数>=60:C
# 分数<60:D
def cul_grade(s):
    """
    根据传入的分数，计算对应的分数等级并返回。
    :param s: 分数
    :return: 等级
    """
    if s >= 90:
        return "A"
    elif s >= 75:
        return "B"
    elif s >= 60:
        return "C"
    else:
        return "D"

score = int(input("请输入分数："))
grade = cul_grade(score)
print(f"{score}分对应等级{grade}")

# 5.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。把字符串反转，如果和原字符串相同，就是回文串。(如:"level"，"radar"，"黄山落叶松叶落山黄")
def reverse_str(s):
    """
    判断一个字符串是否是回文串，返回bool值。
    :param s: 字符串
    :return: 是否是回文串（bool值）
    """
    rs = s[::-1]    # 反转字符串
    if rs == s:
        return True
    else:
        return False

str = input("请输入字符串：")
print(f"{str}是否是回文串：{reverse_str(str)}")

# 6.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def exchange_time(t):
    """
    完成时间转换功能，将传入的秒转换为小时、分钟、秒。。
    :param t:时间（秒）
    :return: 时、分、秒
    """
    h = t / 3600
    m = t /60
    return h, m, t

time = int(input("请输入秒数："))
hour, minute, second = exchange_time(time)
print(f"{time}秒对应{hour:.2f}时，{minute}分与{second}秒")

# 7.定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
def judge_triangle(a, b, c):
    """
    根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
    :param a: 第一条边长
    :param b: 第二条边长
    :param c: 第三条边长
    :return: 三角形类型
    """
    if a == b == c:
        return "等边三角形"
    elif a == b or b == c or c == a:
        return "等腰三角形"
    elif a + b > c and b + c > a and c + a > b:
        return "普通三角形"
    else:
        return "不能构成三角形"

x = int(input("请输入第一条边长："))
y = int(input("请输入第二条边长："))
z = int(input("请输入第三条边长："))
print(f"{x}、{y}、{z}三条边为{judge_triangle(x, y, z)}")