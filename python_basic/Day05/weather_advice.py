"""
程序名称：weather_advice.py
作者：黄乐源
日期：2026-07-02
描述：掌握if-elif-else多分支与match模式匹配，模拟天气预警与科研方向匹配
"""

print("================= 任务 1：if-elif-else 多分支（遥感气象与外场数据采集建议） =================")
# 模拟输入当前的24小时累积降雨量（单位：mm），并根据气象级别给出无人机（UAV）外场作业建议
rainfall = float(input("请输入当前24小时累计降雨量（单位：mm）："))

# 严格注意区间从高到低的先后判定顺序（大范围/严格条件在前）
if rainfall >= 50:
    warning = "暴雨预警！"
    advice = "🔴 严禁任何无人机外场数据采集作业，注意防汛防涝！"
elif rainfall >=25 and rainfall < 50:
    warning = "大雨"
    advice = "🟡 天气恶劣，设备极易受损，建议取消野外光谱数据采集计划。"
elif rainfall >=10 and rainfall < 25:
    warning = "中雨"
    advice = "🔵 降雨明显，空气湿度过大，会干扰红外波段反射率，不建议作业。"
elif rainfall > 0:
    warning = "小雨"
    advice = "⚪ 局部有微量降水，如需作业请务必做好设备防水。"
else:
    warning = "晴朗无雨"
    advice = "🟢 气象条件良好，非常适合无人机外场遥感影像采集！"

print(f"当前气象评估结果：{warning}")
print(f"专家建议：{advice}")



print("\n================= 任务 2：Python 3.10+ 全新 match...case 语法（预研团队方向匹配） =================")
# 模拟匹配你即将要调研的华中师范大学城市与环境科学学院的导师科研方向
print("欢迎使用华中师范大学城市与环境科学学院导师研究方向查询系统！")
print("目前系统内剩余可选导师有：Liu（刘鹏程教授）、Zhou（周洋副教授）")
mentor = input("请选择你想查询的导师名称：")

# 使用全新的 match-case 语法替换繁琐的字符串相等判断
match mentor:
    case "Liu" | "liu" | "刘鹏程":
        print("查询成功！刘鹏程教授课题组")
        print("核心研究方向：地图制图综合、GeoAI")
    case "Zhou" | "zhou" | "周洋":
        print("查询成功！周洋副教授课题组")
        print("核心研究方向：请关注华中师范大学周洋副教授的教师主页中发布最新的研究成果。")
    case _:
        print("提示：输入了其他导师，建议开学后在华中师范大学城环学院官网或教师主页进一步查询。")
