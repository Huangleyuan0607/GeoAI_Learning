# GeoAI Learning

### GeoAI预研学习仓库（2026）

### 作者：黄乐源

---

## 目录结构

GeoAI-Learning
│
├── .git
├── .idea
├── .gitignore
├── README.md
├── requirements.txt
│
├── docs
├── notes
├── reports
├── papers
│
├── python_basic
├── pytorch
├── opencv
├── segmentation
├── transformer
│
├── datasets
├── projects

## 学习目标

- Python开发
- Git/GitHub
- PyTorch
- OpenCV
- CNN
- U-Net
- Transformer
- 遥感建筑物提取

---

## 每周学习清单

|  **周数**  |                 **核心内容**                 |                     **每日细分学习清单**                     |
| :--------: | :------------------------------------------: | :----------------------------------------------------------: |
| **Week 1** |        **Python 核心语法与循环控制**         | Day 01: 环境搭建与 GitHub 初始化<br />Day 02: 变量与基础数据类型<br />Day 03: 字符串高级操作与格式化<br />Day 04: 运算符与 if 基础判断<br />Day 05: 多分支判断与模式匹配<br />Day 06: while 循环与猜数字游戏<br />Day 07: for 循环与循环控制（break/continue） |
| **Week 2** |        **Python 高级特性与阶段复盘**         | Day 08: 数据容器·列表操作<br />Day 09: 推导式与元组组包解包<br />Day 10: 数据容器·集合与字典<br />Day 11: 函数基础与嵌套调用<br />Day 12: 函数进阶与匿名函数 lambda Day<br />13: 递归算法与模块化开发<br />Day 14: 面向对象编程基础（类与对象）<br />Day 15: 异常处理与 Python 基础阶段总结 |
| **Week 3** |       **数学基础与 PyTorch 数据加载**        | Day 16: NumPy 矩阵思维与广播机制<br />Day 17: 线性代数基础（向量与矩阵乘法）<br />Day 18: 矩阵计算深化与批量运算<br />Day 19: 自动求导机制与反向传播<br />Day 20: PyTorch 环境配置与 Tensor 运算<br />Day 21: 数据加载之自定义 Dataset 类<br />Day 22: 数据加载之 DataLoader 批处理 |
| **Week 4** |        **深度学习经典模型与网络骨架**        | Day 23: 纯手工从零实现线性回归<br />Day 24: PyTorch 简洁实现线性回归 <br />Day 25: Softmax 分类理论与数据集引入 <br />Day 26: Fashion-MNIST 图像分类器实现 <br />Day 27: 多层感知机 MLP 与激活函数 <br />Day 28: 模型选择（过拟合与欠拟合） <br />Day 29: 神经网络骨架 nn.Module 与初识卷积 <br />Day 30: 跑通 MNIST 项目与深度学习基础总结 |
| **Week 5** |        **CNN 卷积控制与经典网络复现**        | Day 31: CNN 产生背景与二维卷积思想 <br />Day 32: 填充 Padding 与步幅 Stride 计算 <br />Day 33: 多通道卷积机制（RGB 卷积） <br />Day 34: 池化层（Max/Average Pooling） <br />Day 35: 经典网络·LeNet 复现 <br />Day 36: 经典网络·AlexNet 与 Dropout 思想 <br />Day 37: 经典网络·VGG 小卷积核优势 |
| **Week 6** |        **图像处理与语义分割架构引入**        | Day 38: 经典网络·GoogLeNet 多尺度特征 <br />Day 39: 经典网络·ResNet 残差连接 <br />Day 40: 数据增强技术（翻转/旋转/裁剪） <br />Day 41: OpenCV 基础（图像读取/显示/保存）<br /> Day 42: OpenCV 图像处理（灰度化/二值化/Canny） <br />Day 43: 语义分割领域引入与任务对比 <br />Day 44: 全卷积网络 FCN 与转置卷积上采样 <br />Day 45: U-Net 网络结构入门与跳跃连接 |
| **Week 7** |     **遥感数据集准备与 U-Net 项目实战**      | Day 46: DeepLabV1 & V2 空洞卷积思想<br />Day 47: DeepLabV3 ASPP 模块理论<br />Day 48: PyTorch 官方语义分割模型推理测试<br />Day 49: 遥感建筑物提取数据集下载与分析<br />Day 50: 构建遥感图像专用 DataLoader Day<br />51: 手动利用 PyTorch 搭建 U-Net 网络<br />Day 52: 编写 train.py 正式启动遥感建筑物提取训练 |
| **Week 8** | **Transformer 进阶、导师论文研读与成果汇报** | Day 53: 模型持续迭代与最佳权重保存<br />Day 54: 建筑物提取结果预测与可视化对比<br />Day 55: 撰写建筑物提取项目实验报告<br />Day 56: 注意力机制 Attention（Q、K、V 概念）<br />Day 57: 自注意力 Self-Attention 与长距离依赖<br />Day 58: Transformer 框架与多头注意力<br />Day 59: 研读导师最新建筑物边缘优化提取论文<br />Day 60: 制作 GeoAI 成果汇报 PPT 与仓库整理 |

## 每日学习任务

### 第一阶段 Python基础与数据分析入门（Day01-15）

- [x] **Day01**：环境搭建（Python & PyCharm安装、GitHub仓库初始化）
- [ ] **Day02**：变量与基础数据类型（输入输出、变量交换、int/float/str/bool）
- [ ] **Day03**：字符串高级操作（字符串拼接、f-string格式化、input函数）
- [ ] **Day04**：运算符与基础条件判断（算术/逻辑/比较运算符、if基础判断）
- [ ] **Day05**：多分支判断与模式匹配（if...elif...else、match模式匹配）
- [ ] **Day06**：while循环（循环基础、猜数字游戏实现）
- [ ] **Day07**：for循环与循环控制（for循环、range函数、嵌套循环、break/continue）
- [ ] **Day08**：数据容器·列表（列表切片、常用方法、成绩统计实验）
- [ ] **Day09**：推导式与元组（列表推导式、字符串方法、元组组包与解包）
- [ ] **Day10**：数据容器·集合与字典（集合去重、字典核心操作、词频统计实验）
- [ ] **Day11**：函数基础（函数定义、形参实参、返回值、嵌套调用）
- [ ] **Day12**：函数进阶（变量作用域、不定长参数、匿名函数 lambda）
- [ ] **Day13**：递归与模块化开发（递归算法、类型注解、自定义模块与包）
- [ ] **Day14**：面向对象编程基础（类与对象、实例方法、魔法方法、属性）
- [ ] **Day15**：异常处理与阶段总结（异常捕获、教务系统综合测试、第一阶段复盘）

### 第二阶段 深度学习基础入门（Day16-30）

- [ ] **Day16**：NumPy矩阵思维（ndarray创建、维度变换 reshape、广播机制）
- [ ] **Day17**：线性代数基础（向量与矩阵乘法、点积、范数、特定轴求和）
- [ ] **Day18**：矩阵计算深化（矩阵转置、批量运算、维度变化规律）
- [ ] **Day19**：自动求导机制（梯度概念、链式法则、反向传播与 PyTorch Autograd）
- [ ] **Day20**：PyTorch 环境与 Tensor（PyTorch配置、Tensor 创建与基本运算）
- [ ] **Day21**：数据加载之 Dataset（自定义 Dataset 类、数据读取流程）
- [ ] **Day22**：数据加载之 DataLoader（Batch 批处理读取、Shuffle 乱序机制）
- [ ] **Day23**：线性回归原理与从零实现（损失函数、梯度下降、纯手工回归）
- [ ] **Day24**：PyTorch 简洁实现线性回归（nn.Linear、MSELoss、SGD 优化器）
- [ ] **Day25**：Softmax 分类原理（Softmax 回归理论、图片分类数据集引入）
- [ ] **Day26**：Softmax 分类器实现（Softmax 从零与简洁实现、Fashion-MNIST 实验）
- [ ] **Day27**：多层感知机 MLP（激活函数、非线性映射、MLP 结构与代码）
- [ ] **Day28**：模型选择与拟合问题（训练集/验证集/测试集划分、过拟合与欠拟合）
- [ ] **Day29**：第一个神经网络（神经网络骨架 nn.Module、初识卷积与最大池化）
- [ ] **Day30**：MNIST 手写数字识别与阶段总结（完整跑通 MNIST 训练、深度学习基础总结）

### 第三阶段 GeoAI核心基础（Day31-Day45）

- [ ] **Day31**：CNN 引入与二维卷积（全连接局限性、卷积核滑动、特征图 Feature Map）
- [ ] **Day32**：卷积控制（填充 Padding、步幅 Stride、输出尺寸公式计算）
- [ ] **Day33**：多通道卷积（RGB三通道输入、多卷积核输出、通道机制）
- [ ] **Day34**：池化层（MaxPooling 与 AveragePooling 的实现与效果对比）
- [ ] **Day35**：经典网络·LeNet（LeNet 结构、手写数字识别经典复现）
- [ ] **Day36**：经典网络·AlexNet（ImageNet 背景、ReLU 激活、Dropout 抑制过拟合）
- [ ] **Day37**：经典网络·VGG（小卷积核 3x3 的优势、深层网络结构设计）
- [ ] **Day38**：经典网络·GoogLeNet（Inception 模块、多尺度特征提取）
- [ ] **Day39**：经典网络·ResNet（残差连接 Skip Connection、解决梯度消失/爆炸）
- [ ] **Day40**：数据增强技术（翻转 Flip、旋转 Rotation、随机裁剪 Crop）
- [ ] **Day41**：OpenCV 基础（OpenCV 安装、图像读取 imread、显示与保存）
- [ ] **Day42**：OpenCV 图像处理（图像灰度化、二值化、Canny 边缘检测）
- [ ] **Day43**：语义分割领域引入（分类、检测、分割的区别、语义分割数据集特点）
- [ ] **Day44**：全卷积网络 FCN（转置卷积上采样、Encoder-Decoder 架构、FCN原理）
- [ ] **Day45**：U-Net 网络入门（U-Net 经典结构、跳跃连接 Skip Connection）

### 第四阶段 GeoAI项目实践与Transformer入门（Day46-Day60）

- [ ] **Day46**：DeepLab 演进（DeepLabV1、V2 理论，空洞卷积与感受野扩大）
- [ ] **Day47**：DeepLabV3（ASPP 空洞空间卷积池化金字塔、多尺度特征融合）
- [ ] **Day48**：PyTorch 语义分割推理（加载官方预训练模型、测试图像推理）
- [ ] **Day49**：遥感数据集准备（下载并分析 Massachusetts Buildings Dataset 影像与标签）
- [ ] **Day50**：遥感数据 DataLoader（构建适用于建筑物提取的遥感图像数据加载器）
- [ ] **Day51**：手动搭建 U-Net 网络（利用 PyTorch 实现 U-Net 编码器与解码器）
- [ ] **Day52**：遥感建筑物提取训练（编写 train.py，配置前向传播、Loss、开始训练）
- [ ] **Day53**：模型迭代与权重保存（多 Epoch 训练、监控 Loss 变化、保存 best_model.pth）
- [ ] **Day54**：建筑物提取结果预测（编写 predict.py，输出原图、标签图、预测对比图）
- [ ] **Day55**：项目实验总结（撰写建筑物提取报告、分析错分漏分及边界问题）
- [ ] **Day56**：注意力机制 Attention（Q、K、V 概念，注意力权重计算理论）
- [ ] **Day57**：自注意力 Self-Attention（自注意力矩阵计算、捕捉遥感长距离依赖关系）
- [ ] **Day58**：Transformer 框架（多头注意力 Multi-Head Attention、Encoder/Decoder 架构）
- [ ] **Day59**：导师论文研读（精读刘鹏程老师《基于Transformer框架的建筑物边缘优化提取研究》）
- [ ] **Day60**：预研成果汇报与开学准备（制作 GeoAI 成果汇报 PPT、整理 GitHub 仓库、准备导师沟通）