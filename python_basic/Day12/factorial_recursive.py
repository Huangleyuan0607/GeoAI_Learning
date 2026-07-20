# -*- coding: utf-8 -*-
"""
程序名称：factorial_recursive.py
作者：黄乐源
日期：2026-07-09
描述：掌握变量作用域、四种核心传参、函数作为参数传递及 lambda 表达式，模拟遥感超参数调优系统
"""

print("================= 任务 1：全局变量安全修改与不定长参数解构演练 =================")

# 声明一个全局计数器，用于记录华中师范大学城市与环境科学学院 GeoAI 模型调优的总迭代次数
total_runs = 0

def configure_training_pipeline(model_name, learning_rate=0.001, *args, **kwargs):
    """
    配置并模拟启动深度学习模型训练流水线

    参数:
    model_name (str): 模型名称
    learning_rate (float): 初始学习率，默认为 0.001
    *args: 不定长位置参数，用于接收额外附加选项
    **kwargs: 不定长关键字参数，用于接收动态超参数（如 batch_size, epochs）
    """
    # 声明并引入全局变量进行修改
    global total_runs
    total_runs += 1

    print(f"第{total_runs}次运行：配置{model_name}训练流水线...")
    print(f"基础参数 -> 初始学习率：{learning_rate}")

    # 检查是否有位置扩展参数 (args 会被自动包装成元组)
    if args:
        print("附加选项列表：",args)

    # 检查是否有关键字扩展参数 (kwargs 会被自动包装成字典)
    if kwargs:
        print("动态超数据集：",kwargs)
        for hyper_key, hyper_val in kwargs.items():
            print(f" - {hyper_key}: {hyper_val}")

# 1. 采用普通位置参数与默认参数调用
configure_training_pipeline("U-Net-Basic")

# 2. 采用关键字参数与位置+关键字不定长参数进行全能调用（模拟输入多维度训练配置）
configure_training_pipeline(
    "Geo-Transformer-V2",   # model_name (位置参数)
    0.005,      # learning_rate (覆盖默认值)
    "启用数据增强", "开启GPU加速",    # args (不定长位置参数，会被包装为元组)
    batch_size = 32,    # kwargs (以下均为不定长关键字参数，会被包装为字典)
    epochs = 150,
    backbone = "ResNet-50",
    loss_function = "DiceLoss"
)

print("\n================= 任务 2：高阶函数调用与 lambda 表达式像元线性重映射 =================")

def apply_pixel_transformation(raw_value, transform_operator):
    """
    高阶函数：接收一个原始像元值，并调用传入的特定数学算子进行像素级重映射
    参数:
    raw_value (float): 原始遥感像元DN值/反射率
    transform_operator (function): 接收一个数值并返回变换后数值的算子函数 (高阶形参)
    """
    # 调用传入的函数对象执行核心数学计算
    transformed_value = transform_operator(raw_value)
    return transformed_value

# 场景：有一批野外建筑物提取中获取的多波段高分像元反射率，需要进行不同算子转换
raw_pixel = 128
print("原始探测区域像元值：",raw_pixel)

# 方案 A：利用 lambda 极简构建一个归一化算子： 将像元线性压缩至 [0, 1] 空间 (假设最大值为 255)
normalize_op = lambda x: x / 255
norm_pixel = apply_pixel_transformation(raw_pixel, normalize_op)
print(f"经过归一化算子变换[lambda x : x / 255] 结果：{norm_pixel:.4f}")

# 方案 B：就地编写一个复杂的非线性拉伸算子，直接送入高阶函数运行
enhance_pixel = apply_pixel_transformation(
    raw_pixel,
    lambda x : (x * 1.2) if x < 150 else (x * 0.8)
)
print(f"经过自适应增强算子[lambda x : (x * 1.2) if x < 150 else (x * 0.8)] 结果：{enhance_pixel:.2f}")

print("\n🏁 Day12 函数高级进阶实验全部跑通，GeoAI 动态超参配置及高阶变换算子部署成功！")