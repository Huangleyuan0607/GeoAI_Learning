"""
程序名称：multiplication_table.py
作者：黄乐源
日期：2026-07-04
描述：掌握for循环、range()序列、双层循环嵌套以及break/continue控制流，实现九九乘法表与猜数字综合案例
"""
import random

# print("================= 任务 1：嵌套循环（双层 for 循环输出九九乘法表） =================")
# # 模拟 GIS 二维空间格网的行列扫描机制：外层循环控制行（Row），内层循环控制列（Column）
# for row in range(1,10):     # 行控制：从第 1 行到第 9 行
#     for col in range(1,row+1):      # 列控制：当前行的最大列数不超过当前行号
#         print(f"{col} x {row} = {row*col}",end="\t")
#     print("\n")      # 内层"列"循环一轮结束，执行换行，进入外层下一"行"扫描


print("\n================= 任务 2：循环中断控制综合实战（智能猜数字交互系统） =================")
# 融合随机数生成、条件分支、无限循环与 break 强行中断机制
# 生成随机数
random_num = random.randint(1,100)

print("🎮 --- 欢迎来到华中师范大学城市与环境科学学院 Python 基本功测试：猜数字系统 ---")
print("💡 系统已经随机生成了一个 1 到 100 之间的整数，请开始你的预测。")
print("💡 若要放弃游戏，请在输入数字界面输入quit或q，从而退出游戏。")
while True:
    # 获取用户输入的数字
    num = input("请输入一个数字：")

    # 控制输入值不可为空
    if num == "":
        print("输入的数字不可为空！")
        continue

    # 判断输入值是否为强行退出
    if num == "q" or num == "quit":
        print("游戏已终止！")
        break

    # 判断输入的数字与随机数的大小或正确
    if int(num) > random_num:
        print("您输入的数字太大了！")
    elif int(num) < random_num:
        print("您输入的数字太小了！")
    else:
        print(f"恭喜您回答正确！随机数为：{random_num}")
        break

print("🏁 任务结束：恭喜攻克循环结构全部核心知识点！")