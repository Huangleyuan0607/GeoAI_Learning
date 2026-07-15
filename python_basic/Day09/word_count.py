"""
程序名称：word_count.py
作者：黄乐源
日期：2026-07-06
描述：全面攻克字符串高级方法与元组组包解包，实现学术论文摘要词频统计与地理空间锚点元数据安全接收
"""

print("================= 任务 1：字符串高级清洗方法全演练 =================")
# 模拟从遥感影像头文件中读取出的未经清洗的原始文本元数据
raw_geo_meta = "  🛰️Satellite: Sentinel-2A ; Sensor: MSI ; Level: L1C  \n"
print(f"原始未清洗字符串：'{raw_geo_meta}'")

# 1. strip() 剔除前后空白与换行
strip_meta = raw_geo_meta.strip()
print(f"1.剔除前后空白与换行后的字符串：‘{strip_meta}’")

# 2. replace() 替换无效字符
replace_meta = strip_meta.replace("🛰️", "")
print(f"2.替换无效字符后的字符串：'{replace_meta}'")

# 3. split() 将字符串切分为列表
split_meta = replace_meta.split(";")
print(f"3.split切分后的属性列表：'{split_meta}'")

# 4. join() 重新组装字符串
join_meta = "|".join(item for item in split_meta)
print(f"4.join重新规范组装后：{join_meta}")

print("\n================= 任务 2：元组的不变之美与变量组包解包演练 =================")
# 场景：记录华中师范大学城市与环境科学学院科研汇报地点的 WGS84 绝对地理坐标
# 地理坐标属于敏感基准数据，使用元组(Tuple)锁死防止后续程序中发生意外篡改
hall_coordinate = (114.3721, 30.5312, 45.2)  # (经度, 纬度, 高程)
print(f"华中师大城环学院空间锚点元组: {hall_coordinate}")
print(f"元组基本属性 -> 经度: {hall_coordinate[0]}, 数据总项数: {len(hall_coordinate)}")

# 尝试修改元组元素的值（在执行前已注释，因它会引发 TypeError）
# hall_coordinate[0] = 114.3800  # ❌ 报错提示：'tuple' object does not support item assignment

# 变量解包（Unpacking）实战演练：将元组内部元素一次性优雅分配给独立变量
longtitute, latitute, altitute = hall_coordinate
print(f"元组成功解包！经度：{longtitute}°E，纬度：{latitute}°N，高程：{altitute}m")

# 函数返回多个变量时的自动组包（Packing）机制模拟
def get_geoai_model_info():
    name = "Geo-Transformer-V2"
    backbone = "ResNet-50"
    accuracy = 0.942
    return name, backbone, accuracy    # 以元组组包形式返回值

model_tuple = get_geoai_model_info()
print(f"函数多变量返回自动组包结果，其类型为：{type(model_tuple)}，具体数据为：{model_tuple}")


print("\n================= 任务 3：多案例融合终极实战（遥感科研摘要词频统计系统） =================")
# 模拟刘鹏程老师发表的关于“基于Transformer的遥感建筑物提取”论文摘要片段
abstract_text = (
    "Transformer networks have achieved great success in remote sensing image interpretation. "
    "In this study, we propose an advanced Transformer architecture for building extraction from high-resolution images. "
    "The proposed building extraction network demonstrates superior performance in capturing global context information. "
    "Experimental results on public building datasets show that Transformer outperforms conventional CNN networks."
)
print("待分析的论文摘要片段：")
print(abstract_text)
print()

# 步骤1：数据粗清洗 —— 将文本全部转换为小写，保证单词统计不区分大小写
lower_text = abstract_text.lower()
print("将全部字母转换为小写后的论文摘要片段：")
print(lower_text)
print()

# 步骤2：数据细清洗 —— 去除文本中的标点符号（句号和逗号）
replace_text = lower_text.replace(",", "").replace(".", "")
print("去除文本中的标点符号（句号和逗号）后的论文摘要片段：")
print(replace_text)
print()

# 步骤3：分词操作 —— 使用 split() 将文章切分为单词列表
words_list = replace_text.split(" ")    # 使用空格作为分隔符切分
print(f"分词操作执行成功！当前单词列表数量：{len(words_list)}")

# 步骤4：高频词频统计与过滤（提取核心关注点，如 'transformer', 'building', 'sensing'）
key_words = ["transformer", "building", "sensing"]
print("华中师范大学城市与环境科学学院GeoAI高频科研词分析结果如下：")

for word in key_words:
    count = words_list.count(word)
    print(f"高频科研词：{word}在摘要片段中共出现{count}次。")
print()

print("Day09字符串方法与元组安全屏障全面构筑完毕，版本控制准备就绪！")