# 嵌套循环（如在for循环中再添加一个for循环）
# 需求：打印一个长度为m，宽度为n的长方形

# 从键盘获取m和n的值
m = int(input("请输入长方形的长度："))
n = int(input("请输入长方形的宽度："))

# 嵌套循环
for i in range(n):      # 遍历宽度 控制行 每次遍历生成一行*
    for j in range(m):      # 遍历长度 控制列 每次遍历生成一个*
        print("*", end="  ")   # 使用end来控制print不在结尾强制换行（默认下的end值为\n，所以会默认换行）
    print("\n")
else:
    print(f"{m}x{n}的长方形打印完毕~\n")


# 案例：打印99乘法表
for a in range(1,10):   # 控制乘式右边的值，外层循环控制行
    for b in range(1,a+1):      # 控制乘式左边的值，内层循环控制列；这里range中的a+1是为了能遍历到a，因为range不包含end值
        print(f"{b} x {a} = {a*b}",end = "\t")
    print("\n")
else:
    print("99乘法表打印完毕~")


# 练习:基于嵌套循环完成如下需求
# 需求1:根据输入的直角边的边长，打印等腰直角三角形
c = int(input("请输入直角边边长："))
for i in range(c):
    for j in range(i+1):
        print("*",end="\t")
    print("\t")
else:
    print(f"直角边为{c}的等腰直角三角形打印完毕~")

# 需求2:根据输入的数字，打印对应的数字金字塔
d = int(input("请输入数字金字塔的最大数字："))
for i in range(1,d+1):
    for j in range(1,i+1):
        print(f"{j}",end="\t")
    print("\n")
else:
    print(f"最大值为{d}的数字金字塔打印完毕~")

# 需求3:打印国际象棋棋盘(8x8)
for i in range(1,9):
    for j in range(1,9):
        if i % 2 != 0:      # 奇数行
            if j % 2 == 0:      # 奇数行先黑后白
                print("□",end="\t")
            else:
                print("■",end="\t")
        else:       # 偶数行
            if j % 2 == 0:      # 偶数行先白后黑
                print("■",end="\t")
            else:
                print("□",end="\t")
    print("\n")
else:
    print("8x8的国际象棋棋盘打印完毕~")




