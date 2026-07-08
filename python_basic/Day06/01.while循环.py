# While循环
# 案例：打印10遍“人生苦短，我用Python~”
# i = 0
# while i < 10:
#     print("人生苦短，我用Python~")
#     i += 1
# else:
#     print("打印完毕~")

# while案例
# 案例：计算1-100之间所有偶数的累加之和。
num = 1     # 循环开始数字
sum = 0     # 记录累加和
while num <= 100:
    if num % 2 == 0:    # 说明这里num是偶数
        sum += num
    num += 1
else:
    print(f"1-100之间所有偶数累加之和为{sum}")     # 也可以直接顶格写，不用加else。