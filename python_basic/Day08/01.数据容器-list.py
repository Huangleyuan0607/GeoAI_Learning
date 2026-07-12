# ------------------------------------------列表操作------------------------------------------

# 定义
# s = [56, 90, 88, 65.11, 90, "A", "Hello", True]
# print(s)
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[0])     # 正向索引，起始值为0
# print(s[-8])    # 反向索引，起始值为-1
#
# print(s[2])     # 通过正向索引获取第3个元素
# print(s[-6])    # 通过反向索引获取第3个元素‘
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # 注意：如果指定的索引超出范围则会报错：list assignment index out of range
# # s[10] = "DEF"
# # print(s)
#
# # 删除
# del s[5]    # 删除列表中第6个元素，这里指的是"A"
# print(s)
#
# # 遍历（证明列表的元素有序）
# for item in s:
#     print(item,end = " ")

# ------------------------------------------列表切片------------------------------------------
# 定义列表
# s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]
#
# # 切片操作 --> s[开始索引:结束索引:步长]
# print(s[0:6:1])     # 截取并打印s列表中的前6个元素
# print(s[:6:])       # 由于开始索引的默认值为0，步长默认值为1，所以均可以省略，但第1个冒号不允许省略。
# print(s[:6])    #这三种写法最终结果一致
#
# print(s[0:8:1])
# print(s[0:-2:1])    # 截取并打印s列表中的第1个元素到倒数第3个元素（因为不打印结束索引处的元素）
# print(s[:-2:])
# print(s[:-2])       # 上述4种写法等效


# ------------------------------------------列表方法------------------------------------------

# 列表定义
# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
#
# # 常见的列表方法：
# # 1、append()：在列表尾部追加元素，如：s.append(1)
# s.append(188)   # 即在s列表尾部追加一个188
# print(s)
#
# # 2、insert()：在指定索引前插入元素，如：s.insert(0,92)
# s.insert(2,80)
# print(s)
#
# # 3、remove()：移除列表中第一个匹配到的值，如：s.remove(75)
# s.remove(90)    # 移除列表中值为90的元素
# print(s)
#
# # 4、pop()：删除列表中指定索引位置的元素，默认为最后一个，如：s.pop(7)
# e= s.pop(5)     # 删除列表中索引为5，即第6个位置的元素
# print(e)
# print(s)
#
# e = s.pop()     # 删除列表中最后一个元素（未指定索引时默认为最后一个）
# print(e)
# print(s)
#
# # 5、sort()：对列表中的值进行从小到大的排序（仅限于列表中所有元素数据类型一致时进行），如：s.sort()
# s.sort()
# print(s)
#
# # 6、reverse()：反转列表元素，如：s.reverse()
# s.reverse()
# print(s)


# ------------------------------------------列表案例------------------------------------------
# 需求：将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。

# 1、获取用户输出的10个数字并依次存储到列表中
# s = []    # 定义一个列表
# for i in range(10):     # 循环获取10个数字
#     num = int(input("请输入数字："))
#     s.append(num)     # 每次循环都向列表中加入一个值
# print(f"初始的数字列表为：{s}")
#
# # 2、将列表中数字进行排序
# s.sort()
# print(f"排序后的数字列表为：{s}")
#
# # 3、输出最值和平均值
#
# # 计算均值方法一：遍历累加后除以个数
# sum1 = 0   # 存储总值，后续用于计算均值
# for j in s:
#     sum1 += j
# avg = sum1 / len(s)      # 计算均值
# print(f"最小值为：{s[0]}")
# print(f"最大值为：{s[-1]}")
# print(f"平均值为：{avg}\n")
#
# # 计算均值方法二：sum()求和函数，len()获取列表长度函数
# avg = sum(s) / len(s)
# print(f"最小值为：{s[0]}")
# print(f"最大值为：{s[-1]}")
# print(f"平均值为：{avg}")


# 需求：合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）。

# 1、定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 2、合并列表
# for i in num_list2:
#     num_list1.append(i)
# print("合并后的列表：",num_list1)
#
# # 3、对合并结果进行去重处理
# # 下面这种做法的错误在于，当删除了某个元素时列表缩短，索引号前移，但j和k依旧按就旧索引递增，随着删除进行，j 和 k 会超过当前列表最大索引，最终报错。
# '''
# for j in range(len(num_list1)):
#     for k in range(len(num_list1)):
#         if j != k and num_list1[j] == num_list1[k]:
#             num_list1.remove(num_list1[j])
#             print(f"移除了重复的{num_list1[j]}")
# print("去重后的列表：",num_list1)
# '''
#
# new_list = []     # 去除重复记录后的列表
# for a in num_list1:
#     # 判断new_list中是否存在a元素，如不存在再添加
#     if a not in new_list:   # 判断元素是否存在于列表中，如果存在则返回True，不存在则返回False
#         new_list.append(a)
# print("去重后的列表：",new_list)
# print()
#
#
# # 简化版操作 --> 解包、加号
# # 1、定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 2、合并列表
# # 解包：将列表这一类容器解开成一个个独立的元素
# num_list3 = [*num_list1, *num_list2]
# print("合并后的列表：",num_list3)
#
# # 3、对合并结果进行去重处理
# # 下面这种做法的错误在于，当删除了某个元素时列表缩短，索引号前移，但j和k依旧按就旧索引递增，随着删除进行，j 和 k 会超过当前列表最大索引，最终报错。
# '''
# for j in range(len(num_list1)):
#     for k in range(len(num_list1)):
#         if j != k and num_list1[j] == num_list1[k]:
#             num_list1.remove(num_list1[j])
#             print(f"移除了重复的{num_list1[j]}")
# print("去重后的列表：",num_list1)
# '''
#
# new_list = []     # 去除重复记录后的列表
# for a in num_list3:
#     # 判断new_list中是否存在a元素，如不存在再添加
#     if a not in new_list:   # 判断元素是否存在于列表中，如果存在则返回True，不存在则返回False
#         new_list.append(a)
# print("去重后的列表：",new_list)
# print()
#
# # 简化版操作 --> 加号
# # 1、定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 2、合并列表
# # 直接用加号合并两个列表
# num_list4 = num_list1 + num_list2
# print("合并后的列表：",num_list4)
#
# # 3、对合并结果进行去重处理
# # 下面这种做法的错误在于，当删除了某个元素时列表缩短，索引号前移，但j和k依旧按就旧索引递增，随着删除进行，j 和 k 会超过当前列表最大索引，最终报错。
# '''
# for j in range(len(num_list1)):
#     for k in range(len(num_list1)):
#         if j != k and num_list1[j] == num_list1[k]:
#             num_list1.remove(num_list1[j])
#             print(f"移除了重复的{num_list1[j]}")
# print("去重后的列表：",num_list1)
# '''
#
# new_list = []     # 去除重复记录后的列表
# for a in num_list4:
#     # 判断new_list中是否存在a元素，如不存在再添加
#     if a not in new_list:   # 判断元素是否存在于列表中，如果存在则返回True，不存在则返回False
#         new_list.append(a)
# print("去重后的列表：",new_list)


# 需求1：生成1-20的平方列表

# 定义新列表
# s = []
#
# # 方法一：传统方式 --> 遍历1-20，将其平方值添加到s列表中
# for i in range(1,21):   # range(1,21)才表示遍历1-20
#     s.append(i**2)
# print("1-20的平方列表为：",s)
#
# # 方法二：列表推导式 --> 就是按照一定规则快速生成一个列表的方法 --> 语法格式：[要插入的值 for i in 序列/列表]
# s = []      # 初始化列表
# s = [i**2 for i in range(1,21)]     # 意思是将每次i的平方存入到列表中
# print("1-20的平方列表为：",s)

# 需求2：从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
new_list = []

# 方法一：传统方式 --> 遍历num_list，将其中的偶数添加到s列表中
# for num in num_list:
#     if num % 2 == 0:
#         new_list.append(num**2)
# print("从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表为：",new_list)
#
# # 方法二：列表推导式 --> 就是按照一定规则快速生成一个列表的方法 --> 语法格式：[要插入的值 for i in 序列/列表 if 条件]
# new_list = []
# new_list = [num**2 for num in num_list if num % 2 == 0]     # 意思是将其中偶数的平方存入列表
# print("从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表为：",new_list)



# -----------------------------------课后习题------------------------------------------
# 案例1：将如下多个列表合并为一个列表，并去除重复元素，排好序(升序)后输出到控制台。
list1= ['M','A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F','G']
list3 = ['W', 'A', 'S', 'D']

# 最快的方法：直接相加
new_list1= list1 + list2 + list3    # 通过直接相加合并后的列表
print("合并后的列表：",new_list1)
# 去除重复元素
new_list3= []   # 定义去重后的列表
for item in new_list1:
    if item not in new_list3:
        new_list3.append(item)
print("去重后的列表：",new_list3)
# 排序
new_list3.sort()
print("升序排列后的列表：",new_list3)

# 解包方法
new_list2= [*list1, *list2, *list3]     # 通过解包合并后的列表
print("合并后的列表：",new_list2)
# 去除重复元素
new_list4= []   # 定义去重后的列表
for item in new_list1:
    if item not in new_list4:
        new_list4.append(item)
print("去重后的列表：",new_list4)
# 排序
new_list4.sort()
print("升序排列后的列表：",new_list4)

# 遍历方法（此处省略）


# 案例2：将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26,27, 28,29, 30]

# 最简洁的方法：列表推导式
new_list5= [num**2 for num in list4 if num % 3 == 0 or num % 5 == 0]
print("列表中能被3或5整除的元素的平方组成新列表为：",new_list5)

# 遍历方法（此处省略）

# 案例3：将如下列表中的正数提取出来，封装为一个新的列表。
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

# 最简洁的方法：列表推导式
new_list6= [num for num in list5 if num > 0]
print("列表中的正数组成新列表为：",new_list6)
