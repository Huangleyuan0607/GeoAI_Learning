"""
案例：
    ANN（人工神经网络）案例：手机价格分类案例 - 优化版

背景：
    基于手机的20列特征 -> 预测手机价格区间（4个区间），推荐用深度学习做

ANN案例的实现步骤：
    1.构建数据集
    2.搭建神经网络
    3.模型训练
    4.模型测试

优化思路：
    1.优化方法 SGD -> Adam
    2.学习率 0.001 -> 0.0001
    3.对数据进行标准化
    4.增加网络深度，调整每层的神经元个数
    5.调整训练的轮数
    6. ...

"""


# 导包
import torch                                    # PyTorch框架，封装张量各种操作
from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset      # 数据集对象，数据 -> Tensor -> TensorDataset ->  数据加载器
from torch.utils.data import DataLoader         # 数据加载器
import torch.nn as nn                           # neural netword，封装了神经网络的各种操作
import torch.optim as optim                     # 优化器
# from sklearn.datasets import make_regression    # 创建回归数据集，此处已有数据，故不需要该库
from sklearn.model_selection import train_test_split        # 训练集和测试集的划分
import matplotlib.pyplot as plt                 # 绘图
import numpy as np                              # 数组（矩阵操作）
import pandas as pd                             # 数据处理
import time                                     # 时间模块
from torchsummary import summary                # 模型结构可视化


# todo 1.定义函数，构建数据集
def create_dataset():
    # 1.加载csv文件数据集
    data = pd.read_csv('./pytorch/Day29/data/手机价格预测.csv')
    # print(f"data:{data.head()}")
    # print(f"data:{data.shape}")       # (2000, 21)

    # 2.获取x特征列和y标签列（即价格区间列）
    x, y = data.iloc[:, :-1], data.iloc[:, -1]      # x特征列只需要前20列，y标签列只需要最后1列
    # print(f"x:{x.head()}, {x.shape}")       # (2000, 20)
    # print(f"y:{y.head()}, {y.shape}")       # (2000, 1)

    # 3.把特征列转成浮点型
    x = x.astype(np.float32)
    # print(f"x:{x.head()}, {x.shape}")       # (2000, 20)

    # 4.切分训练集和测试集
    # 参1：特征；参2：标签；参3：测试集所占比例（这里为0.2，即2000条中的20%，也就是400条测试集数据）；参4：随机种子：参5：样本分布（抽取数据集时参考y的比例）
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 3, stratify = y)
    # 优化1：数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 5.把数据集封装成张量数据集，思路：数据 -> 张量Tensor -> 数据集TensorDataset ->  数据加载器DataLoader
    train_dataset = TensorDataset(torch.from_numpy(x_train), torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.from_numpy(x_test), torch.tensor(y_test.values))
    # print(f"train_dataset:{train_dataset}, test_dataset:{test_dataset}")

    # 6.返回结果                         20(充当输入特征数)   4(充当输出标签数)
    return train_dataset, test_dataset, x_train.shape[1], len(np.unique(y))

# todo 2.搭建神经网络
class PhonePriceModel(nn.Module):
    # 1.在init魔法方法中，初始化父类成员，及搭建神经网络
    def __init__(self, input_dim, output_dim):          # 输入：20，输出：4
        # 1.1 初始化父类成员
        super().__init__()
        # 1.2 搭建神经网络
        # 优化2：增加网络深度
        # 隐藏层1
        self.fc1 = nn.Linear(input_dim, 128)
        # 隐藏层2
        self.fc2 = nn.Linear(128, 256)
        # 隐藏层3
        self.fc3 = nn.Linear(256, 512)
        # 隐藏层4
        self.fc4 = nn.Linear(512, 128)
        # 输出层
        self.output = nn.Linear(128, output_dim)

    # 2.定义前向传播方法forward()
    def forward(self, x):
        # 2.1 隐藏层1：加权求和+激活函数(ReLU)
        # x = self.fc1(x)
        # x = torch.relu(x)
        x = torch.relu(self.fc1(x))
        # 2.2 隐藏层2：加权求和+激活函数(ReLU)
        x = torch.relu(self.fc2(x))
        # 2.3 隐藏层3：加权求和+激活函数(ReLU)
        x = torch.relu(self.fc3(x))
        # 2.4 隐藏层4：加权求和+激活函数(ReLU)
        x = torch.relu(self.fc4(x))
        # 2.5 输出层：加权求和+激活函数(Softmax)
        # 正常写法，按行处理，但不需要，后续用多分类交叉熵损失函数CrossEntropyLoss()替代
        # CrossEntropyLoss() = softmax() + 损失计算
        # x = torch.softmax(self.output(x), dim = 1)
        x = self.output(x)
        # 2.4 返回处理结果
        return x

# todo 3.模型训练
def train(train_dataset, input_dim, output_dim):
    # 1.创建数据加载器，流程：数据 -> 张量 -> 数据集 -> 数据加载器
    # 参1：数据集对象（1600条）；参2：每批次数据条数（这里为16，即每批16条数据）；参3：是否打乱数据（训练集：打乱；测试集：不打乱）
    train_loader = DataLoader(train_dataset, batch_size = 16, shuffle = True)

    # 2.创建神经网络模型
    model = PhonePriceModel(input_dim, output_dim)

    # 3.定义损失函数，因为是多分类，这里用的是：多分类交叉熵损失函数
    criterion = nn.CrossEntropyLoss()

    # 4.创建优化器对象
    # 优化3:使用Adam优化方法；优化4：学习率变为0.0001
    # optimizer = optim.SGD(model.parameters(), lr = 0.001)
    optimizer = optim.Adam(model.parameters(), lr = 0.0001)

    # 5.模型训练
    # 5.1 定义变量，记录训练总轮数
    # 优化5：增加训练轮数 50 -> 100
    epochs = 100
    # 5.2 开始（每轮的）训练
    for epoch in range(epochs):
        # 5.2.1 定义变量，记录每次训练的损失值，训练批次数
        total_loss, batch_num = 0.0, 0
        # 5.2.2 定义变量，表示训练开始的时间
        start = time.time()
        # 5.2.3 开始本轮的各个批次的训练
        for x, y in train_loader:
            # 5.2.4 切换模型（状态）
            model.train()       # 训练模式
            # 5.2.5 模型预测
            y_pred = model(x)
            # 5.2.6 计算损失值
            loss = criterion(y_pred, y)
            # 5.2.7 梯度清零 + 反向传播 + 优化参数
            optimizer.zero_grad()
            loss.sum().backward()
            optimizer.step()
            # 5.2.8 累加损失值
            total_loss += loss.item()       # 把本轮的每批次的平均损失值累计起来，第1批次的平均损失 + 第2批次的平均损失 + 第3批次的平均损失 + ...
            batch_num += 1
        # 5.2.4 至此，本轮训练结束，打印训练信息
        print(f"epoch:{epoch + 1}, loss:{total_loss / batch_num:.4f}, time:{time.time() - start:.2f}s")

    # 6.走到这里，说明多轮训练结束，保存模型（参数）
    # 参1：模型对象的参数（权重矩阵，偏置矩阵）；参2：模型保存文件名及路径
    # print(f"\n\n模型的参数信息：{model.state_dict()}\n\n")
    torch.save(model.state_dict(), './pytorch/Day29/model/phone.pth')     # 后缀名用：pth, pkl, pickle均可

# todo 4.模型测试
def evaluate(test_dataset, input_dim, output_dim):
    # 1.创建神经网络分类对象
    model = PhonePriceModel(input_dim, output_dim)

    # 2.加载模型参数
    model.load_state_dict(torch.load('./pytorch/Day29/model/phone.pth'))

    # 3.创建测试集的数据加载器对象
    # 参1：数据集对象（400条）；参2：每批次数据条数（这里为8，即每批8条数据）；参3：是否打乱数据（训练集：打乱；测试集：不打乱）
    test_loader = DataLoader(test_dataset, batch_size = 8, shuffle = False)        # 测试集不打乱数据

    # 4.定义变量，记录预测正确的样本个数
    correct = 0

    # 5.从数据加载器中，获取到每批次的数据
    for x, y in test_loader:
        # 5.1 切换模型状态 -> 测试模式
        model.eval()
        # 5.2 模型预测
        y_pred = model(x)
        # print(f"y_pred:{y_pred}")           # [[0分类概率, 1分类概率, 2分类概率, 3分类概率], [...], ...]
        # 5.3 根据加权求和，得到类别，用argmax()函数获取最大值对应的下标，就是类别（做了类似于softmax的活）
        y_pred = torch.argmax(y_pred, dim = 1)      # dim = 1表示逐行处理
        # print(f"y_pred:{y_pred}")           # [第1条数据的预测分类, 第2条数据的预测分类, ...]
        # print(f"y:{y}")
        # 5.4 统计预测正确的样本个数
        # print(y_pred == y)              # tensor([False, False,  True, False, False,  True,  True,  True])
        # print((y_pred == y).sum())      # True:1, False:0
        correct += (y_pred == y).sum()          # 预测正确的样本数量

    # 6.走到这里，模型预测结束，打印准确率即可
    print(f"准确率(Accuracy): {correct / len(test_dataset):.4f}")

# todo 5.测试
if __name__ == '__main__':
    # 1.准备数据集
    train_dataset, test_dataset, input_dim, output_dim = create_dataset()       # 构建数据集
    # print(f"训练集 数据集对象：{train_dataset}")
    # print(f"测试集 数据集对象：{test_dataset}")
    # print(f"输入特征数：{input_dim}")         # 20
    # print(f"输出标签数：{output_dim}")        # 4

    # 2.搭建神经网络模型
    model = PhonePriceModel(input_dim, output_dim)
    # 计算模型参数
    # 参1：模型对象；参2：输入数据的形状（批次大小，输入特征数），每批16条，每条20列特征
    summary(model, input_size = (16, input_dim))

    # 3.模型训练
    train(train_dataset, input_dim, output_dim)

    # 4.模型测试
    evaluate(test_dataset, input_dim, output_dim)





























