"""
程序名称：geo_sample_manager.py
作者：黄乐源
日期：2026-07-05
描述：全面攻克列表核心方法、切片语法与案例全串联，实现遥感科研样本的动态录入、清洗与统计
"""

print("================= 任务 1：列表核心方法全演练（多视频案例综合） =================")
# 初始化一个华师大城环学院遥感解译小组的初始名单
members = ["张三", "李四", "王五"]
print("小组初始成员：",members)

# 1. 动态增加：append 末尾追加，insert 指定位置插入
member1 = input("请输入新增组员1名称：")
members.append(member1)
member2 = input("请输入新增组员2名称：")
members.insert(1,member2)
print(f"增添成员后组员名单 ({member2}加入索引1, {member1}加入末尾): {members}")

# 2. 批量合并：extend 引入外部合作团队
external_teams = ["周八", "武九"]
members.extend(external_teams)
print(f"合并外部团队后组员名单：{members}")

# 3. 动态删除：remove 按值删除，pop 按索引弹出
member3 = input("请输入因毕业而退出组员名称：")
member4 = int(input("请输入删除组员2索引号："))
members.remove(member3)
members.pop(member4)
print(f"毕业生{member3}退出后，当前团队成员: {members} (刚才弹出的成员是: {member4})")

# 4. 检索与统计：index 找位置，count 计算出现次数
search_name = input("请输入查找的组员名称：")
if search_name in members:
    print(f"查询到{search_name}同学仍在研究小组内，其索引号为{members.index(search_name)}")
print(f"查询到团队中名为{search_name}的成员数量为: {members.count(search_name)}")

print("\n================= 任务 2：高频切片与空间降采样抽样模拟 =================")
# 模拟一段长序列的空间栅格像元点或者样点编号
spatial_samples = ["Grid_01", "Grid_02", "Grid_03", "Grid_04", "Grid_05", "Grid_06", "Grid_07", "Grid_08"]
print("原始格网样点序列：",spatial_samples)

# 左右闭开切片
sub_samples = spatial_samples[1:5]
print(f"切片 [1:5] 截取中间段（获取第2-5个）: {sub_samples}")

# 步长抽样（模拟遥感影像分辨率降采样，每隔一个像元抽样一次）
down_sampled = spatial_samples[::2]
print("步长为2降采样抽样 [::2]：", down_sampled)

# 逆序反转
reverse_sample = spatial_samples[::-1]
# 也可以在原列表上直接反转 --> spatial_samples.reverse()
print("利用切片实现序列完全反转[::-1]：", reverse_sample)


print("\n================= 任务 3：多案例融合终极实战（遥感解译样点数据清洗系统） =================")
# 场景：模拟从野外采集回来的建筑物、水体等遥感解译样本的置信度评分（0-100分）
# 目标：通过循环录入，剔除不合格样本，最终利用列表内置函数算出样本优质率和平均分
sample_scores = []
print("🛰️ 欢迎进入刘鹏程老师课题组：地物解译样本质量动态审计中心")
print("💡 提示：请输入每批次遥感样点的置信度得分（0-100），输入 -1 结束录入。")

while True:
   input_score = float(input("请输入样本置信度得分："))

   # 当输入值为-1时停止录入
   if input_score == -1:
       print("结束录入")
       break
   # 当输入值在0-100之间时视为有效数据，记录并存入列表
   elif 0 <= input_score <= 100:
       sample_scores.append(input_score)
       print(f"✅ 样点成功记录，当前已捕获样本数: {len(sample_scores)}")
   # 当输入值不在0-100之间时视为无效数据，重新输入
   else:
       print("⚠️ 异常：置信度必须在0到100之间，请重新检查数据！")

# 综合数据处理（融合案例3思维）
if len(sample_scores) > 0:      # 当收集到有效数据时
    # 计算需要输出的各种数值
    max_score = max(sample_scores)
    min_score = min(sample_scores)
    avg_score = sum(sample_scores) / len(sample_scores)

    # 过滤出置信度优秀（>=85分）的科研核心样点
    excellent_samples = []
    for score in sample_scores:
        if score >= 85:
            excellent_samples.append(score)

    print("\n--- 📊 华师大资环学院 GeoAI 样本审计汇报 ---")
    print(f"1. 成功捕获样点总数: {len(sample_scores)} 个")
    print(f"2. 样点最高置信度: {max_score:.2f} | 最低置信度: {min_score:.2f}")
    print(f"3. 整体样本平均置信度: {avg_score:.2f}")
    print(f"4. 置信度优秀样点集(>=85): {excellent_samples}")
    print(f"5. 科研核心优质样本占比: {(len(excellent_samples) / len(sample_scores)) * 100:.1f}%")
else:
    print("❌ 审计中心未检测到有效的样本输入，算法终止。")

print("\n🏁 Day08 列表核心案例全攻克，版本控制准备就绪！")