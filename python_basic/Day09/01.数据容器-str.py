# 字符串 基本操作 --> 不可变的（无法修改）、有序性、可迭代性
s = "Hello-Python"

print(s[4])     # 正向索引
print(s[-8])    # 反向索引

# 因为字符串具有不可变性，所以下面这种写法是错误的
'''
s[4] = "X"
print(s)
'''

for i in s:
    print(i)

# 切片
# 截取Hello
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

# 截取Python
print(s[6:12:1])
print(s[6::1])
print(s[6::])
print(s[6:])

print("----------------------------------")
# 步长 --> 正数：从前往后截取；负数：从后往前截取
print(s[0:5:2])
print(s[0:5:-1])    # 步长为负数时从后往前截取，而s[0:5]为从前往后截取，二者发生冲突故未输出结果。
print(s[-1:-7:-1])      # 从后往前截取，达到反转字符串的效果
print(s[::-1])      # 整体反转字符串


# 字符串常用方法
print("\n---------------------------------------------")
s = "   Hello-Python-Hello-World   "

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割 - 列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace() 将字符串中的指定字串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print("----------------------")
print("原始字符串：",s)      # 因为字符串具有不可变性，所以上述操作均不改变字符串本身



# ------------------------------------------------
# 字符串案例
# 案例1：邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。

# 方法1：使用count()方法
# 1、接收用户输入的邮箱
email = input("请输入邮箱地址：")

# 2、判断邮箱格式
count1 = email.count("@")   # 计算邮箱中@的个数
count2 = email.count(".")   # 计算邮箱中.的个数

if count1 == 1 and count2 > 0:          # 也可以直接写成：if email.count("@") == 1 and email.count(".") > 0:
    print(f"{email}邮箱格式正确~")
else:
    print(f"{email}邮箱格式错误！")

# 方法2：in 运算符 --> 判断子串是否存在字符串中，存在返回True；否则返回False（只判断有无，不论个数）
# 1、接收用户输入的邮箱
email = input("请输入邮箱地址：")

# 2、判断邮箱格式
count1 = email.count("@")   # 计算邮箱中@的个数

if count1 == 1 and "." in email:          # 也可以直接写成：if email.count("@") == 1 and "." in email:
    print(f"{email}邮箱格式正确~")
else:
    print(f"{email}邮箱格式错误！")


# 案例2：输入一个字符串，判断该字符串是否是回文(两边对称)
# 黄山落叶松叶落山黄
# 上海自来水来自海上

# 1、获取用户输入的字符串
s1 = input("请输入一串字符：")

# 2、判断字符串是否是回文（两边对称） --> 使用s1[::-1]整体反转字符串
s2 = s1[::-1]   # s2即为用户输入的字符串的反转版

if s1 == s2:
    print(f"{s1}是回文~")
else:
    print(f"{s1}不是回文~")


# 案例3：将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。

# 定义空列表存放处理后的字符串
s4 = []

# 循环10次处理过程
for i in range(10):
    # 1、获取用户输入的字符串
    s1 = input("请输入一串字符：")

    # 2、反转字符串 --> 使用s1[::-1]整体反转字符串
    s2 = s1[::-1]   # s2即为用户输入的字符串的反转版

    # 3、转换为大写记录在列表中 --> 使用列表的append()方法和字符串的upper()方法
    s4.append(s2.upper())

# 遍历输出列表
for i in s4:
    print(i,end = "\t")




