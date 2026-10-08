# 《GeoAI预研60天学习计划 V4.0》

## 每日具体任务安排表

> **计划版本说明（V4.0 · 方案A修订，2026.08.08）**
>
> **更正（2026.09.30）**：导师口头澄清，GAN 先修要补的是 **C-GAN 与流模型**，不是 CycleGAN。Day49—52 与第六阶段（Day68—73）正文已按新口径改写；本计划自 2026.09.29 起暂停（转入《GeoIRL 论文复现 30 天计划》），改写仅为口径正确，供 11 月回归时使用。以下 08.08 修订说明保留存档。
>
> 因导师要求“**尽快学习 GAN**”，经沟通确认采用方案A：将原第五阶段 GAN 专题的**原理部分整体提前**为一周先修阶段，主体计划顺延，现修订如下：
>
> - **Day01—Day45**：Python → PyTorch → CNN → 制图综合理论，编号与内容不变。
> - **Day46—Day52**：**新增第四阶段「GAN 基础专题（先修）」**：GAN 原理与最简 GAN 实战、CycleGAN 无配对图像翻译原理（原 Day61—Day62 内容前移并扩充）。
> - **Day53—Day67**：原第四阶段「地图制图综合与 Transformer 入门」（语义分割 / U-Net / Transformer / 导师论文）整体顺延 +7 天，内容不变。
> - **Day68—Day73**：原第五阶段改为第六阶段「**GAN 项目实战与文献调研**」：CycleGAN / starGAN 开源项目实战、图像补全、GAN×制图综合文献调研与专题总结。
> - **Day74（选学）**：GAN 图像超分辨率。
>
> 即：**实际学习周期为 Day01—Day73（73 天），选学上限 Day74。**


------

## 第一阶段：Python基础与数据分析入门

### 时间：2026.06.28—2026.07.12

### 阶段目标

- 熟悉Python开发环境
- 掌握Python核心语法
- 掌握常见数据结构
- 掌握函数与模块开发
- 掌握面向对象编程基础
- 建立GitHub学习仓库
- 形成每日Commit习惯

------

# Day01（2026.06.28）

## 今日目标

完成Python环境搭建，正式开启GeoAI学习计划。

## 今日任务

### 视频学习

#### 黑马Python

- - [x] 01 Python+AI课程导学
- - [x] 02 Python启航-初识Python
- - [x] 03 Python安装
- - [x] 04 Python程序初体验
- - [x] 05 常见问题解决方案
- - [x] 06 PyCharm安装

预计时长：2小时

### 理论学习

- Python应用场景
- GeoAI中的Python生态
- Python开发环境组成

### 代码实验

- 安装Python
- 安装PyCharm
- 配置解释器
- 创建第一个项目

文件：

```python
hello_geoai.py
print("Hello GeoAI")
```

### 输出成果

- 环境配置截图
- hello_geoai.py

### GitHub提交

- 注册GitHub账号
- 创建GeoAI-Learning仓库

```bash
git commit -m "init: GeoAI learning journey"
```

## 今日成果验收

- - [x] Python安装完成
- - [x] PyCharm安装完成
- - [x] 成功运行程序
- - [x] GitHub仓库建立

------

# Day02（2026.06.29）

## 今日目标

掌握变量与数据类型。

## 今日任务

### 视频学习

- - [x] 07 入门程序
- - [x] 08 入门程序剖析
- - [x] 09 字面量
- - [x] 10 变量
- - [x] 11 标识符
- - [x] 12 变量交换
- - [x] 13 数据类型

预计时长：2小时

### 理论学习

-  int
-  float
-  str
-  bool

### 代码实验

创建：

```python
variables_demo.py
```

实现：

-  用户输入姓名
-  用户输入年龄
-  输出个人信息

### GitHub提交

```bash
git commit -m "feat: variable and datatype"
```

## 今日成果验收

- - [x] 掌握变量定义
- - [x] 理解数据类型
- - [x] 完成实验代码

------

# Day03（2026.06.30）

## 今日目标

掌握字符串与输入输出。

## 今日任务

### 视频学习

- - [x] 14 字符串定义
- - [x] 15 字符串拼接
- - [x] 16 字符串格式化
- - [x] 17 输入与输出

预计时长：2小时

### 理论学习

-  f-string
-  format
-  input函数

### 代码实验

```python
student_info.py
```

实现：

-  输入姓名
-  输入专业
-  输出格式化介绍

### GitHub提交

```bash
git commit -m "feat: string and io"
```

------

# Day04（2026.07.01）

## 今日目标

掌握运算符与条件判断。

## 今日任务

### 视频学习

- - [x] 18 算术运算符
- - [x] 19 赋值运算符
- - [x] 20 比较运算符
- - [x] 21 逻辑运算符
- - [x] 22 if基础语法
- - [x] 23 if案例

预计时长：2.5小时

### 代码实验

```python
grade_judge.py
```

实现：

-  输入成绩
-  输出等级

### GitHub提交

```bash
git commit -m "feat: operator and if"
```

------

# Day05（2026.07.02）

## 今日目标

掌握多分支判断。

## 今日任务

### 视频学习

- - [x] 24 if...else
- - [x] 25 if...elif...else
- - [x] 26 综合案例
- - [x] 27 match模式匹配

预计时长：2.5小时

### 代码实验

```python
weather_advice.py
```

实现：

-  根据天气给出建议

### GitHub提交

```bash
git commit -m "feat: conditional logic"
```

------

# Day06（2026.07.03）

## 今日目标

掌握while循环。

## 今日任务

### 视频学习

- - [x]  28 while循环
- - [x] 29 while案例

预计时长：2.5小时

### 代码实验

```python
guess_number.py
```

实现：

-  猜数字游戏

### GitHub提交

```bash
git commit -m "feat: while loop"
```

------

# Day07（2026.07.04）

## 今日目标

掌握for循环。

## 今日任务

### 视频学习

- - [x] 30 for循环
- - [x] 31 range案例
- - [x] 32 嵌套循环
- - [x] 33 嵌套循环案例
- - [x] 34 break continue
- - [x] 35 猜数字综合案例

预计时长：2.5小时

### 代码实验

```python
multiplication_table.py
```

实现：

-  九九乘法表

### GitHub提交

```bash
git commit -m "feat: for loop"
```

------

# Day08（2026.07.05）

## 今日目标

掌握列表操作。

## 今日任务

### 视频学习

- - [x] 36 数据容器概述
- - [x] 37 列表介绍
- - [x] 38 列表切片
- - [x] 39 列表方法
- - [x] 40 列表案例1
- - [x] 41 列表案例2
- - [x] 42 列表案例3

预计时长：3小时

### 代码实验

```python
geo_sample_manager.py
```

实现：

-  优秀样点的提取筛选
-  比例计算输出

### GitHub提交

```bash
git commit -m "feat: list basic"
```

------

# Day09（2026.07.06）

## 今日目标

掌握字符串高级操作与元组。

## 今日任务

### 视频学习

- - [x] 43 字符串操作
- - [x] 44 字符串方法
- - [x] 45 字符串案例
- - [x] 46 元组基础
- - [x] 47 组包与解包
- - [x] 48 元组案例
- - [x] 49 元组案例优化

预计时长：2.5小时

### 代码实验

```python
word_count.py
```

实现：

-  文本词频统计

### GitHub提交

```bash
git commit -m "feat: tuple and string"
```

# Day10（2026.07.07）

## 今日目标

掌握集合与字典。

## 今日任务

### 视频学习

- - [x] 50 集合基础
- - [x] 51 集合案例
- - [x] 52 字典介绍
- - [x] 53 字典操作
- - [x] 54 字典案例
- - [x] 55 字典案例测试
- - [x] 56 数据容器总结

预计时长：3小时

### 代码实验

```python
word_frequency.py
```

### GitHub提交

```bash
git commit -m "feat: set and dict"
```

------

# Day11（2026.07.08）

> 暑期助教开始（晚间学习）

## 今日目标

掌握函数基础。

## 今日任务

### 视频学习

- - [x] 57 函数介绍
- - [x] 58 函数定义
- - [x] 59 参数与返回值
- - [x] 60 函数说明文档
- - [x] 61 函数嵌套
- - [x] 62 函数案例

预计时长：2.5小时

### 代码实验

```python
calculator_function.py
```

### GitHub提交

```bash
git commit -m "feat: function basic"
```

------

# Day12（2026.07.09）

## 今日目标

掌握函数进阶。

## 今日任务

### 视频学习

- - [x] 63 变量作用域
- - [x] 64 传参方式
- - [x] 65 默认参数
- - [x] 66 不定长参数
- - [x] 67 函数作为参数
- - [x] 68 lambda表达式

预计时长：3小时

### 代码实验

```python
factorial_recursive.py
```

### GitHub提交

```bash
git commit -m "feat: advanced function"
```

------

# Day13（2026.07.10）

## 今日目标

掌握递归与模块。

## 今日任务

### 视频学习

- - [x] 69 递归
- - [x] 70 案例2
- - [x] 71 类型注解
- - [x] 72 函数类型注解
- - [x] 73 模块介绍
- - [x] 74 导入模块
- - [x] 75 自定义模块
- - [x] 76 包

预计时长：2小时

### 代码实验

创建：

```python
utils/
```

### GitHub提交

```bash
git commit -m "feat: module and package"
```

------

# Day14（2026.07.11）

## 今日目标

掌握面向对象基础。

## 今日任务

### 视频学习

- - [x] 77 类与对象
- - [x] 78 类与对象（进阶）
- - [x] 79 实例方法
- - [x] 80 魔法方法
- - [x] 81 类属性

预计时长：2小时

### 代码实验

```python
student_class.py
```

实现：

-  Student类
-  成员属性
-  成员方法

### GitHub提交

```bash
git commit -m "feat: oop basic"
```

------

# Day15（2026.07.12）

## 今日目标

完成Python基础阶段总结。

## 今日任务

### 视频学习

- - [x] 82 教务系统案例准备
- - [x] 83 添加学生信息
- - [x] 84 修改删除查询
- - [x] 85 运行测试
- - [x] 86 异常处理
- - [x] 87 异常案例

预计时长：2.5小时

### 阶段总结

整理：

-  Python语法
-  数据结构
-  函数
-  模块
-  面向对象

### 输出成果

```text
Week1_Python_Summary.md
```

### GitHub提交

```bash
git commit -m "summary: python foundation stage"
```

# Day1-Day15阶段验收（7月12日晚）

你应该达到：

-  熟练掌握Python基础语法
-  理解函数与模块
-  掌握面向对象基础
-  熟悉Git与GitHub操作
-  安装好PyTorch环境
-  掌握Pandas基础分析
-  GitHub累计提交 ≥ 15次
-  完成Python_Basic目录全部代码

### 阶段成果仓库结构

```text
GeoAI-Learning
├── Python_Basic
│   ├── Day01
│   ├── Day02
│   ├── Day03
│   ├── Day04
│   ├── Day05
│   ├── Day06
│   ├── Day07
│   ├── Day08
│   ├── Day09
│   ├── Day10
│   ├── Day11
│   ├── Day12
│   ├── Day13
│   ├── Day14
│   └── Day15
├── Notes
│   ├── Day01（2026.06.28）Note.md
│   ├── Day02（2026.06.29）Note.md
│   ├── Day03（2026.06.30）Note.md
│   ├── Day04（2026.07.01）Note.md
│   ├── Day05（2026.07.02）Note.md
│   ├── Day06（2026.07.03）Note.md
│   ├── Day07（2026.07.04）Note.md
│   ├── Day08（2026.07.05）Note.md
│   ├── Day09（2026.07.06）Note.md
│   ├── Day10（2026.07.07）Note.md
│   ├── Day11（2026.07.08）Note.md
│   ├── Day12（2026.07.09）Note.md
│   ├── Day13（2026.07.10）Note.md
│   ├── Day14（2026.07.11）Note.md
│   └── Day15（2026.07.12）Note.md
└── README.md
```

下一阶段（Day16-Day30）将正式进入：

- NumPy与张量运算
- 自动求导
- Dataset/DataLoader
- 线性回归
- Softmax
- MLP
- MNIST实战
- 第一个真正的深度学习项目。

------

## 第二阶段：深度学习基础入门（Day16-Day30）

### 时间：2026.07.13—2026.07.27

### 阶段目标

> 本阶段主要完成从Python科学计算到深度学习框架的过渡，掌握PyTorch基础使用方法，并理解深度学习模型训练的核心原理。
>
> 本阶段主要目标如下：
>
> 完成NumPy基础操作，掌握矩阵运算与科学计算基础；
>
> 掌握PyTorch张量(Tensor)创建、运算及GPU加速方法；
>
> 理解自动求导机制，掌握梯度下降与反向传播基本原理；
>
> 掌握Dataset与DataLoader数据加载流程；
>
> 理解线性回归模型建立、损失函数与优化过程；
>
> 理解Softmax分类模型及交叉熵损失函数；
>
> 掌握MLP多层感知机结构，理解神经网络前向传播与参数更新过程；
>
> 完成MNIST手写数字识别项目，熟悉完整深度学习训练流程；
>
> 为后续CNN图像处理与地理空间数据（地图要素）深度学习任务学习奠定基础。

# Day16（2026.07.13）

## 今日目标

掌握NumPy数组创建与基本操作，理解Tensor与NumPy数组之间的联系。

## 今日任务

### 视频学习

#### 黑马Python数据分析

- - [x] Numpy入门-15 Numpy_属性介绍
- - [x] Numpy入门-16 Numpy_创建ndarray对象

#### 李沐《动手学深度学习》

- - [x] 第6讲 数据操作
- - [x] 第7讲 数据操作实现
- - [x] 第8讲 数据预处理实现

预计时长：3小时

### 理论学习

- NumPy数组
- ndarray对象
- Tensor与NumPy转换
- 数据预处理

### 代码实验

创建：

```
numpy_array_demo.py
```

实现：

- 创建NumPy数组
- 数组索引与切片
- Tensor与NumPy相互转换
- 数据预处理练习

### GitHub提交

```
git add .
git commit -m "Day16：完成NumPy数组基础学习"
git push
```

------

# Day17（2026.07.14）

## 今日目标

掌握NumPy矩阵计算与线性代数基础。

## 今日任务

### 视频学习

#### 黑马Python数据分析

- - [x] Pandas基础-01 numpy_类型转换
- - [x] Pandas基础-02 numpy_创建等比和等差数列
- - [x] Pandas基础-03 numpy_基本函数
- - [x] Pandas基础-06 numpy_矩阵运算

#### 李沐《动手学深度学习》

- - [x] 第10讲 线性代数
- - [x] 第11讲 线性代数实现
- - [x] 第12讲 按特定轴求和
- - [x] 第14讲 矩阵计算

预计时长：3小时

### 理论学习

- 向量
- 矩阵
- 广播机制
- 矩阵乘法
- 范数

### 代码实验

创建：

```
numpy_linear_algebra.py
```

实现：

- NumPy矩阵运算
- 广播计算
- 向量点积
- 矩阵乘法

### GitHub提交

```
git add .
git commit -m "Day17：完成NumPy矩阵计算学习"
git push
```

------

# Day18（2026.07.15）

## 今日目标

建立深度学习整体认知，了解深度学习发展历程与常见模型，掌握PyTorch框架基础以及Tensor基本创建方法。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

- - [x] 深度学习与神经网络课程导学
- - [x] Day01-01 深度学习_知识框架介绍
- - [x] Day01-02 深度学习_简介
- - [x] Day01-03 深度学习_特点
- - [x] Day01-04 深度学习_常用模型介绍
- - [x] Day01-05 深度学习_应用场景介绍
- - [x] Day01-06 深度学习_发展史介绍
- - [x] Day01-07 PyTorch_框架简介
- - [x] Day01-08 PyTorch_张量基本创建方式

预计时长：3小时

### 理论学习

- 深度学习基本概念
- 深度学习发展历程
- 常见深度学习模型：
  - ANN
  - CNN
  - RNN
  - Transformer
- PyTorch框架组成
- Tensor基本概念
- Tensor与NumPy数组区别

### 代码实验

创建：

```
tensor_create.py
```

实现：

- 创建Tensor对象
- 创建随机Tensor
- 创建全0、全1Tensor
- 查看Tensor属性

示例：

```
import torch

x = torch.tensor([1,2,3])

print(x)
print(x.shape)
print(x.dtype)
```

### GitHub提交

```
git add .
git commit -m "Day18：完成PyTorch框架与Tensor创建学习"
git push
```

------

# Day19（2026.07.16）

## 今日目标

掌握PyTorch Tensor常用创建方式、数据类型转换以及Tensor与NumPy之间的数据转换。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

- - [x] Day01-09 PyTorch_创建全0 / 1指定值张量
- - [x] Day01-09 PyTorch_创建线性和随机张量
- - [x] Day01-10 PyTorch_元素类型转换
- - [x] Day01-11 PyTorch_创建张量方式总结
- - [x] Day02-02 张量和Numpy之间相互转换

预计时长：3小时

### 理论学习

- Tensor数据类型
- Tensor与NumPy关系
- CPU Tensor与GPU Tensor区别
- dtype转换
- 数据存储方式

### 代码实验

创建：

```
tensor_numpy.py
```

实现：

- Tensor创建方式练习
- Tensor与NumPy相互转换
- 数据类型转换

练习：

```
import numpy as np
import torch

arr = np.array([1,2,3])

tensor = torch.tensor(arr)

print(tensor)
```

### GitHub提交

```
git add .
git commit -m "Day19：完成Tensor创建与NumPy转换学习"
git push
```

------

# Day20（2026.07.17）

## 今日目标

掌握PyTorch Tensor基础运算和维度变换操作，为后续神经网络模型输入输出处理打基础。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

- - [x] Day02-03 张量基本运算
- - [x] Day02-04 张量点乘和矩阵乘法
- - [x] Day02-05 张量的常用运算函数
- - [x] Day02-06 张量的索引操作（上）
- - [x] Day02-07 张量的索引操作（下）
- - [x] Day02-09 张量的形状操作_reshape函数
- - [x] Day02-10 张量的形状操作_unsqueeze和squeeze函数
- - [x] Day02-11 张量的形状操作_transpose和permute函数
- - [x] Day02-12 张量的形状操作_view和contiguous函数

预计时长：4小时

### 理论学习

- Tensor索引
- Tensor切片
- 矩阵乘法
- reshape
- squeeze
- unsqueeze
- transpose
- permute

重点理解：

地图栅格数据：

```
H × W × C
```

转换为：

```
C × H × W
```

的原因。

### 代码实验

创建：

```
tensor_shape.py
```

实现：

- Tensor索引操作
- reshape操作
- 维度增加与减少
- permute维度转换

### GitHub提交

```
git add .
git commit -m "Day20：完成Tensor运算与维度变换学习"
git push
```

------

# Day21（2026.07.18）

## 今日目标

理解深度学习自动求导机制，掌握梯度计算与参数更新基本流程。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

- - [x] Day02-13 张量的拼接操作
- - [x] Day02-14 自动微分模块_介绍
- - [x] Day02-15 自动微分模块案例_更新一次参数
- - [x] Day02-16 自动微分模块案例_循环更新参数
- - [x] Day03-01 自动微分小问题_detach函数
- - [x] Day03-02 自动微分真实应用场景

预计时长：3小时

### 理论学习

- 自动微分机制
- 梯度
- 反向传播基本思想
- 参数更新流程

理解：

```
Forward
 ↓
Loss
 ↓
Backward
 ↓
Gradient
 ↓
Update
```

### 代码实验

创建：

```
autograd.py
```

实现：

- requires_grad使用
- backward计算梯度
- detach操作

### GitHub提交

```
git add .
git commit -m "Day21：完成PyTorch自动求导学习"
git push
```

------

# Day22（2026.07.19）

## 今日目标

掌握PyTorch完整模型训练流程，通过线性回归理解深度学习训练基本框架。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day03-03 PyTorch模拟线性回归_准备数据集
-  - [x] Day03-04 PyTorch模拟线性回归_模型训练
-  - [x] Day03-05 PyTorch模拟线性回归_可视化操作

预计时长：3小时

### 理论学习

- Dataset数据准备
- 模型定义
- Forward计算
- Loss计算
- Backward反向传播
- Optimizer参数更新

### 代码实验

创建：

```
linear_regression.py
```

实现：

- 创建训练数据
- 构建线性模型
- 使用MSELoss
- 使用Adam优化器
- 绘制Loss变化曲线

### 输出成果

完成：

```
Linear Regression with PyTorch
```

项目。

### GitHub提交

```
git add .
git commit -m "Day22：完成PyTorch线性回归模型训练"
git push
```

------

# Day23（2026.07.20）

## 今日目标

理解神经网络基本结构，掌握PyTorch搭建简单神经网络的方法。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day03-06 如何构建神经网络(neural network)
-  - [x] Day03-07 神经网络_文字介绍
-  - [x] Day03-08 激活函数介绍
-  - [x] Day03-09 Sigmoid激活函数介绍
-  - [x] Day03-10 Tanh激活函数介绍

预计时长：3小时

### 理论学习

- 神经元
- 全连接层
- 网络结构
- 激活函数作用

掌握：

```
Input
 ↓
Linear
 ↓
Activation
 ↓
Output
```

### 代码实验

创建：

```
mlp_network.py
```

实现：

- 使用nn.Module创建网络
- 编写forward函数
- 完成简单MLP模型

### GitHub提交

```
git add .
git commit -m "Day23：完成神经网络结构与MLP搭建学习"
git push
```

------

# Day24（2026.07.21）

## 今日目标

掌握常用激活函数及分类任务中的输出方式，理解不同激活函数在神经网络中的作用。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day03-11 ReLU激活函数介绍
-  - [x] Day03-12 Softmax激活函数介绍
-  - [x] Day04-01 参数初始化_介绍
-  - [x] Day04-02 参数初始化_代码演示

预计时长：3小时

### 理论学习

- 激活函数作用
- Sigmoid函数
- Tanh函数
- ReLU函数
- Softmax分类概率
- 参数初始化方法

重点理解：

为什么神经网络需要非线性：

```text
Linear
 ↓
Activation
 ↓
Non-linear feature
```

### 代码实验

创建：

```id="2h7x8m"
activation_function.py
```

实现：

- 绘制Sigmoid、Tanh、ReLU函数曲线
- 使用Softmax输出分类概率
- 对比不同激活函数效果

### 输出成果

完成：

```text
Activation Function总结.md
```

记录：

- 函数公式
- 使用场景
- 优缺点

### GitHub提交

```bash
git add .
git commit -m "Day24：完成激活函数与参数初始化学习"
git push
```

------

# Day25（2026.07.22）

## 今日目标

掌握神经网络完整搭建流程，能够独立完成一个简单分类网络训练。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day04-03 神经网络_搭建流程介绍
-  - [x] Day04-04 神经网络_搭建代码实现
-  - [x] Day04-05 神经网络_模型训练
-  - [x] Day04-06 神经网络_总结

预计时长：3小时

### 理论学习

- nn.Module结构
- forward函数
- 网络参数管理
- 模型训练流程

掌握：

```python
model()
 ↓
loss()
 ↓
backward()
 ↓
optimizer.step()
```

### 代码实验

创建：

```id="0j7fpa"
mlp_classifier.py
```

实现：

- 构建MLP分类网络
- 加载数据
- 模型训练
- 测试准确率

### 输出成果

完成：

```text
MLP Classification Project
```

包括：

- 模型代码
- 训练结果
- Loss曲线

### GitHub提交

```bash
git add .
git commit -m "Day25：完成PyTorch MLP网络结构搭建"
git push
```

------

# Day26（2026.07.23）

## 今日目标

理解不同任务对应的损失函数，掌握分类和回归任务中的Loss使用方法。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day04-07 损失函数_多分类交叉熵损失介绍
-  - [x] Day04-08 损失函数_二分类交叉熵损失介绍
-  - [x] Day04-09 损失函数_MAE损失函数介绍
-  - [x] Day04-10 损失函数_MSE损失函数介绍
-  - [x] Day04-11 损失函数_Smooth L1损失函数介绍

预计时长：3小时

### 理论学习

- Loss函数作用
- 分类任务Loss
- 回归任务Loss
- CrossEntropyLoss
- MSELoss
- MAELoss
- SmoothL1Loss

结合地图制图任务理解：

| 任务             | Loss                   |
| ---------------- | ---------------------- |
| 地图要素分类     | CrossEntropyLoss       |
| 地图要素分割     | CrossEntropy/Dice Loss |
| 连续变量预测     | MSELoss                |

### 代码实验

创建：

```id="f8b0px"
loss_function.py
```

实现：

- 不同Loss函数计算
- 对比Loss变化
- 理解输入输出格式

### 输出成果

完成：

```text
Loss函数总结.md
```

内容：

- 公式
- 使用场景
- PyTorch API

### GitHub提交

```bash
git add .
git commit -m "Day26：完成深度学习损失函数学习"
git push
```

------

# Day27（2026.07.24）

## 今日目标

掌握常用优化算法和学习率调整策略，理解模型训练过程中的参数优化方法。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day04-12 梯度下降算法回顾
-  - [x] Day04-13 反向传播(了解)
-  - [x] Day05-01 梯度相关知识点回顾
-  - [x] Day05-02 指数移动加权平均介绍
-  - [x] Day05-03 梯度下降优化方法_动量法
-  - [x] Day05-04 梯度下降优化方法_AdaGrad
-  - [x] Day05-05 梯度下降优化方法_RMSProp
-  - [x] Day05-08 梯度下降优化方法_Adam
-  - [x] Day05-09 梯度下降优化方法_总结

预计时长：4小时

### 理论学习

- 梯度下降
- SGD
- Momentum
- AdaGrad
- RMSProp
- Adam

重点掌握：

Adam为什么成为深度学习常用优化器。

### 代码实验

创建：

```id="2x7w0v"
optimizer_compare.py
```

实现：

比较：

- SGD
- Adam

观察：

- Loss下降速度
- 收敛效果

### 输出成果

完成：

```text
Optimizer总结.md
```

记录：

- 优化器特点
- 使用场景

### GitHub提交

```bash
git add .
git commit -m "Day27：完成优化器与梯度下降学习"
git push
```

------

# Day28（2026.07.25）

## 今日目标

掌握模型训练中的常见优化技巧，理解过拟合问题及解决方法。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day05-10 学习率优化_背景介绍
-  - [x] Day05-11 学习率衰减策略_等间隔学习率衰减
-  - [x] Day05-12 学习率衰减策略_指定间隔学习率衰减
-  - [x] Day05-13 学习率衰减策略_指数间隔学习率衰减
-  - [x] Day05-15 正则化_dropout(随机失活)介绍
-  - [x] Day05-16 正则化_dropout(随机失活)代码演示
-  - [x] Day05-17 正则化_批量归一化(BN)介绍
-  - [x] Day05-18 正则化_批量归一化(BN)代码实现

预计时长：4小时

### 理论学习

- 过拟合
- 欠拟合
- 学习率调整
- Dropout
- BatchNorm

重点理解：

为什么地理/地图数据深度学习容易过拟合：

- 标注样本数量有限
- 地物与要素类型复杂
- 不同区域、不同尺度之间差异明显

### 代码实验

创建：

```id="o4e3li"
regularization.py
```

实现：

- Dropout网络
- BatchNorm网络
- 对比训练效果

### 输出成果

完成：

```text
模型优化方法总结.md
```

### GitHub提交

```bash
git add .
git commit -m "Day28：完成Dropout与BatchNorm学习"
git push
```

------

# Day29（2026.07.26）

## 今日目标

完成第一个完整神经网络项目，掌握从数据处理到模型测试的完整流程。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day05-19 ANN案例_手机价格分类-需求介绍
-  - [x] Day05-20 ANN案例_手机价格分类-准备数据集
-  - [x] Day06-01 ANN案例_手机价格分类-准备数据集(回顾)
-  - [x] Day06-02 ANN案例_手机价格分类-搭建神经网络
-  - [x] Day06-03 ANN案例_手机价格分类-模型训练
-  - [x] Day06-04 ANN案例_手机价格分类-模型测试
-  - [x] Day06-05 ANN案例_手机价格分类-调优思路

预计时长：5小时

### 理论学习

- 完整深度学习项目流程
- 数据加载
- 模型设计
- 训练验证
- 模型评价

### 代码实验

创建项目：

```text
ANN_phone_price_classification
```

完成：

- 数据读取
- 数据预处理
- ANN模型搭建
- 模型训练
- 测试评价

### 输出成果

GitHub项目：

```text
ANN Phone Price Classification
```

包含：

- README.md
- train.py
- model.py
- dataset.py

### GitHub提交

```bash
git add .
git commit -m "Day29：完成ANN分类项目"
git push
```

------

# Day30（2026.07.27）

## 今日目标

总结PyTorch与神经网络基础知识，整理深度学习训练代码模板，为CNN学习阶段做准备。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day06-06 图像相关知识介绍
-  - [x] Day06-07 上午内容回顾
-  - [ ] 复习Day01-Day06重点内容

预计时长：3小时

### 理论学习

整理：

- Tensor操作
- 自动求导
- 网络结构
- Loss函数
- Optimizer
- 模型训练流程

形成：

```text
PyTorch深度学习训练流程
```

### 代码实验

创建：

```text
pytorch_template
```

整理通用模板：

```
project
│
├── dataset.py
├── model.py
├── train.py
├── test.py
└── config.py
```

实现：

- 数据加载模板
- 模型定义模板
- 训练循环模板

### 输出成果

完成：

```text
PyTorch基础学习总结.md
```

内容包括：

- Tensor
- Autograd
- Neural Network
- Loss
- Optimizer
- Training Pipeline

### GitHub提交

```bash
git add .
git commit -m "Day30：完成PyTorch深度学习基础总结"
git push
```

------

# Day16-Day30阶段验收（2026.07.27 晚）

完成第二阶段后，你应该达到：

- ✅ 熟练掌握NumPy数组创建、索引、切片及矩阵基础运算
- ✅ 理解Tensor本质以及Tensor与NumPy数组之间的转换关系
- ✅ 掌握PyTorch Tensor常用操作（创建、运算、reshape、permute等）
- ✅ 理解自动求导（Autograd）机制以及梯度更新流程
- ✅ 理解深度学习模型训练基本流程

```
数据
 ↓
模型
 ↓
Loss
 ↓
Backward
 ↓
Optimizer
 ↓
参数更新
```

- ✅ 能够使用PyTorch完成简单数据加载与训练流程
- ✅ 掌握Dataset与DataLoader的基本使用方法
- ✅ 掌握线性回归模型的构建、训练与结果可视化
- ✅ 理解神经网络基本结构（输入层、隐藏层、输出层）
- ✅ 掌握PyTorch `nn.Module` 网络搭建方式
- ✅ 理解常用激活函数（Sigmoid、Tanh、ReLU、Softmax）
- ✅ 掌握常用损失函数（MSELoss、CrossEntropyLoss等）
- ✅ 掌握常用优化方法（SGD、Adam、学习率调整）
- ✅ 理解模型过拟合问题以及Dropout、BatchNorm等优化方法
- ✅ 能完成一个基于PyTorch的ANN分类项目
- ✅ GitHub累计提交 ≥ 30 次

------

# 第二阶段成果

完成Day30后，你的GitHub仓库应至少包含：

```
pytorch/
├── Day16/
├── Day17/
├── Day18/
├── Day19/
├── Day20/
├── Day21/
├── Day22/
├── Day23/
├── Day24/
├── Day25/
├── Day26/
├── Day27/
├── Day28/
├── Day29/
└── Day30/
```

并完成：

- NumPy数组与矩阵运算实验
- Tensor基础操作实验
- Tensor维度变换实验
- 自动求导实验
- PyTorch线性回归实验
- MLP神经网络搭建实验
- 激活函数实验
- Loss函数实验
- Optimizer优化实验
- Dropout与BatchNorm实验
- ANN分类综合项目
- PyTorch训练代码模板整理

------

# 当前能力等级（预计）

完成Day30后，你的水平大致相当于：

```
Python开发        ★★★★☆
Git/GitHub        ★★★★☆
NumPy             ★★★★☆
PyTorch           ★★★☆☆
深度学习理论      ★★★☆☆
计算机视觉基础    ★☆☆☆☆
CNN               ☆☆☆☆☆
Transformer       ☆☆☆☆☆
GeoAI             ☆☆☆☆☆
```

------

## 第三阶段：GeoAI核心基础（Day31-Day45）

### 时间：2026.07.28—2026.08.11

## 阶段目标

> 本阶段是进入GeoAI方向的重要阶段。
>
> 将从“深度学习基础”进一步进入“计算机视觉与地图智能综合基础”。
>
> 完成后应达到：
>
> - 理解CNN核心原理
> - 掌握卷积层、池化层、BatchNorm等基础模块
> - 理解LeNet、AlexNet、VGG、GoogLeNet、ResNet演化过程
> - 掌握PyTorch CNN模型搭建流程
> - 掌握图像增强方法
> - 掌握OpenCV基础图像处理操作
> - 理解CNN Backbone概念
> - 理解图像分类任务完整流程
> - 理解语义分割基本概念
> - 理解FCN网络思想
> - 为U-Net和地图建筑物要素提取与化简项目做好准备

# Day31（2026.07.28）

## 今日目标

进入计算机视觉方向学习，理解图像数据特点以及CNN解决图像任务的基本思想。

## 今日任务

### 视频学习

#### 黑马AI大模型《神经网络与深度学习》

-  - [x] Day06-08 CNN概述介绍
-  - [x] Day06-09 卷积层_计算规则介绍

#### 李沐《动手学深度学习》

-  - [x] 第63讲 从全连接到卷积
-  - [x] 第64讲 卷积层
-  - [x] 第65讲 代码

预计时长：4小时

### 理论学习

- 图像数据结构
- 图像通道
- 卷积神经网络发展背景
- CNN相比MLP的优势

重点理解：

为什么图像任务不用全连接：

```
图片
 ↓
局部感受野
 ↓
卷积
 ↓
特征提取
```

### 代码实验

创建：

```
conv_basic.py
```

实现：

- 使用PyTorch Conv2d
- 输入图片Tensor
- 查看卷积输出尺寸

### GitHub提交

```
git add .
git commit -m "Day31：开始CNN学习与卷积基础"
git push
```

------

# Day32（2026.07.29）

## 今日目标

掌握卷积层核心参数，理解卷积计算过程。

## 今日任务

### 视频学习

#### 黑马

-  - [x] Day06-10 卷积层_填充Padding介绍
-  - [x] Day06-11 卷积层_步长Stride介绍
-  - [x] Day06-12 卷积层_多通道卷积计算
-  - [x] Day06-13 卷积层_多卷积核卷积计算

#### 李沐

-  - [x] 第67讲 填充和步幅
-  - [x] 第70讲 多输入输出通道

预计时长：4小时

### 理论学习

掌握：

- kernel
- padding
- stride
- channel
- feature map

理解地图数据：

```
地图瓦片 / 建筑物矢量
        ↓
CNN特征提取
        ↓
要素分类与识别
```

### 代码实验

创建：

```
conv_parameter.py
```

实现：

- 不同kernel测试
- stride影响
- padding影响

### GitHub提交

```python
git add .
git commit -m "Day32：掌握CNN卷积参数"
git push
```

------

# Day33（2026.07.30）

## 今日目标

掌握池化层和CNN基本结构，能够搭建简单CNN网络。

## 今日任务

### 视频学习

#### 黑马

-  - [x] Day06-14 特征图计算规则
-  - [x] Day06-15 卷积层API介绍
-  - [x] Day06-16 池化层介绍
-  - [x] Day06-17 池化层API介绍

#### 李沐

-  - [x] 第73讲 池化层
-  - [x] 第76讲 LeNet

预计时长：4小时

### 理论学习

- 最大池化
- 平均池化
- CNN基本结构

```
Conv
 ↓
Activation
 ↓
Pooling
 ↓
FC
```

### 代码实验

创建：

```
simple_cnn.py
```

实现：

简单CNN：

```
Conv2d
ReLU
MaxPool
Linear
```

### GitHub提交

```
git add .
git commit -m "Day33：完成CNN基础网络搭建"
git push
```

------

# Day34（2026.07.31）

## 今日目标

完成第一个CNN图像分类项目，掌握完整视觉任务流程。

## 今日任务

### 视频学习

#### 黑马

-  - [x] Day07-02 CNN图像分类案例_准备数据集
-  - [x] Day07-03 CNN图像分类案例_搭建神经网络思路分析
-  - [x] Day07-04 CNN图像分类案例_代码实现
-  - [x] Day07-05 CNN图像分类案例_模型训练
-  - [x] Day07-06 CNN图像分类案例_模型测试
-  - [x] Day07-07 CNN图像分类案例_优化及总结

预计时长：4小时

### 理论学习

- 图像分类任务流程
- Dataset
- DataLoader
- CNN训练流程

### 代码实验

项目：

```
CNN_Image_Classification
```

实现：

- 数据加载
- CNN模型
- 训练
- 测试

### GitHub提交

```
git add .
git commit -m "Day34：完成CNN图像分类项目"
git push
```

------

# Day35（2026.08.01）

## Buffer Day：阶段总结

## 今日任务

### 理论复习

整理：

- - [x] CNN结构
- - [x] 卷积计算
- - [x] Feature Map
- - [x] Pooling

### 代码整理

优化：

```
CNN_Project
├── dataset.py
├── model.py
├── train.py
└── test.py
```

### 输出成果

完成：

```
CNN基础学习总结.md
```

### GitHub提交

```
git add .
git commit -m "Day35：CNN基础阶段总结"
git push
```

# Day36（2026.08.02）

## 今日目标

理解经典CNN模型的发展背景，掌握AlexNet网络结构及其对深度学习发展的影响。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第79讲 AlexNet
-  - [x] 第80讲 AlexNet代码实现

预计时长：3小时

### 理论学习

学习：

- LeNet局限
- AlexNet创新点

重点理解：

AlexNet相比LeNet：

| LeNet    | AlexNet   |
| -------- | --------- |
| 浅层网络 | 深层网络  |
| CPU训练  | GPU训练   |
| 小数据   | ImageNet  |
| 简单卷积 | 大规模CNN |

核心技术：

- ReLU激活函数
- Dropout
- GPU训练

### 代码实验

创建：

```
AlexNet.py
```

实现：

- 使用PyTorch搭建AlexNet
- 查看网络结构
- 输入随机图片测试forward

输出：

```
model(torch.randn(1,3,224,224))
```

### GitHub提交

```
git add .
git commit -m "Day36：完成AlexNet网络学习"
git push
```

------

# Day37（2026.08.03）

## 今日目标

理解VGG网络设计思想，掌握小卷积核堆叠构建深层网络的方法。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第82讲 VGG
-  - [x] 第83讲 VGG代码实现

预计时长：3小时

### 理论学习

理解：

VGG核心思想：

```
多个3×3卷积
       ↓
替代大卷积核
       ↓
增加网络深度
```

掌握：

- VGG16结构
- VGG19结构
- Block设计思想

### 代码实验

创建：

```
VGG.py
```

实现：

- VGG Block
- VGG网络搭建
- 参数量统计

### 输出成果

完成：

```
CNN经典网络结构.md
```

记录：

- LeNet
- AlexNet
- VGG

### GitHub提交

```
git add .
git commit -m "Day37：完成VGG网络学习"
git push
```

------

# Day38（2026.08.04）

## 今日目标

理解网络加深后的问题，掌握ResNet残差连接思想。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第94讲 ResNet
-  - [x] 第95讲 ResNet代码实现
-  - [x] 第97讲 ResNet梯度计算

预计时长：4小时

### 理论学习

重点：

为什么需要ResNet？

问题：

```
网络越来越深
   ↓
梯度消失
   ↓
训练困难
```

解决：

残差结构：

```
x
↓
Conv
↓
Conv
↓
+
↓
output
```

理解：

- Shortcut
- Residual Block
- Identity Mapping

### 代码实验

创建：

```
ResNet_Block.py
```

实现：

- Residual Block
- 简化ResNet

### GitHub提交

```
git add .
git commit -m "Day38：完成ResNet残差网络学习"
git push
```

------

# Day39（2026.08.05）

## 今日目标

掌握ResNet在PyTorch中的实现方式，理解CNN Backbone概念。

## 今日任务

### 视频学习

#### PyTorch官方模型阅读

-  - [x] torchvision.models.resnet

预计时长：4小时

### 理论学习

理解：

Backbone：

```
Input Image

↓

CNN Backbone

↓

Feature Map

↓

Task Head
```

例如：

分类：

```
ResNet
 ↓
FC
 ↓
Class
```

分割：

```
ResNet
 ↓
Decoder
 ↓
Mask
```

### 代码实验

创建：

```
backbone_test.py
```

实现：

调用：

```
torchvision.models.resnet50()
```

完成：

- 输出feature map
- 查看网络层

### GitHub提交

```
git add .
git commit -m "Day39：理解CNN Backbone结构"
git push
```

------

# Day40（2026.08.06）

## 今日目标

了解更多经典CNN模型，建立完整CNN发展路线。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第85讲 NIN
-  - [x] 第86讲 NIN代码
-  - [x] 第88讲 GoogLeNet
-  - [x] 第89讲 GoogLeNet代码

预计时长：3小时

### 理论学习

学习：

### NIN

思想：

增加网络表达能力：

```
MLP卷积层
+
CNN
```

### GoogLeNet

核心：

- Inception模块
- 多尺度特征

理解：

为什么地图需要多尺度表达：

```
建筑物
道路
河流

尺寸不同，且随比例尺变化取舍规则不同

大比例尺：要素详细表达
小比例尺：只保留主要要素，并进行化简、合并
```

### 代码实验

创建：

```
GoogLeNet.py
```

实现：

- 查看Inception结构
- 测试forward

### GitHub提交

```
git add .
git commit -m "Day40：完成GoogLeNet与NIN学习"
git push
```

------

# Day41（2026.08.07）

## 今日目标

掌握CNN训练优化方法，提升图像模型训练能力。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第91讲 批量归一化
-  - [x] 第92讲 BatchNorm代码

预计时长：3小时

### 理论学习

理解：

BatchNorm作用：

- 加速训练
- 稳定梯度
- 提升泛化能力

掌握：

训练阶段：

```
mean
variance
```

推理阶段：

```
running mean
running variance
```

### 代码实验

创建：

```
BatchNorm.py
```

实现：

比较：

- 有BN
- 无BN

### GitHub提交

```
git add .
git commit -m "Day41：完成BatchNorm学习"
git push
```

------

# Day42（2026.08.08）

## 今日目标

学习CNN模型训练技巧，为后续语义分割项目打基础。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [x] 第111讲 数据增广
-  - [x] 第112讲 数据增广代码

预计时长：3小时

### 理论学习

学习：

图像增强：

- 翻转
- 裁剪
- 旋转
- 颜色变化

地图/地理数据应用：

解决：

- 标注样本不足
- 不同季节、不同区域的地图风格差异
- 采集条件与符号化差异

### 代码实验

创建：

```
image_augmentation.py
```

实现：

使用：

```
torchvision.transforms
```

完成：

- RandomFlip
- RandomCrop
- Normalize

### GitHub提交

```
git add .
git commit -m "Day42：完成图像增强学习"
git push
```

------

# Day43（2026.08.09）

## 今日目标

完成CNN综合复习，能够独立阅读常见CNN项目代码。

## 今日任务

### 理论复习

整理：

```
CNN知识体系.md
```

包含：

- 卷积
- Padding
- Stride
- Pooling
- Backbone
- ResNet
- BatchNorm
- 数据增强

### 代码实验

创建：

```
CNN_template
```

结构：

```
CNN_Project
│
├── dataset.py
├── model.py
├── train.py
├── test.py
└── utils.py
```

### GitHub提交

```
git add .
git commit -m "Day43：完成CNN知识体系整理"
git push
```

------

# Day44（2026.08.10）

## 今日目标

建立地图制图综合的基础理论框架，了解深度学习（含GAN）在地图综合与多尺度表达中的应用。

## 今日任务

### 文献阅读

阅读：

- 地图制图综合深度学习论文1篇（建议从综述入手）

重点关注：

- 研究问题（哪类要素、哪类综合算子）
- 数据表示（矢量还是栅格）
- 网络结构
- 多尺度评价指标

### 理论学习

**第一部分：制图综合基础理论（本阶段先修知识）**

理解制图综合的基本概念：

```
大比例尺地图
        ↓
制图综合
        ↓
小比例尺地图
```

核心综合算子：

| 算子     | 作用                           |
| -------- | ------------------------------ |
| 选取     | 按重要性取舍要素，控制要素密度 |
| 化简     | 简化线状/面状要素的几何形状    |
| 合并     | 将邻近同类要素聚合为一个       |
| 典型化   | 用代表性要素表达成群的同类要素 |
| 位移     | 避免要素压盖，保持关系清晰     |
| 夸大     | 放大重要但过小的要素           |
| 分类分级 | 重新划分要素类别与等级         |

**第二部分：多尺度表达**

- 多尺度表达：同一区域在不同比例尺下的地图表达
- 尺度变换的关键：不仅尺寸变化，**符号系统与取舍规则也在变化**
- 这正是可以建模为“**跨域图像翻译**”问题的原因

**第三部分：评价指标**

常见指标：

- OA
- Kappa
- F1

多尺度专用指标（需额外关注）：

- 位置精度
- 形状相似度
- 拓扑一致性
- 要素数量与密度保持度

### 代码实验

创建：

```
map_generalization_CNN.py
```

尝试：

使用：

- 地图瓦片数据 或 建筑物矢量数据
- CNN分类 / 特征提取

### GitHub提交

```
git add .
git commit -m "Day44：完成制图综合理论与CNN应用探索"
git push
```

------

# Day45（2026.08.11）

## Buffer Day：CNN阶段验收

## 今日目标

总结CNN学习成果，为地图要素提取与多尺度表达阶段做准备。

## 阶段验收

完成后应该达到：

- ✅ 理解CNN基本原理
- ✅ 掌握卷积层、池化层
- ✅ 能搭建CNN分类网络
- ✅ 理解AlexNet、VGG、ResNet思想
- ✅ 理解Backbone概念
- ✅ 能阅读CNN项目代码
- ✅ 掌握图像增强方法
- ✅ 具备进入U-Net学习基础

## GitHub成果

仓库：

```
pytorch/
├── Day31/
├── Day32/
├── Day33/
├── Day34/
├── Day35/
├── Day36/
├── Day37/
├── Day38/
├── Day39/
├── Day40/
├── Day41/
├── Day42/
├── Day43/
├── Day44/
└── Day45/
```

提交：

```
git add .
git commit -m "Day45：完成CNN阶段学习总结"
git push
```

------

# 第三阶段验收

完成Day45后，应达到：

- ✅ 理解CNN基本原理
- ✅ 理解卷积运算过程
- ✅ 理解卷积核、Padding、Stride等核心参数
- ✅ 理解池化层作用
- ✅ 能解释CNN图像特征提取流程
- ✅ 熟悉LeNet网络结构
- ✅ 理解AlexNet网络设计思想
- ✅ 理解VGG网络结构特点
- ✅ 理解GoogLeNet Inception模块
- ✅ 理解ResNet残差连接机制
- ✅ 掌握PyTorch CNN模型搭建流程
- ✅ 完成CNN图像分类实验
- ✅ 完成数据增强实验
- ✅ 掌握OpenCV基础操作
- ✅ 理解CNN Backbone概念
- ✅ 理解语义分割基本任务
- ✅ 理解FCN基本思想
- ✅ GitHub累计提交 ≥ 45次

------

# 当前能力等级（预计）

```
Python开发        ★★★★☆
Git/GitHub        ★★★★☆
Pandas            ★★★☆☆
PyTorch           ★★★★☆
CNN               ★★★★☆
OpenCV            ★★☆☆☆
语义分割          ★☆☆☆☆
Transformer       ☆☆☆☆☆
GeoAI             ★☆☆☆☆
```

------

# 阶段成果仓库结构

```
GeoAI-Learning

├── CNN_Basic
│   ├── lenet.py
│   ├── alexnet_demo.py
│   ├── vgg_demo.py
│   ├── resnet_demo.py
│   └── augmentation_demo.py
│
├── Image_Classification
│   └── CNN_classification_project
│       ├── dataset.py
│       ├── model.py
│       ├── train.py
│       └── test.py
│
├── OpenCV
│   └── opencv_basic.py
│
├── Semantic_Segmentation
│   └── FCN.md
│
└── Notes
    ├── CNN发展史.md
    ├── CNN结构总结.md
    └── CNN阶段总结.md
```

------

# 阶段成果要求

完成Day45后，你应该拥有：

## 代码成果

- LeNet模型实现
- AlexNet结构复现
- VGG网络结构理解
- ResNet残差模块实现
- CNN图像分类项目
- 图像增强实验代码
- OpenCV基础处理代码

## 理论成果

完成：

```
CNN知识体系.md
```

包含：

- CNN发展历史
- 卷积原理
- Feature Map
- Padding
- Stride
- Pooling
- Backbone
- AlexNet
- VGG
- GoogLeNet
- ResNet

------

# 完成Day45后的能力定位

完成本阶段后，你已经具备：

> GIS专业背景学生进入GeoAI（地图智能综合）方向所需的计算机视觉基础能力。

能够：

- 阅读基础CNN模型代码
- 修改PyTorch视觉模型
- 理解地图数据深度学习基本流程
- 理解制图综合基础理论与多尺度表达概念
- 为后续地图要素提取、U-Net、建筑物化简研究做好准备

------

# 下一阶段 Day46-Day67

先用一周完成导师要求的 GAN 基础先修，再进入最贴近地图制图综合研究方向的阶段：

## 语义分割与地图多尺度表达

主要内容：

- GAN原理与最简GAN实战（Day46—Day52）
- FCN实现
- DeepLab系列
- U-Net网络
- Attention机制
- Massachusetts Buildings Dataset
- 地图建筑物要素提取与化简实践
- Transformer基础
- Self-Attention
- Vision Transformer
- 制图综合方向论文阅读与复现

路线：

```
CNN基础
    ↓
GAN基础
    ↓
语义分割
    ↓
FCN
    ↓
U-Net
    ↓
地图要素提取与化简
    ↓
Transformer
    ↓
地图多尺度表达应用
```

------

# 第四阶段：GAN基础专题·先修（Day46-Day52）

### 时间：2026.08.12—2026.08.18

## 阶段目标

> 本阶段按导师要求**提前学习 GAN**（原第五阶段的前半部分前移）。
>
> 从“判别式模型”进入“生成式模型”，本阶段先解决**原理与最简实战**，开源项目实战与文献调研保留在第六阶段（Day68—Day73）完成。
>
> 完成后应达到：
>
> - 理解生成器与判别器的对抗训练机制
> - 掌握 GAN 损失函数与训练不稳定的成因
> - 独立完成最简 GAN（MNIST）实战
> - 理解 C-GAN 的**条件生成**思想（标签进 G 与 D 的两处位置）与流模型的**变量替换公式**（导师 09.30 更正，原 CycleGAN 取消）
> - 能说明 GAN 与地图制图综合的结合点

## 视频资源

```
GAN对抗生成网络
```

> **观看范围说明**：
>
> - **本阶段**：第一章全部（GAN原理与最简实战）；C-GAN 与流模型黑马课程没有对应章节，按 Day49—51 所列单集看
> - **留给第六阶段（选看）**：第二章（CycleGAN）、第三章（starGAN架构）、第四章（starGAN实战）、第八章（图像补全）——09.30 更正后不再是先修，多域翻译与图像补全对制图综合仍是好参照，回归主线有余力再看
> - **跳过**：第五章（除 5、6 两节）、第六章（变声器项目，与地图方向无关）
> - **选学**：第七章（图像超分辨率，Day74）

------

# Day46（2026.08.12）

## 今日目标

理解GAN的基本原理，掌握生成器与判别器的对抗机制。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第一章 1-对抗生成网络通俗解释
-  - [ ] 第一章 2-GAN网络组成
-  - [ ] 第一章 3-损失函数解释说明

预计时长：1小时

------

### 理论学习

理解：

GAN核心机制：

```
随机噪声
    ↓
生成器 G
    ↓
生成样本
    ↓
判别器 D
    ↓
真 / 假
```

重点理解：

- 生成器与判别器的博弈关系
- minimax 目标函数
- 损失函数与 JS 散度的关系

------

### 代码实验

创建：

```
gan_mnist/gan_data.py
```

实现：

- GAN 项目环境配置
- MNIST 数据读取模块（DataLoader，reshape 为 784 维向量）

------

### GitHub提交

```
git add .
git commit -m "Day46：完成GAN基本原理学习"
git push
```

------

# Day47（2026.08.13）

## 今日目标

掌握生成器与判别器的网络定义，完成最简GAN的代码搭建。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第一章 4-数据读取模块
-  - [ ] 第一章 5-生成与判别网络定义

预计时长：1小时

------

### 理论学习

理解：

- 生成器：噪声向量 → 全连接 → 784 维图像（输出层 Sigmoid）
- 判别器：图像向量 → 全连接 → 真/假概率（输出层 Sigmoid）
- 两个优化器**交替更新**的训练循环

------

### 代码实验

创建：

```
gan_mnist/mnist_gan.py
```

实现：

- 生成器 G 与判别器 D 定义
- 对抗训练循环骨架（先跑通 1 个 epoch）

------

### GitHub提交

```
git add .
git commit -m "Day47：完成最简GAN网络搭建"
git push
```

------

# Day48（2026.08.14）

## 今日目标

完成最简GAN完整训练，观察并分析GAN的训练不稳定问题。

## 今日任务

### 视频学习

#### 复习与自由调试

重听第一章 3-损失函数，对照训练日志理解 D/G loss 曲线含义。

预计时长：0.5小时

------

### 理论学习

重点理解：

- **训练不稳定与模式崩塌（mode collapse）**
- D loss 与 G loss 此消彼长的读法
- 常用稳定技巧：较小学习率、Adam(β1=0.5)、真实标签软标签（label smoothing）、平衡 G/D 训练步数

------

### 代码实验

完善：

```
gan_mnist/mnist_gan.py
```

实现：

- 完整训练 50+ epoch，定期保存生成样例（epoch 1 / 10 / 50 对比）
- 调参实验至少 2 组，记录现象

输出：

```
GAN训练问题记录.md
```

------

### GitHub提交

```
git add .
git commit -m "Day48：完成最简GAN实战与训练问题分析"
git push
```

------

# Day49（2026.08.15）

## 今日目标

理解C-GAN的条件生成思想，掌握标签进入G与D的两处位置。

## 今日任务

### 视频学习

#### 李宏毅《机器学习2021》

-  - [ ] 生成式对抗网络（三）生成器效能评估与条件式生成 `BV1By4y1A7K8`（约50分钟，只看条件式生成一节）

预计时长：1小时

------

### 理论学习

理解：

C-GAN（Mirza & Osindero 2014，4 页原文，arXiv 1411.1784）：

```
无监督 GAN：  z ──G──→ x̂            D(x̂) → 真/假
条件   C-GAN： (z, y) ──G──→ x̂|y     D(x̂, y) → 真/假
```

重点理解：

- y 从**两处**进入：生成器输入（与 z 拼接或其 embedding）、判别器输入（与图像拼接）
- 条件判别器必须同时看图像和标签，否则学不到 p(x|y)
- 加了标签不消灭模式坍塌：每个标签内部仍可能只学出一个样本
- **与制图综合的联系**：比例尺／综合等级就是现成的条件标签 y

------

### 输出成果

笔记：C-GAN 条件注入图（手绘或 mermaid），标注 y 进入 G 与 D 的两处位置，并回答"加了标签为什么仍会模式坍塌"。

------

### GitHub提交

```
git add .
git commit -m "Day49：完成C-GAN原理学习"
git push
```

------

# Day50（2026.08.16）

## 今日目标

理解条件数据集的组织形式，完成标签与条件向量的准备。

## 今日任务

### 理论学习

理解：

- 条件数据集的组织方式：图像与标签成对返回（MNIST 天然满足），标签要变成网络能吃的向量
- 标签进网络的三种写法：one-hot 直接拼接、embedding 后拼接、条件批归一化（把标签当条件调制）
- 与 Day42 数据增广知识的呼应：**几何变换不改变标签**，翻转旋转后 (x, y) 的 y 原样带过

------

### 代码实验

创建：

```
cgan_prepare.py
```

实现：

- 用 torchvision 载入 MNIST，打印一个 batch 的 x/y 形状与标签分布
- 写 `to_onehot(y, K)` 与 `nn.Embedding(K, d)` 两条路，各打印拼接后送入生成器的输入形状 (B, z_dim + d)
- 验证：同一 batch 两条路拼出的向量维度不同，但 batch 维一致

------

### GitHub提交

```
git add .
git commit -m "Day50：完成C-GAN条件数据与向量准备"
git push
```

------

# Day51（2026.08.17）

## 今日目标

掌握流模型的变量替换公式，手写耦合层验证可逆与三角 Jacobian。

## 今日任务

### 视频学习

#### 归一化流

-  - [ ] 【中配】什么是归一化流 `BV1hu4y1H7xg`（约 12 分钟）
-  - [ ] 神经网络(十五）标准化流(normalizing flow)与 INN `BV1Pm4y1X7yN`（约 30 分钟，重点看耦合层）

预计时长：45分钟

------

### 理论学习

理解：

变量替换公式（流模型的全部数学就这一行）：

```
p_X(x) = p_Z(f(x)) · |det ∂f(x)/∂x|        （f 可逆，且 Jacobian 行列式好算）
```

重点理解：

- 三条要求：可逆、Jacobian 行列式易算、堆叠后仍满足前两条
- 耦合层（NICE/RealNVP 思想）：把 x 分成 (x₁, x₂)，固定 x₁、只用 x₁ 的参数变换 x₂ → Jacobian 成三角阵，行列式＝对角块乘积
- 精确似然是拿架构约束换的：网络形状被"可逆＋三角"限制死，不像 GAN 随便堆

------

### 代码实验

创建：

```
flow_layers.py
```

实现：

- 手写仿射耦合层：y₁ = x₁，y₂ = x₂ ⊙ exp(s(x₁)) + t(x₁)，s/t 各用一个两层小 MLP
- 随机张量验证两条：正向→反向能还原（往返误差 < 1e-5）；log|det J| = Σ s(x₁) 与 autograd 数值一致
- 一维 toy 验证变量替换：x = exp(z)（z 服从标准正态）时 p_X 应是 lognormal，直方图对理论密度

------

### GitHub提交

```
git add .
git commit -m "Day51：完成流模型耦合层手写验证"
git push
```

------

# Day52（2026.08.18）

## 今日目标

完成GAN基础阶段复习与成果沉淀，为进入语义分割/U-Net主线做准备。

## 今日任务

### 理论复习

输出：

```
GAN基础总结.md
```

包含：

- GAN 原理与训练难点（附 mnist_gan 训练曲线）
- C-GAN 条件注入（标签进 G 与 D 两处）与流模型变量替换公式
- 生成路线对照：GAN 无似然·采样式 ／ 流模型 精确似然·架构受限——各自适合什么任务
- GAN 与制图综合、多尺度表达的结合点清单（供导师派任务时参考）

### 阶段衔接

- 预习第五阶段：语义分割任务定义（Day53 起）
- 整理本周 GAN 笔记与代码，准备向导师做一次 GAN 基础专题的小型进度汇报

------

### GitHub提交

```
git add .
git commit -m "Day52：完成GAN基础阶段总结"
git push
```

------

# GAN基础阶段验收（Day46-Day52）

完成后：

## 生成式模型基础能力

- ✅ 理解GAN的对抗训练机制
- ✅ 理解GAN训练不稳定的成因与表现
- ✅ 独立完成最简GAN（MNIST）实战
- ✅ 理解C-GAN的条件注入与"加标签仍会模式坍塌"的原因
- ✅ 掌握流模型变量替换公式，完成耦合层可逆与三角 Jacobian 的手写验证

------

# 第五阶段：地图制图综合与Transformer入门（Day53-Day67）

### 时间：2026.08.19—2026.09.02

## 阶段目标

> 本阶段是整个主体计划（Day01—Day67）最核心的阶段。
>
> 从“计算机视觉基础学习”进入“地图制图综合与多尺度表达实践”。
>
> 通过语义分割、U-Net地图建筑物要素提取以及Transformer学习，建立深度学习模型与地图制图应用之间的联系。
>
> 完成后应达到：
>
> - 理解语义分割任务流程
> - 理解FCN、DeepLab、U-Net网络结构
> - 掌握PyTorch语义分割项目开发流程
> - 能完成地图建筑物要素提取与化简实验
> - 掌握IoU、Dice等评价指标，并了解多尺度专用评价指标
> - 理解Attention机制
> - 理解Transformer基本结构
> - 阅读导师相关论文
> - 完成地图智能综合成果汇报

------

# Day53（2026.08.19）

## 今日目标

进入语义分割领域，理解分类、检测、分割任务区别。

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [ ] 第135讲 语义分割
-  - [ ] 第136讲 语义分割数据集

#### 霹雳吧啦语义分割

-  - [ ] 语义分割任务介绍

预计时长：2小时

------

### 理论学习

理解：

- 图像分类
- 目标检测
- 语义分割

重点：

```
Classification:

Image → Category


Segmentation:

Image → Pixel Mask
```

------

### 代码实验

创建：

```
segmentation_basic.py
```

实现：

- 读取图片
- 显示Mask
- 理解像素标签

------

### 输出成果

创建：

```
Semantic_Segmentation_Basic.md
```

记录：

- 三类视觉任务区别
- 语义分割应用场景

------

### GitHub提交

```
git add .
git commit -m "Day53：完成语义分割基础学习"
git push
```

------

# Day54（2026.08.20）

## 今日目标

理解FCN网络结构。

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] FCN网络结构讲解
-  - [ ] FCN代码实现

预计时长：2小时

------

### 理论学习

理解：

- Fully Convolutional Network
- Feature Map
- Upsampling
- Pixel Prediction

------

### 代码实验

创建：

```
fcn_demo.py
```

实现：

- 卷积特征提取
- 上采样恢复尺寸

------

### 输出成果

创建：

```
FCN_Notes.md
```

记录：

- FCN结构图
- FCN优缺点

------

### GitHub提交

```
git add .
git commit -m "Day54：完成FCN学习"
git push
```

------

# Day55（2026.08.21）

## 今日目标

理解DeepLab系列思想。

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] DeepLabV3网络介绍
-  - [ ] ASPP模块讲解

预计时长：

1.5小时

------

### 理论学习

掌握：

- 空洞卷积
- 感受野
- 多尺度特征

理解：

ASPP：

```
不同尺度卷积
        ↓
多尺度特征融合
```

------

### 代码实验

创建：

```
deeplab_demo.py
```

实现：

- 加载预训练DeepLab模型
- 图片预测

------

### 输出成果

创建：

```
DeepLab_Notes.md
```

------

### GitHub提交

```
git add .
git commit -m "Day55：完成DeepLab学习"
git push
```

------

# Day56（2026.08.22）

## 今日目标

学习U-Net网络结构。

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] U-Net网络结构讲解
-  - [ ] U-Net代码解析

预计时长：

2小时

------

### 理论学习

理解：

Encoder：

- 特征提取

Decoder：

- 空间恢复

Skip Connection：

- 保留边缘信息

------

### 代码实验

创建：

```
unet_structure_demo.py
```

实现：

- Conv Block
- Encoder
- Decoder

------

### 输出成果

生成：

```
U-Net_structure.png
```

创建：

```
UNet_Notes.md
```

------

### GitHub提交

```
git add .
git commit -m "Day56：完成U-Net结构学习"
git push
```

------

# Day57（2026.08.23）

## 今日目标

掌握语义分割数据读取流程。

## 今日任务

### 视频学习

#### 小土堆PyTorch

-  - [ ] Dataset与DataLoader复习

#### 霹雳吧啦语义分割

-  - [ ] U-Net数据处理

预计时长：

2小时

------

### 理论学习

掌握：

```
Image

↓

Tensor

↓

Model

↓

Prediction
```

------

### 代码实验

创建：

```
dataset.py
```

实现：

- Dataset类
- DataLoader
- 数据增强

------

### 输出成果

创建：

```
Dataset_Process.md
```

------

### GitHub提交

```
git add .
git commit -m "Day57：完成语义分割数据读取"
git push
```

------

# Day58（2026.08.24）

## 今日目标

搭建完整U-Net模型。

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] U-Net模型搭建

预计时长：

2小时

------

### 理论学习

理解：

- Encoder
- Decoder
- Skip Connection
- Feature Fusion

------

### 代码实验

创建：

```
unet.py
```

实现：

- Double Conv
- Down Sampling
- Up Sampling

------

### 输出成果

完成：

```
U-Net模型代码
```

------

### GitHub提交

```
git add .
git commit -m "Day58：完成U-Net模型搭建"
git push
```

------

# Day59（2026.08.25）

## 今日目标

开始训练建筑物提取模型。

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] U-Net训练流程

预计时长：

1.5小时

------

### 理论学习

掌握：

- Loss函数
- Optimizer
- Training Loop

------

### 代码实验

创建：

```
train.py
```

实现：

- Forward
- Loss计算
- 参数更新

------

### 输出成果

记录：

- Epoch Loss
- 模型训练过程

------

### GitHub提交

```
git add .
git commit -m "Day59：开始U-Net训练"
git push
```

# Day60（2026.08.26）

## 今日目标

优化U-Net模型训练效果，掌握语义分割模型评价指标。

------

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] U-Net模型训练优化
-  - [ ] 语义分割评价指标讲解

预计时长：

2小时

------

### 理论学习

掌握：

## 模型优化

- 学习率调整
- Batch Size调整
- Epoch数量影响
- 模型保存策略

## 评价指标

理解：

### IoU

Intersection over Union

### Dice

Dice Coefficient

理解：

为什么语义分割不能只看Accuracy。

------

### 代码实验

修改：

```
train.py
```

增加：

- best model保存
- IoU计算
- Dice计算

保存：

```
best_model.pth
```

------

### 输出成果

创建：

```
Segmentation_Metrics.md
```

记录：

- IoU公式
- Dice公式
- 模型训练结果

------

### GitHub提交

```
git add .
git commit -m "Day60：完成U-Net模型优化与评价指标"
git push
```

------

# Day61（2026.08.27）

## 今日目标

完成建筑物提取结果预测与可视化。

------

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] 语义分割预测流程
-  - [ ] 模型测试与结果可视化

预计时长：

1.5小时

------

### 理论学习

理解：

训练阶段：

```
Image
 ↓
Model
 ↓
Loss
 ↓
Update
```

预测阶段：

```
New Image
 ↓
Model
 ↓
Prediction Mask
```

------

### 代码实验

创建：

```
predict.py
```

实现：

- 加载best_model
- 输入测试影像
- 输出预测Mask

------

### 输出成果

生成：

```
results/
├── image.png
├── label.png
└── prediction.png
```

完成：

建筑物提取可视化结果。

------

### GitHub提交

```
git add .
git commit -m "Day61：完成建筑物提取预测可视化"
git push
```

------

# Day62（2026.08.28）

## 今日目标

完成第一个地图要素语义分割项目总结。

------

## 今日任务

### 视频学习

#### 霹雳吧啦语义分割

-  - [ ] 语义分割项目总结

预计时长：

1小时

------

### 理论学习

总结：

地图建筑物要素提取完整流程：

```
地图影像

↓

数据预处理

↓

Dataset

↓

U-Net

↓

训练

↓

预测

↓

精度评价
```

------

### 项目整理

创建：

```
Building_Extraction_Project/
│
├── dataset.py
├── unet.py
├── train.py
├── predict.py
├── metrics.py
│
├── README.md
└── results/
```

------

### 输出成果

创建：

```
Building_Extraction_Report.md
```

内容：

- 数据集介绍
- 模型结构
- 实验流程
- 评价指标
- 实验结果
- 存在问题

------

### GitHub提交

```
git add .
git commit -m "Day62：完成建筑物提取项目总结"
git push
```

------

# Day63（2026.08.29）

## 今日目标

学习Attention机制，为Transformer学习做准备。

------

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [ ] 第181讲 注意力机制
-  - [ ] 第182讲 Attention代码

预计时长：

40分钟

------

### 理论学习

理解：

Attention核心思想：

让模型自动学习不同位置的重要程度。

掌握：

## Query

查询信息

## Key

匹配信息

## Value

实际内容

理解：

Attention Score计算过程。

------

### 代码实验

创建：

```
attention_demo.py
```

实现：

- QKV生成
- Attention计算

------

### 输出成果

创建：

```
Attention_Notes.md
```

记录：

- Attention公式
- QKV含义
- 应用场景

------

### GitHub提交

```
git add .
git commit -m "Day63：完成Attention机制学习"
git push
```

------

# Day64（2026.08.30）

## 今日目标

理解Self-Attention机制。

------

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [ ] 第183讲 注意力分数
-  - [ ] 第189讲 自注意力

预计时长：

1小时

------

### 理论学习

理解：

Self-Attention：

输入自身产生：

- Query
- Key
- Value

掌握：

- Attention Matrix
- 长距离依赖

理解：

为什么Transformer可以替代RNN。

------

### 代码实验

创建：

```
Self_Attention_demo.py
```

实现：

- Scaled Dot Product Attention
- Attention Matrix可视化

------

### 输出成果

创建：

```
Self_Attention_Notes.md
```

------

### GitHub提交

```
git add .
git commit -m "Day64：完成Self Attention学习"
git push
```

------

# Day65（2026.08.31）

## 今日目标

理解Transformer整体结构。

------

## 今日任务

### 视频学习

#### 李沐《动手学深度学习》

-  - [ ] 第192讲 Transformer
-  - [ ] 第193讲 多头注意力代码
-  - [ ] 第194讲 Transformer代码

预计时长：

1.5小时

------

### 理论学习

掌握：

Transformer组成：

## Encoder

特征编码

## Decoder

序列生成

## Multi-Head Attention

多尺度关系建模

## Position Encoding

位置信息补充

理解：

Transformer为什么适用于地图要素与空间数据。

------

### 代码实验

创建：

```
transformer_demo.py
```

实现：

- Multi-head Attention调用
- Transformer Encoder调用

------

### 输出成果

创建：

```
Transformer_Notes.md
```

记录：

- Transformer结构图
- Attention流程

------

### GitHub提交

```
git add .
git commit -m "Day65：完成Transformer基础学习"
git push
```

------

# Day66（2026.09.01）

## 今日目标

阅读导师相关论文，了解GeoAI研究方向。

------

## 今日任务

### 视频学习

#### 论文辅助学习

观看：

- - [ ] Transformer地图要素应用介绍
- - [ ] 建筑物提取相关论文解读

预计时长：

1小时

------

### 论文阅读

阅读：

《基于Transformer框架的建筑物边缘优化提取研究》

重点分析：

- 研究背景
- 数据来源
- 模型结构
- Transformer作用
- 实验设计

------

### 理论学习

重点理解：

传统CNN：

```
局部感受野
```

Transformer：

```
全局依赖关系
```

思考：

为什么建筑物边缘提取需要Transformer。

------

### 输出成果

创建：

```
LiuPengcheng_Paper_Reading.md
```

记录：

- 研究问题
- 方法流程
- 创新点
- 对自己研究启发

------

### GitHub提交

```
git add .
git commit -m "Day66：完成导师论文阅读"
git push
```

------

# Day67（2026.09.02）

## 今日目标

完成主体阶段（Day01—Day67）总结，形成开学前成果。

------

## 今日任务

### 视频学习

#### 复习视频

回顾：

- CNN基础
- U-Net项目
- Transformer结构
- GAN图像翻译与实战

预计时长：

1小时

------

### 理论总结

总结主体阶段学习路线：

```
Python

↓

PyTorch

↓

CNN

↓

GAN基础

↓

语义分割

↓

U-Net地图要素提取与化简

↓

Attention

↓

Transformer

↓

GeoAI
```

------

### PPT制作

创建：

```
GeoAI_PreResearch_Report.pptx
```

内容：

------

## 第一部分

个人背景

包括：

- 长江大学GIS本科
- 华中师范大学资源与环境硕士

------

## 第二部分

主体阶段学习路线

包括：

- Python
- Git
- PyTorch
- CNN
- GAN
- U-Net
- Transformer

------

## 第三部分

地图建筑物要素提取与化简项目

展示：

- 数据集
- U-Net结构
- 实验结果

------

## 第四部分

论文阅读收获

------

## 第五部分

研一规划

包括：

- GeoAI方向
- 地图制图综合与多尺度表达
- Transformer地图要素应用
- GAN生成对抗网络

------

### 仓库整理

完善：

```
GeoAI-Learning
│
├── PyTorch
├── CNN
├── Semantic_Segmentation
├── Building_Extraction
├── Transformer
├── GAN
│
└── README.md
```

------

### GitHub提交

```
git add .
git commit -m "Day67：完成主体阶段GeoAI预研总结"
git push
```

------

# 第五阶段验收（Day53-Day67）

完成后：

## 深度学习能力

- ✅ 掌握PyTorch完整训练流程
- ✅ 理解CNN到语义分割过渡
- ✅ 掌握Dataset/DataLoader
- ✅ 掌握模型训练与评价

------

## 地图智能综合能力

- ✅ 理解FCN
- ✅ 理解DeepLab
- ✅ 掌握U-Net
- ✅ 完成地图建筑物要素提取与化简项目
- ✅ 理解地图要素语义分割流程

------

## Transformer能力

- ✅ 理解Attention
- ✅ 理解Self-Attention
- ✅ 理解Transformer Encoder
- ✅ 能阅读Transformer地图要素论文结构

------

# 第六阶段：生成模型项目实战与文献调研（Day68-Day73）

### 时间：2026.09.03—2026.09.08

## 阶段目标

> 本阶段为生成模型专题的后半部分。**GAN 原理与最简实战、C-GAN 与流模型原理已在第四阶段（Day46—Day52）提前完成**（导师 09.30 更正口径），本阶段聚焦**条件生成与流模型的开源项目实战、与制图综合结合**。
>
> 完成后应达到：
>
> - 跑通 cGAN 开源项目（按标签生成 MNIST）
> - 跑通流模型玩具＋图像两级实验，会看 NLL 曲线并说清精确似然付了什么代价
> - 能说明"多尺度＝条件标签"与"要素补齐＝条件补全"两个结合点
> - 能阅读生成模型相关论文
> - 完成生成模型与制图综合结合的文献调研与专题总结

## 视频资源

```
实战期以开源仓库 README＋代码为教材（黑马课程没有 cGAN 与流模型实战章节）
```

> **资源说明**：
>
> - **已学**（第四阶段，Day46—Day52）：第一章（GAN原理）；C-GAN 与流模型按 Day49—51 所列单集
> - **本阶段**：cGAN 任一 PyTorch 实现；流模型选一个耦合层实现（RealNVP/NICE 类）的仓库
> - **选看**（09.30 更正后由必修降级）：第二章 6-10（CycleGAN 实战）、第三章（starGAN架构）、第四章（starGAN实战）、第八章（图像补全）、第五章第 5、6 节（InstanceNorm、AdaIn）——多域翻译与图像补全对制图综合仍是好参照
> - **跳过**：第六章（变声器项目，与地图方向无关）
> - **选学**：第七章（图像超分辨率，Day74）

------

# Day68（2026.09.03）

## 今日目标

跑通cGAN开源项目，按标签生成指定数字。

## 今日任务

### 理论学习

理解：

- 训练循环与 Day43 最简 GAN 的唯一差别：G 与 D 各多接一路标签输入（对照 Day49 的条件注入图）
- 评估方式：固定一组 (z, y) 看随训练的演化；0—9 每个数字出一张 10×10 采样网格
- 多域扩展（starGAN 思想，选看第三章）：一个 G 吃所有标签 ↔ "一个模型多个比例尺"

------

### 代码实验

创建：

```
cgan_run/
```

实现：

- 跑通一个 PyTorch cGAN 在 MNIST 上的训练（6 GB 显存下 batch 128 足够）
- 输出 0—9 各一张采样网格图；可视化用 matplotlib

------

### GitHub提交

```
git add .
git commit -m "Day68：完成cGAN项目实战"
git push
```

------

# Day69（2026.09.04）

## 今日目标

跑通流模型在2D玩具分布上的训练，看懂精确似然。

## 今日任务

### 理论学习

理解：

玩具问题设定（双月/八高斯）：

```
真密度 p(x) 已知  →  流模型拟合 q(x)  →  直接比较：平均 log q(x)（NLL）
```

重点理解：

- 训练目标就是平均 log p(x)——GAN 根本没有这个数可看
- 收敛判据：测试集 NLL 不再降；可视化：采样点覆盖真分布、密度热图形状正确
- 耦合层堆叠：用 Day51 手写的那一层，堆 8 层加随机旋转

------

### 代码实验

创建：

```
flow_toy.py
```

实现：

- 双月分布上训练 8 层耦合流（Adam，lr 1e-3）
- 打印测试 NLL；画训练前/后采样对比图与密度热图各一张

------

### GitHub提交

```
git add .
git commit -m "Day69：完成流模型2D玩具实战"
git push
```

------

# Day70（2026.09.05）

## 今日目标

把流模型推到图像尺寸，观察"精确似然 vs 感知质量"的取舍。

## 今日任务

### 理论学习

理解：

- 图像上做流模型需要多尺度结构（glow 式下采样＋耦合），显存是主要约束
- 观察点：NLL 好看不代表样本好看出——精确似然与感知质量的矛盾，与 Day68 cGAN 的糊图对照
- 与制图综合的联系：若"1:1万→1:25万"做成可逆映射，流模型能给出**像素级一致**的综合结果并可算似然，GAN 不能

------

### 代码实验

创建：

```
flow_mnist/
```

实现：

- 跑通一个小型 RealNVP/Glow 在 MNIST（或 16×16 降采样版）上训练
- 记录 NLL 曲线＋采样图，与 Day68 cGAN 的视觉质量并排比较

------

### GitHub提交

```
git add .
git commit -m "Day70：完成流模型图像实战"
git push
```

------

# Day71（2026.09.06）

## 今日目标

掌握"补全"类任务在 GAN 与流模型两条路线下的做法，落到要素补齐。

## 今日任务

### 理论学习

理解：

图像补全两条路线：

```
路线 A（GAN）：    残缺图 → G → 补全图 → D 判整体真假        （无似然，说不出"补得有多合理"）
路线 B（流模型）： 已知区固定，对缺失区做条件采样 p(缺失|已知)  （可算似然，能给补全置信度）
```

**与制图综合的连接**：

- 要素补齐：断裂道路连接、河流连通性修复、要素缺失恢复——本质都是条件补全
- 路线 B 的"可逆"额外给一个好处：补全结果可反推回原图校验一致性

（选看：黑马第八章 1-4，了解路线 A 的经典做法）

------

### GitHub提交

```
git add .
git commit -m "Day71：完成条件补全两条路线梳理"
git push
```

------

# Day72（2026.09.07）

## 今日目标

完成生成模型与制图综合结合的文献调研。

## 今日任务

### 文献阅读

阅读：

- 制图综合 × 深度学习/GAN 论文 2~3 篇

重点关注：

- 研究问题与数据表示（矢量 / 栅格）
- 是否使用生成式方法（GAN / Flow / Diffusion）
- 多尺度评价指标
- 与课程中方法的异同

------

### 输出成果

创建：

```
生成模型制图综合文献调研.md
```

每篇论文记录：研究问题、方法、数据、与 cGAN / 流模型 / 条件补全的对应关系、可借鉴点。

------

### GitHub提交

```
git add .
git commit -m "Day72：完成生成模型与制图综合文献调研"
git push
```

------

# Day73（2026.09.08）

## 今日目标

完成生成模型专题总结，形成生成模型×制图综合研究方向清单。

## 今日任务

### 输出成果

完成：

```
生成模型学习总结.md
```

包含：

- GAN 原理与训练难点（Day46—Day48 部分并入）
- 三条生成路线对比：GAN 采样式无似然／cGAN 条件采样／流模型 精确似然·架构受限（starGAN 多域翻译为选看参照）
- 与制图综合、多尺度表达的结合点分析
- 后续可探索方向（供研一选题参考）

------

### GitHub提交

```
git add .
git commit -m "Day73：完成生成模型专题总结"
git push
```

------

# Day74（选学，2026.09.09）

## 今日目标

掌握基于GAN的图像超分辨率方法。

## 今日任务

### 视频学习

#### GAN对抗生成网络

-  - [ ] 第七章 1-论文概述
-  - [ ] 第七章 2-网络架构
-  - [ ] 第七章 3-数据与环境配置
-  - [ ] 第七章 4-数据加载与配置
-  - [ ] 第七章 5-生成模块
-  - [ ] 第七章 6-判别模块
-  - [ ] 第七章 7-VGG特征提取网络
-  - [ ] 第七章 8-损失函数与训练
-  - [ ] 第七章 9-测试模块

预计时长：1.5小时

------

### 理论学习

理解：

- 超分辨率与 GAN 的结合思路
- **感知损失（Perceptual Loss）：用 VGG 提取特征**（对应 Day37 VGG 学习内容）
- 对抗损失与内容损失的权衡

------

### GitHub提交

```
git add .
git commit -m "Day74：完成GAN图像超分辨率学习"
git push
```

------

# 第六阶段验收（Day68-Day73）

完成后：

## 生成式模型能力

- ✅ 巩固GAN对抗训练机制（原理与最简实战见第四阶段）
- ✅ 跑通 cGAN 开源项目（按标签生成）
- ✅ 跑通流模型玩具＋图像两级实验，会看 NLL 曲线并说清精确似然付了什么代价
- ✅ 掌握"补全"任务的 GAN／流模型两条路线
- ✅ 掌握生成模型项目开发流程

## 方向结合能力

- ✅ 能说明"多尺度＝条件标签""要素补齐＝条件补全"两个结合点
- ✅ 能阅读生成模型与制图综合相关论文
- ✅ 形成后续可探索的研究方向清单

------

# 73天最终验收

## 技术能力

- Python基础
- NumPy
- Pandas
- Git/GitHub
- PyTorch
- CNN
- FCN
- U-Net
- Attention
- Transformer

------

## 项目成果

完成：

- Massachusetts Buildings Dataset实验
- U-Net地图建筑物要素提取与化简项目
- GeoAI项目仓库

------

## 学术成果

完成：

- 导师相关论文阅读
- Transformer地图要素方向理解
- GAN生成对抗网络应用理解
- GeoAI汇报PPT

------

## 导师沟通准备

开学前能够向刘老师介绍：

> 我完成了GeoAI预研计划（Day01—Day73），已经掌握Python、PyTorch、CNN基础，并完成U-Net地图建筑物要素提取与化简实验，同时学习Transformer结构、GAN生成对抗网络并阅读老师相关论文，希望研一进一步开展地图制图综合与多尺度表达的智能化方法研究。

------

# 73天最终能力评估

```
Python开发          ★★★★☆
Git/GitHub          ★★★★☆
Pandas              ★★★☆☆
PyTorch             ★★★★☆
CNN                 ★★★★☆
OpenCV              ★★★☆☆
语义分割            ★★★☆☆
U-Net               ★★★☆☆
Transformer         ★★☆☆☆
GAN生成对抗网络     ★★★★☆
制图综合理论        ★★★☆☆
GeoAI               ★★★☆☆
论文阅读            ★★★☆☆
```

73天路线逻辑

```
Day1-Day15
Python + Git

↓

Day16-Day30
PyTorch + 深度学习基础

↓

Day31-Day45
CNN + CV基础 + 制图综合理论

↓

Day46-Day52
GAN基础专题（导师要求提前）

↓

Day53-Day62
地图要素语义分割 + U-Net建筑物提取与化简

↓

Day63-Day67
Transformer + 导师论文

↓

Day68-Day73
生成模型项目实战与文献调研

↓

研一进入地图制图综合与多尺度表达课题
```