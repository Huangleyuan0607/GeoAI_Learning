# 集合 set ---> 无序、不可重复、可修改
# 定义集合
# s1 = {5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}     # 使用大括号定义
#
# print(s1)
# print(type(s1))
#
# # 定义空集合
# s2 = set()
# print(s2)      # 空集合的输出就是set()
# print(type(s2))
#
#
# # 集合常见方法
# # add()：添加元素到集合
# s1 = {100, 200, 300, 400, 500, 600, 700, 800}
# print(s1)
#
# s1.add(1200)
# print(s1)
#
# # remove()：移除集合中的指定元素（指定元素不存在则报错）
# s1.remove(200)
# print(s1)
#
# # pop()：随机删除集合中的元素并返回
# e = s1.pop()
# print(e)
# print(s1)
#
# # clear()：清空集合
# s1.clear()
# print(s1)   # 空集合的输出是set()
#
# s2 = {"A", "B", "C", "D", "E", "X", "Y",}
# s3 = {"C", "E", "Y", "Z"}
# # difference()：求取两个集合的差集（包含在集合A但不包含在集合B的元素）
# print(s2.difference(s3))    # 求存在于s2但不存在于s3的元素
# print(s3.difference(s2))    # 求存在于s3但不存在于s2的元素
#
# # union()：求取两个集合的并集
# print(s2.union(s3))     # 对于求并集而言，两个集合的位置对结果没有影响
# print(s3.union(s2))
#
# # intersection()：求取两个集合的交集
# print(s2.intersection(s3))      # 对于求交集而言，两个集合的位置对结果没有影响
# print(s3.intersection(s2))


# 集合案例
# 案例1：根据提供的班级学生的选课情况，完成如下需求：
# 1.找出同时选修了法语和艺术的学生
# 2.找出同时选修了所有四门课程的学生
# 3.找出选修了足球，但是没有选修篮球的学生
# 4.统计每一个学生选修的课程数量

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1、找出同时选修了法语和艺术的学生
# 方法一：intersaction()
fa_set = french_set.intersection(art_set)     # 求取法语和艺术的交集
print("同时选修了法语和艺术的学生有：", fa_set)

# 方法二：&（与）运算符 --> 交集
fa_set2 = french_set & art_set
print("同时选修了法语和艺术的学生有：", fa_set2)

# 2、找出同时选修了所有四门课程的学生
# 方法一：intersaction()
every_set = football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)
print("同时选修了所有四门课程的学生有：", every_set)

# 方法二：& ---> 求交集
every_set2 = football_set & basketball_set & french_set & art_set
print("同时选修了所有四门课程的学生有：", every_set2)

# 3、找出选修了足球，但是没有选修篮球的学生
# 方法一：
fnb_set = football_set.difference(basketball_set)   # 存在于足球但不存在于篮球
print("选修了足球，但是没有选修篮球的学生有：", fnb_set)

# 方法二：-（减号） ---> 差集
fnb_set2 = football_set - basketball_set
print("选修了足球，但是没有选修篮球的学生有：", fnb_set2)

# 方式三：集合推导式 ---> 快速构建集合，语法：{要往集合中添加的元素 for s in set1 if 条件}
fnb_set3 = {s for s in football_set if s not in basketball_set}
print("选修了足球，但是没有选修篮球的学生有：", fnb_set3)

# 4、统计每一个学生选修的课程数量
# 获取全体学生名单
# 方法一：union()
# all_set = football_set.union(basketball_set).union(french_set).union(art_set)
# 方法二：| ---> 求并集
all_set = football_set | basketball_set | french_set | art_set
print(all_set)

# 获取每一次学生选修的课程数量
# 方法一：遍历判断
for s in all_set:
    count = 0
    if s in basketball_set:
        count += 1
    if s in french_set:
        count += 1
    if s in art_set:
        count += 1
    if s in football_set:
        count += 1
    print(f"{s}同学选修的课程数量为：{count}")

# 方法二：列表
all_list = [*football_set, *basketball_set, *french_set, *art_set]      # 解包操作
for s in all_list:
    print(f"{s}同学选修了{all_list.count(s)}门课程")
