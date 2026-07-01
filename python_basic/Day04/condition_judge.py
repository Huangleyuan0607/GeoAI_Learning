"""
程序名称：condition_judge.py
作者：黄乐源
日期：2026-07-01
描述：攻克四大运算符与if基础判断，模拟初试成绩判定与遥感像元过滤
"""

print("================= 任务 1：算术与赋值运算符（遥感网格计算模拟） =================")
# 假设一张遥感影像总共有 1025 列，计划裁剪成每 256 列为一个格网图块
total_columns = 1025
tile_size = 256

tile_count = total_columns // tile_size     # 取整
remain_columns = total_columns % tile_size  # 取余

print(f"本遥感影像共有{total_columns}列，计划裁剪成每{tile_size}列为一个格网图块。")
print(f"整图可完整裁剪出{tile_count}个标准图块。")
print(f"剩余{remain_columns}列（即整图边缘部分）不足以构成一个完整图块。")

# 复合赋值运算：迭代器递增模拟
epoch_counter = 0
epoch_counter += 1
print(f"当前训练迭轮次累加至：{epoch_counter}")


print("\n================= 任务 2：比较、逻辑运算符与 if 判断（复试线判定） =================")
# 动态获取用户输入的统考成绩
print("欢迎进入华中师范大学城市与环境科学学院2026年研究生初试复试线审核系统！")
print("本系统适用于资源与环境专业型硕士考生。")
name = input("请输入考生姓名：")
politics_score = int(input("请输入您的思想政治理论分数："))   # 吸取Day03避坑经验：必须显式转换类型后才能进行数值大小比较
english2_score = int(input("请输入您的英语（二）分数："))
math2_score = int(input("请输入您的数学（二）分数："))
rs_score = int(input("请输入您的遥感原理及应用分数："))
total_score = politics_score + english2_score + math2_score + rs_score

# 设定模拟复试线
scoreline_100 = 35
scoreline_150 = 53
scoreline_total = 264

# 组合多条件判定：总分过线 且 单科过线
print(f"\n{name}同学，您的成绩如下：\n(101)思想政治理论：{politics_score}\n(204)英语（二）：{english2_score}\n(302)数学（二）：{math2_score}\n(858)遥感原理及应用：{rs_score}\n总分：{total_score}\n")
if total_score >= scoreline_total and politics_score >= scoreline_100 and english2_score >= scoreline_100 and math2_score >= scoreline_150 and rs_score >= scoreline_150:
    print(f"您的单科分数与总分均已达到复试线要求。恭喜您进入华中师范大学城市与环境科学学院2026年硕士研究生招生考试复试！")
    print("请提前整理好相关资格审查材料，于2026年3月27日（周五）上午9：30－11：30到华中师范大学城市与环境科学学院（10号楼南楼）一楼大厅提交资格审查材料。")
    print("具体复试日程与资格审查材料清单请参阅华中师范大学城市与环境科学学院官网发布的2026年硕士研究生招生复试录取工作细则。")
    print("祝您复试顺利！期待和您在桂子山相遇！")

# 基础 if 单独控制（未过线提示）
if total_score < scoreline_total:
    print("很遗憾，您的总分未达到复试线要求，建议查看调剂信息。")
    print("华中师范大学城市与环境科学学院资源与环境专业2026年研究生招生考试复试线：264。")
if politics_score < scoreline_100 or english2_score < scoreline_100 or math2_score < scoreline_150 or rs_score < scoreline_150:
    print("很遗憾，您的单科分数未达到A类考生工学单科分数线要求，建议查看官方单科线情况或查看调剂信息。")
    print("2026年硕士研究生招生考试A类考生工学单科分数线如下：")
    print("单科（满分=100）：35")
    print("单科（满分>100）：53")
