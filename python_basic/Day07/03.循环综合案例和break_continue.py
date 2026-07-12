# 循环综合案例（包括while和for）和break-continue相关知识

# 需求:根据输入的用户名密码执行登录操作，具体要求如下:
# 1.正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666
# 2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
# 3.输入的用户名和密码不能为空!
# 4.登录成功:输出"登录成功，进入B站首页~"
# 5.登录失败:输出"用户名或密码错误，请重新输入!"

# 分析：while循环适用于循环次数未知，for循环适用于已知循环次数；这里无法准确知道循环次数，所以选用while循环
print("欢迎来到哔哩哔哩！")
# is_success = False
while True:     # 如果不用break，也可以用bool类型的is_success控制循环是否进行
    # 从用户处获取账号密码
    input_id = input("请输入账号：")
    input_psd = input("请输入密码：")

    # 限定用户名或密码不能为空
    if input_id == "" or input_psd == "":
        print("用户名或密码不能为空，请重新输入!")
        continue    # 当账号密码至少有一个为空时，使用continue中断本次循环，直接进入下一轮循环，即直接开始重新输入账号密码。

    # 判断账号密码是否正确
    if input_id == "admin" and input_psd == "666888":
        print(f"用户{input_id}登录成功，进入B站首页~")
        # is_success = True
        break   # 当账号密码正确时使用break跳出循环
    elif input_id == "zhangsan" and input_psd == "123456":
        print(f"用户{input_id}登录成功，进入B站首页~")
        # is_success = True
        break   # 当账号密码正确时使用break跳出循环
    elif input_id == "taoge" and input_psd == "888666":
        print(f"用户{input_id}登录成功，进入B站首页~")
        # is_success = True
        break   # 当账号密码正确时使用break跳出循环
    else:
        print("用户名或密码错误，请重新输入!")


# 案例：猜数字游戏
# 1、系统随机生成一个随机数
# 2、用户根据提示猜数字，并将所猜的数字输入系统
# 3、如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4、如果猜对，系统自动退出，游戏结束

# 导入random库用以生成随机数
import random

# 生成随机数
random_num = random.randint(1,100)

while True:
    # 获取用户输入的数字
    num = input("请输入一个数字：")

    # 控制输入值不可为空
    if num == "":
        print("输入的数字不可为空！")
        continue

    # 判断输入的数字与随机数的大小或正确
    if int(num) > random_num:
        print("您输入的数字太大了！")
    elif int(num) < random_num:
        print("您输入的数字太小了！")
    else:
        print(f"恭喜您回答正确！随机数为：{random_num}")
        break


