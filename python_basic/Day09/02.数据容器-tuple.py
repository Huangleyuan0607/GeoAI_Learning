# 元组基本操作 - tuple(读作“塌破”) 元素可重复、有序、不可修改
# 定义元组
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)      # 区别于列表使用中括号定义，元组使用小括号定义

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

# count() 统计元素个数
print(t1.count(1))

# index() 获取元素的索引（第一个元素出现的位置）
print(t1.index(1))


# 注意点：
t2 = ()     # 定义空元组
print(t2)
print(type(t2))

t3 = (100,)   # 正确定义单元素元组的方法（在单个元素后加逗号，不加逗号的含义就是给t3赋值100）
print(t3)
print(type(t3))


# -------------------------------------------------
# 元组的组包和解包

# 组包操作
t1 = (5, 7, 9, 10, 2, 23, 12)
t2 = 5, 7, 9, 10, 2, 23, 12     # 不加小括号也可以，python会识别为元组，但建议加上。

# 解包操作
# 基础解包 --> 注意：如果仅使用基础解包，那么变量的数量必须和元组中元素数量相等。
a, b, c, d, e, f, g = t1
print(a, b, c, d, e, f, g)

# (*)扩展解包 --> （* 收集剩余的所有元素并封装到列表list中）
first, second, *other, last = t1
print(first, second)    # 输出分别为5和7
print(other)    # 输出为[9, 10, 2, 23]
print(last)     # 输出为12

*other, last2, last1 = t1
print(*other)   # 输出为[5, 7, 9, 10, 2]
print(last2)    # 输出为23
print(last1)    # 输出为12


#----------------------------------------------
# 元组案例
# 案例1：现有两个变量，分别为:a = 10,b = 20，现需要将这两个变量值交换，然后输出到控制台。
a = 10
b = 20

# 原始方法是引入中间变量，新方法采用了组包操作

'''
# 组包
t = b, a
# 解包
a, b =t
'''
# 上述操作可简化为下面写法 二者含义相同
a, b = b, a     #b, a其实是元组的写法，采用了组包的操作
print(a)
print(b)

# 案例2：现有三个变量，分别为:a = 100,b= 200,c= 300,现需要将这三个变量值进行交换，将a,b，c的值分别赋值给c，a,b，并将其输出到控制台。
a = 100
b = 200
c = 300

# 采用组包与解包操作
c, a, b = a, b, c

print(a)
print(b)
print(c)


# 案例3：根据提供的学生成绩单，完成如下需求:
# 1.计算每个学生的总分、各科平均分，然后一并输出。
# 2.统计各科成绩的最低分、最高分、平均分，并输出。
# 3.查找成绩优秀(平均分大于90)的学生，并输出。

# 1、存储学生信息
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 88, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 自写版
print("------------------------------------------------------------")
print("自写版")
# 2、计算每个学生的总分、各科平均分，然后一并输出。
print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
for s in students:      # s的样例：("S001", "王林", 85, 92, 78),
    # 计算每个学生的总分
    total = s[2] + s[3] + s[4]      # 计算总分
    avg = total / 3     # 计算平均分
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
print()

# 3、统计各科成绩的最低分、最高分、平均分，并输出。
yw_totals = 0   # 语文总分
yw_avgs = 0     # 语文均分
yw_min = 100      # 语文最低分
yw_max = 0      # 语文最高分
sx_totals = 0   # 数学总分
sx_avgs = 0     # 数学均分
sx_min = 100      # 数学最低分
sx_max = 0      # 数学最高分
yy_totals = 0   # 英语总分
yy_avgs = 0     # 英语均分
yy_min = 100      # 英语最低分
yy_max = 0      # 英语最高分

for s in students:
    yw_totals += s[2]   # 累加计算语文总分
    sx_totals += s[3]   # 累加计算数学总分
    yy_totals += s[4]   # 累加计算英语总分

    # 计算语文最高分与最低分
    if s[2] > yw_max:
        yw_max = s[2]
    if s[2] < yw_min:
        yw_min = s[2]

    # 计算数学最高分与最低分
    if s[3] > sx_max:
        sx_max = s[3]
    if s[3] < sx_min:
        sx_min = s[3]

    # 计算英语最高分与最低分
    if s[4] > yy_max:
        yy_max = s[4]
    if s[4] < yy_min:
        yy_min = s[4]

# 计算各科均分
yw_avgs = yw_totals / len(students)
sx_avgs = sx_totals / len(students)
yy_avgs = yy_totals / len(students)
print(f"语文学科最高分：{yw_max}，最低分：{yw_min}，平均分：{yw_avgs}")
print(f"数学学科最高分：{sx_max}，最低分：{sx_min}，平均分：{sx_avgs}")
print(f"英语学科最高分：{yy_max}，最低分：{yy_min}，平均分：{yy_avgs}")
print()

# 4、查找成绩优秀(平均分大于90)的学生，并输出。
perfects = []
for s in students:
    # 计算每个学生的总分
    total = s[2] + s[3] + s[4]      # 计算总分
    avg = total / 3     # 计算平均分
    if avg > 90:
        perfects.append(s[1])
print("成绩优秀(平均分大于90)的学生如下：")
for i in perfects:
    print(i, end=" ")
print("\n")



# 黑马版
print("------------------------------------------------------------")
print("黑马版")
# 2、计算每个学生的总分、各科平均分，然后一并输出。
print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
for s in students:      # s的样例：("S001", "王林", 85, 92, 78),
    # 计算每个学生的总分
    total = s[2] + s[3] + s[4]      # 计算总分
    avg = total / 3     # 计算平均分
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
print()

# 3、统计各科成绩的最低分、最高分、平均分，并输出。
# 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]   # 获取所有学生的语文单科成绩
math_scores = [s[3] for s in students]      # 获取所有学生的数学单科成绩
english_scores = [s[4] for s in students]   # 获取所有学生的英语单科成绩

# 统计各科成绩的最低分、最高分、平均分
print(f"语文最低分：{min(chinese_scores)}，最高分：{max(chinese_scores)}，平均分：{sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最低分：{min(math_scores)}，最高分：{max(math_scores)}，平均分：{sum(math_scores) / len(math_scores)}")
print(f"英语最低分：{min(english_scores)}，最高分：{max(english_scores)}，平均分：{sum(english_scores) / len(english_scores)}")
print()

# 4、查找成绩优秀(平均分大于90)的学生，并输出。
print("成绩优秀(平均分大于90)的学生如下：")
for s in students:
    # 计算每个学生的总分
    total = s[2] + s[3] + s[4]      # 计算总分
    avg = total / 3     # 计算平均分
    if avg > 90:
        print(f"学号：{s[0]}，姓名：{s[1]}，平均分：{avg:.1f}")
print()

# 黑马优化版 --> 基于元组的解包操作来实现
print("------------------------------------------------------------")
print("黑马优化版")
# 2、计算每个学生的总分、各科平均分，然后一并输出。
print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")

# 方式一：索引
# for s in students:      # s的样例：("S001", "王林", 85, 92, 78),
#     # 计算每个学生的总分
#     total = s[2] + s[3] + s[4]      # 计算总分
#     avg = total / 3     # 计算平均分
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

# 方式二：元组解包
for id, name, chinese, math, english in students:   # 将students里的子元组解包出来赋值给这五个变量
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
print()

# 3、统计各科成绩的最低分、最高分、平均分，并输出。
# 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]   # 获取所有学生的语文单科成绩
math_scores = [s[3] for s in students]      # 获取所有学生的数学单科成绩
english_scores = [s[4] for s in students]   # 获取所有学生的英语单科成绩

# 统计各科成绩的最低分、最高分、平均分
print(f"语文最低分：{min(chinese_scores)}，最高分：{max(chinese_scores)}，平均分：{sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最低分：{min(math_scores)}，最高分：{max(math_scores)}，平均分：{sum(math_scores) / len(math_scores)}")
print(f"英语最低分：{min(english_scores)}，最高分：{max(english_scores)}，平均分：{sum(english_scores) / len(english_scores)}")
print()

# 4、查找成绩优秀(平均分大于90)的学生，并输出。
print("成绩优秀(平均分大于90)的学生如下：")

# 方法一：索引
# for s in students:
#     # 计算每个学生的总分
#     total = s[2] + s[3] + s[4]      # 计算总分
#     avg = total / 3     # 计算平均分
#     if avg > 90:
#         print(f"学号：{s[0]}，姓名：{s[1]}，平均分：{avg:.1f}")
# print()

# 方法二：元组解包
for id, name, chinese, math, english in students:   # 将students里的子元组解包出来赋值给这五个变量
    total = chinese + math + english
    avg = total / 3
    if avg > 90:    # 判断优秀学生
        print(f"学号：{id}，姓名：{name}，平均分：{avg:.1f}")
print()
