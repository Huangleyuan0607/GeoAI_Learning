"""
程序名称：guess_number.py
作者：黄乐源
日期：2026-07-03
描述：掌握 while 循环语法，模拟深度学习 Loss 早期停止机制与编写猜数字游戏
"""
import random

print("================= 任务 1：while 循环应用（机器学习 Loss 早期停止机制模拟） =================")
# 模拟深度学习训练中，当 Loss（损失值）下降到指定阈值时停止迭代（Early Stopping）
current_loss = 2.5  # 初始损失值
target_loss = 0.3  # 目标停止阈值
epoch = 1  # 当前迭代轮次（Epoch）

print(f"🚀 开始训练模型... 初始 Loss: {current_loss}, 目标 Loss: {target_loss}")

# 当 Loss 高于目标值时，循环继续训练

while current_loss > target_loss:
    # 模拟每个 Epoch 训练后 Loss 逐渐下降（随机递减 0.2 ~ 0.5 之间的值）
    loss_drop = random.uniform(0.2, 0.5)
    current_loss -= loss_drop   #模拟每轮训练后loss值下降
    epoch += 1
    print(f"当前轮次：{epoch}，当前Loss：{current_loss:.4f}。")
else:
    # epoch-1才为迭代轮次，因为最后一次迭代后epoch加了1
    print(f"🎉训练完成！模型在第{epoch - 1}轮成功收敛，最终Loss:{current_loss:.4f}，触发 Early Stopping 机制。")

print("\n================= 任务 2：while 条件控制实战（智能猜数字游戏） =================")
# 结合 while 条件控制与随机数，实现游戏逻辑闭环
print("--- 欢迎来到数字密码破解游戏 ---")
print("系统已在 1-100 之间随机生成了一个目标地理要素编号，请尝试破解它！")

# 1. 系统自动生成 1-100 的随机数作为正确答案
num_boom = random.randint(1, 100)

# 2. 初始化用户的猜测次数和当前的猜测状态
guess_epoch = 1     # 用户猜测次数
condition = False   # 当前猜测状态

# 3. 使用 while 循环控制游戏，直到用户猜中才结束
while condition == False:
    guess_num = int(input(f"当前为第{guess_epoch}轮，请输入你的猜测："))
    if guess_num > num_boom:
        print(f"答案比{guess_num}小！")
        condition = False
    elif guess_num < num_boom:
        print(f"答案比{guess_num}大！")
        condition = False
    else:
        print(f"恭喜你答对啦！正确答案就是{num_boom}~")
        condition = True
    guess_epoch += 1
else:
    print(f"恭喜你用时{guess_epoch - 1}轮猜出结果！")