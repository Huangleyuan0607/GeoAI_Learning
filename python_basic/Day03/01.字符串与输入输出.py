# # 双引号定义（不可换行）
# s1 = "Hello"
#
# # 单引号定义（不可换行）
# s2 = 'World'
#
# # 多引号定义（可换行）
# s3 = """
# 亲爱的刘教授：
#     您好！我是黄乐源。
#     感谢您的耐心！
# """
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# # 定义字符串 ---> It's very good!
# # 常见转义字符：\'(单引号) \"(双引号) \t(制表符) \n(换行符)
# msg1 = 'It\'s very good!'
# msg2 = "It's very good!"    # 当内容里含有单引号时，也可以直接使用双引号来定义。
# msg3 = "Hello的意思是：\"你好！\""
# msg4 = 'Hello的意思是："你好！"'    #当内容里含有双引号时，也可以直接使用单引号来定义。
# print(msg1)
# print(msg2)
# print(msg3)
# print(msg4)
#
# print("欢迎收看节目！\n大家记得点赞哦~")  # \n即为换行符
# print("\t欢迎收看节目！\n\t大家记得点赞哦~")  # \t即为制表符
from jedi.api.refactoring import extract

# 字符串拼接
# s1 = "人生苦短" "我用Python" ",OK"    #中间空格可以省略
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用Python"
# print("龟叔说：" + msg1 + "," +msg2 + "。")

# name = "黄乐源"
# age = 22
# major = "地理信息科学"
# hobby = "打篮球、Python"
# # 加号只能用于字符串拼接，这里需要把int类型的age显示转式换为str类型才能使用加号拼接。
# print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + major + "，爱好" + hobby + "。")

# 字符串格式化（用以解决诸如前面int类型的age无法用加号连接来输出的情况）
# 方法1 --> %s 占位符
# name = "黄乐源"
# age = 22
# major = "地理信息科学"
# hobby = "打篮球、Python"
# # 加号只能用于字符串拼接，这里需要把int类型的age显示转式换为str类型才能使用加号拼接。
# print("大家好，我是%s，今年%s岁，学习的专业是%s，爱好%s。" %(name, age, major, hobby))   # 当有多个元素需要占位时使用括号来囊括这些元素
#
# # 方法2 --> f"内容{变量/表达式}"
# print(f"大家好，我是{name}，今年{age}岁，学习的专业是{major}，爱好{hobby}。")   # 注意：一定要在前引号前加f，这样才不会把{}直接识别为大括号

# 获取键盘上输入的数据 --> input(...)
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
# print(f"您的姓名为：{name}，年龄为：{age}。")

# 案例：模拟银行卡ATM取款。
# sum = 10000
# psd = 123456
# input_psd = int(input("请输入您的密码："))
# if input_psd == psd:
#     print("密码正确，欢迎光临！")
#     extract1 = int(input("请输入取款金额："))   # input函数获取到的数据默认为str类型，这里的取款金额需要显式转换为int类型才能执行减法计算
#     print(f"您的取款金额是：{extract1}，取款后卡内余额为：{sum - extract1}")
# else:
#     print("密码错误！身份验证失败！")

# 案例：实现两数求和功能
print("欢迎使用加法计算器！")
num1 = int(input("请输入数字1："))
num2 = int(input("请输入数字2："))
sum = num1 + num2
print(f"计算完毕！您的计算结果为:{num1} + {num2} = {sum}")






