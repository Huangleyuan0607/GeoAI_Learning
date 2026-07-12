# for循环
# 案例：遍历字符串"Hello-GeoAI"、

# 定义要遍历的字符串
# msg = "Hello-GeoAI"
msg = input("请输入需要遍历的字符串：")

# 遍历字符串并处理
for i in msg:   # i表示遍历出来的元素；msg表示需要遍历的数据
    print(f"元素：{i}")
else:   # 可选
    print("遍历结束")

# 案例：基于for循环完成如下需求
# 1.计算1-100之间所有奇数之和。
i = 1;
sum = 0;
# 法一：使用range(start,end,step)
for i in range(1,101,2):    # 注意：range数字序列不包含end本身。
    sum += i
else:
    print(f"1-100之间所有奇数之和为：{sum}")
# 法二：使用if条件语句判断
sum = 0;    # 初始化sum的值
for i in range(1,101):    # 注意：range数字序列不包含end本身。
    if i % 2 != 0:
        sum += i
else:
    print(f"1-100之间所有奇数之和为：{sum}")


# 2.计算100-500之间所有3的倍数的数字之和。
s = 100;
sum1 = 0

# 法一：使用range(start,end,step)
for s in range(102,501,3):
    sum1 += s
else:
    print(f"100-500之间所有3的倍数的数字之和为：{sum1}")

# 法二：使用if条件语句判断
sum1 = 0;
for s in range(102,501):
    if s % 3 == 0:
        sum1 += s
else:
    print(f"100-500之间所有3的倍数的数字之和为：{sum1}")
