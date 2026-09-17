"""
案例：
    演示CNN的综合案例，图像分类

回顾：深度学习项目步骤
    1.准备数据集
        这里我们用的是计算机视觉模块torchvision自带的CIFAR10数据集，包含6w张(32, 32, 3)图像，10个类别，每个类别6000张图像，5w张训练集，1w张测试集
        需要单独安装torchvision包
    2.搭建(卷积)神经网络
    3.模型训练
    4.模型测试

卷积层：
    提取图像局部特征 -> 特征图(Feature Map)，计算方式：N = (W - F + 2P) // S + 1
池化层：
    降维，有最大池化和平均池化
    池化只在HW上做调整，通道上不改变

案例的优化思路：
    增加卷积核的数量
    增加全连接层的参数量
    调整学习率
    调整优化方法
    调整激活函数
    增加Dropout层 （常见的全连接层Dropout用法：Linear -> ReLU -> Dropout -> Linear -> ReLU -> Dropout -> Linear）
    ...

本文件已实施的优化（按代码中出现的先后顺序编号）：
    优化1：增加每批次样本数 8 -> 64
    优化2：使用GPU进行训练（设备定义、模型与数据搬运、DataLoader加速、权重加载）
    优化3：增加卷积层通道数 6/16/32 -> 32/64/128，并给3x3卷积加 padding=1
    优化4：增加批量归一化层 BatchNorm2d（共3层，顺序：卷积 -> BN -> ReLU -> 池化）
    优化5：增加卷积层和池化层（卷积层从2组增加到3组）
    优化6：调整全连接层结构（删除 fc2，只保留 fc1 和输出层）
    优化7：增加Dropout层（p = 0.5，接在 fc1 之后）
    优化8：增加训练轮数 10 -> 50
    优化9：使用学习率调度器 MultiStepLR（milestones=[25, 40], gamma=0.2）
    优化10：增加 with torch.no_grad()（测试时不计算梯度，节省显存和计算）
"""


# 导包
import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor
import torch.optim as optim
from torch.utils.data import DataLoader
import time
import matplotlib.pyplot as plt
from torchsummary import summary

# 每批次样本数
"""优化1：增加每批次样本数 8 -> 64"""
# BATCH_SIZE = 8
# BATCH_SIZE = 32
BATCH_SIZE = 64
"""优化2：使用GPU进行训练"""
# 定义全局设备，如果检测到GPU就用cuda，否则用cpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 全局开启 cuDNN 自动调优（只需一次）
torch.backends.cudnn.benchmark = True

# 1.准备数据集
def create_dataset():
    # 1.获取训练集
    # 参1：数据集路径；参2：是否是训练集；参3：数据预处理 -> 张量数据；参4：是否联网下载数据集（这里我们已经下栽到了本地）
    train_dataset = CIFAR10(root = './pytorch/Day34/data', train = True, transform = ToTensor(), download = True)

    # 2.获取测试集
    test_dataset = CIFAR10(root = './pytorch/Day34/data', train = False, transform = ToTensor(), download = True)

    # 3.返回数据集
    return train_dataset, test_dataset

# 2.搭建(卷积)神经网络
class ImageModel(nn.Module):
    # 1.初始化父类成员，搭建神经网络
    def __init__(self):
        # 1.1 初始化父类成员
        super(ImageModel, self).__init__()
        # 1.2 搭建神经网络
        """优化3：增加卷积层通道数 6/16/32 -> 32/64/128，并给3x3卷积加padding=1"""
        # 卷积层1：输入3通道，输出32通道，卷积核大小3x3，步长1，填充1
        self.conv1 = nn.Conv2d(3, 32, 3, padding = 1)
        """优化4：增加批量归一化层"""
        # 新增：批量归一化层1
        self.bn1 = nn.BatchNorm2d(32)
        # 池化层1：池化窗口2x2，步长2，填充0（默认）
        self.pool1 = nn.MaxPool2d(2, 2)

        # 卷积层2：输入32通道，输出64通道，卷积核大小3x3，步长1，填充1
        self.conv2 = nn.Conv2d(32, 64, 3, padding = 1)
        """优化4：增加批量归一化层"""
        # 新增：批量归一化层2
        self.bn2 = nn.BatchNorm2d(64)
        # 池化层2：池化窗口2x2，步长2，填充0（默认）
        self.pool2 = nn.MaxPool2d(2, 2)

        """优化5：增加卷积层和池化层（卷积层从2组增加到3组）"""
        # 卷积层3：输入64通道，输出128通道，卷积核大小3x3，步长1，填充1
        self.conv3 = nn.Conv2d(64, 128, 3, padding = 1)
        """优化4：增加批量归一化层"""
        # 新增：批量归一化层3
        self.bn3 = nn.BatchNorm2d(128)
        # 池化层3：池化窗口2x2，步长2，填充0（默认）
        self.pool3 = nn.MaxPool2d(2, 2)

        # # 隐藏层（全连接层）1：输入16*6*6，输出120
        # self.fc1 = nn.Linear(16 * 6 * 6, 120)
        # # 隐藏层（全连接层）2：输入120，输出84
        # self.fc2 = nn.Linear(120, 84)
        # # 输出层（全连接层）：输入84，输出10
        # self.output = nn.Linear(84, 10)

        """优化6：调整全连接层结构（删除fc2，只保留fc1和输出层）"""
        # 隐藏层（全连接层）1：输入128*4*4 = 2048，输出128
        self.fc1 = nn.Linear(128 * 4 * 4, 128)
        # 输出层（全连接层）：输入128，输出10
        self.output = nn.Linear(128, 10)

        """优化7：增加Dropout层"""
        # Dropout层，p表示神经元被丢弃的概率
        self.dropout = nn.Dropout(p = 0.5)

    # 2.定义前向传播
    def forward(self, x):
        # 第1层：卷积层1(加权求和) + 激励层(激活函数) + 池化层1
        # 分解版
        # x = self.conv1(x)         # 卷积层1
        # x = torch.relu(x)         # 激活函数
        # x = self.pool1(x)         # 池化层1

        # 整合版：池化  +  激活   +    卷积
        # x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool1(torch.relu(self.bn1(self.conv1(x))))

        # 第2层：卷积层2(加权求和) + 激励层(激活函数) + 池化层2
        # x = self.pool2(torch.relu(self.conv2(x)))
        x = self.pool2(torch.relu(self.bn2(self.conv2(x))))

        """优化5：增加卷积层和池化层（卷积层从2组增加到3组）"""
        # 第3层：卷积层3(加权求和) + 激励层(激活函数) + 池化层3
        # x = self.pool3(torch.relu(self.conv3(x)))
        x = self.pool3(torch.relu(self.bn3(self.conv3(x))))

        # 细节：全连接层只能处理二维数据，所以要将数据进行展平处理 (N, 128, 4, 4) -> (N, 128 * 4 * 4)
        # 参1：样本数(行数)；参2：特征数(列数)，-1表示自动计算
        x = x.reshape(x.shape[0], -1)       # 64行2048列
        # print(f"x.shape:{x.shape}")

        # 第3层：全连接层(加权求和) + 激励层(激活函数)
        x = torch.relu(self.fc1(x))
        """优化7：增加Dropout层"""
        x = self.dropout(x)

        # # 第4层：全连接层(加权求和) + 激励层(激活函数)
        # x = torch.relu(self.fc2(x))
        # x = self.dropout(x)

        # 第5层：输出层(加权求和)
        return self.output(x)       # 后续用 多分类交叉熵随时函数CrossEntropyLoss =softmax()激活函数 + 损失计算

# 3.模型训练
def train(train_dataset):
    # 1.创建数据加载器
    # dataloader = DataLoader(train_dataset, batch_size = BATCH_SIZE, shuffle = True)
    """优化2：使用GPU进行训练"""
    dataloader = DataLoader(train_dataset, batch_size = BATCH_SIZE, shuffle = True, num_workers = 2, pin_memory = True)
    # 2.创建模型对象
    # model = ImageModel()
    """优化2：使用GPU进行训练"""
    model = ImageModel().to(device)
    print(f"模型所在设备: {next(model.parameters()).device}")
    # 3.创建损失函数对象
    criterion = nn.CrossEntropyLoss()
    # 4.创建优化器对象
    optimizer = optim.Adam(model.parameters(), lr = 1e-3)

    # 5.循环遍历epoch，开始每轮的训练动作
    # 5.1 定义变量，记录训练总轮数
    """优化8：增加训练轮数 10 -> 50"""
    # epochs = 10         # 训练总轮数
    epochs = 50         # 训练总轮数
    # epochs = 100         # 训练总轮数

    """优化9：使用学习率调度器（MultiStepLR：milestones=[25, 40], gamma=0.2）"""
    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[25, 40], gamma=0.2)

    # 5.2 遍历，完成每轮的所有批次的训练动作
    for epoch_idx in range(epochs):
        # 5.2.1 定义变量，记录：总损失，总样本数据量，预测正确样本个数，训练（开始）时间
        total_loss, total_samples, total_correct, start = 0.0, 0, 0, time.time()
        # 5.2.2 遍历数据加载器，获取每批次的数据
        for x, y in dataloader:
            """优化2：使用GPU进行训练"""
            x, y = x.to(device), y.to(device)
            # 5.2.3 切换训练模式
            model.train()
            # 5.2.4 模型预测
            y_pred = model(x)       # 没有结合损失函数和优化器
            # 5.2.5 计算损失
            loss = criterion(y_pred, y)
            # 5.2.6 梯度清零 + 反向传播 + 参数更新
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

             # 5.2.7 统计预测正确的样本个数
            # print(y_pred)       # 批次中每张图每个分类的预测概率

            # argmax()函数返回最大值对应的索引，充当 -> 该图片的预测分类
            # print(torch.argmax(y_pred, dim = -1))       # -1表示最后一个维度，即行
            # print(y)
            # print(torch.argmax(y_pred, dim = -1) == y)
            # print((torch.argmax(y_pred, dim = -1) == y).sum())
            # total_correct += (torch.argmax(y_pred, dim = -1) == y).sum()
            total_correct += (torch.argmax(y_pred, dim=-1) == y).sum().item()

            # 5.2.8 统计当前批次的总损失            弟1批平均损失 + 弟1批样本个数
            total_loss += loss.item() * len(y)      # [第1批总损失 + 第2批总损失 + ...]
            # 5.2.9 统计当前批次的总样本个数
            total_samples += len(y)         # 累加每批样本的个数
            # break     # 每轮只训练1批，提高训练效率，减少训练时长，只有测试会这么写，实际开发绝不可这样做

        # 5.2.10 至此说明一轮训练完毕，打印每轮的训练信息
        print(f"Epoch: {epoch_idx + 1}, Loss: {total_loss / total_samples:.5f}, Acc: {total_correct / total_samples:.2f}, time: {time.time() - start:.2f}s")
        # break     # 这里写break意味着只训练1轮，提高训练效率，减少训练时长，只有测试会这么写，实际开发绝不可这样做
        scheduler.step()        # 加衰减

    # 6.保存模型
    torch.save(model.state_dict(), './pytorch/Day35/model/image_model_new.pth')

# 4.模型测试
def evaluate(test_dataset):
    # 1.创建测试集数据加载器
    # test_dataloader = DataLoader(test_dataset, batch_size = BATCH_SIZE, shuffle = False)
    """优化2：使用GPU进行训练"""
    test_dataloader = DataLoader(test_dataset, batch_size = BATCH_SIZE, shuffle = False, num_workers = 2, pin_memory = True)
    # 2.创建模型对象
    # model = ImageModel()
    """优化2：使用GPU进行训练"""
    model = ImageModel().to(device)
    # 3.加载模型参数
    # model.load_state_dict(torch.load('./pytorch/Day35/model/image_model_new.pth'))      # pickle文件
    """优化2：使用GPU进行训练"""
    model.load_state_dict(torch.load('./pytorch/Day35/model/image_model_new.pth', map_location=device))
    # 4.定义变量，统计预测正确的样本个数以及总样本个数
    total_correct, total_samples = 0, 0
    # 5.遍历数据加载器，获取每批次的数据
    """优化10：增加with torch.no_grad():，测试时不需要计算梯度，节省显存和计算"""
    with torch.no_grad():
        for x, y in test_dataloader:
            """优化2：使用GPU进行训练"""
            x, y = x.to(device), y.to(device)
            # 5.1 切换模型模式
            model.eval()        # 测试模式
            # 5.2 模型预测
            y_pred = model(x)
            # 5.3 因为训练时用了CrossEntropyLoss，所以搭建网络时没有加softmax()激活函数，这里要用argmax()来模拟
            # argmax()函数功能：返回最大值对应索引，充当 -> 该图片的预测分类
            y_pred = torch.argmax(y_pred, dim = -1)
            # 5.4 统计预测正确的样本个数
            # total_correct += (y_pred == y).sum()
            total_correct += (y_pred == y).sum().item()
            # total_correct += (torch.argmax(y_pred, dim = -1) == y).sum()      # 也可以合并5.3和5.4
            # 5.5 统计总样本个数
            total_samples += len(y)

    # 6.打印正确率（预测结果）
    print(f"Test Acc: {total_correct / total_samples:.2f}")

# 5.测试
if __name__ == '__main__':
    # 1.获取数据集
    train_dataset, test_dataset = create_dataset()
    # print(f"训练集：{train_dataset.data.shape}")        # (50000, 32, 32, 3)
    # print(f"测试集：{test_dataset.data.shape}")         # (10000, 32, 32, 3)
    # # {'airplane': 0, 'automobile': 1, 'bird': 2, 'cat': 3, 'deer': 4, 'dog': 5, 'frog': 6, 'horse': 7, 'ship': 8, 'truck': 9}
    # print(f"数据集类别：{train_dataset.class_to_idx}")
    #
    # # 图像展示
    # plt.figure(figsize = (2, 2))
    # plt.imshow(train_dataset.data[11])      # 索引为11的图像
    # plt.title(train_dataset.targets[11])        # 标题为索引为11的图像的标签
    # plt.show()

    # 2.搭建神经网络
    # model = ImageModel()
    # 查看模型参数
    # 参1：模型；参2：输入维度(C通道, H高, W宽)；参3：批次大小
    # summary(model, (3, 32, 32), batch_size = BATCH_SIZE)        # 查看模型参数（batch_size在模型训练里生效）

    # 3.模型训练
    # train(train_dataset)

    # 4.模型测试
    evaluate(test_dataset)





