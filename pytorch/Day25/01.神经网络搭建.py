"""
案例：
    演示神经网络搭建流程

深度学习案例的4个步骤：
    1、准备数据
    2、搭建神经网络（数据预处理）
    3、模型训练（反向传播就在这一步中进行）
    4、模型测试

神经网络搭建流程：
    1、定义一个类，继承：nn.module
    2、在__init__()方法中，搭建神经网络
    3、在forward方法中，完成：前向传播

"""

# 导包
import torch
import torch.nn as nn
from torchsummary import summary        # 计算模型参数，查看模型结构


# todo：1.搭建神经网络，即自定义继承：nn.module
class ModelDemo(nn.Module):
    # todo：1.1 在init魔法方法中，完成初始化：父类成员，及神经网络搭建
    def __init__(self):
        # 1.1 初始化父类成员
        super().__init__()

        # 1.2 搭建神经网络 -> 隐藏层 + 输出层
        # 隐藏层1：输入特征数3，输出特征数3
        self.fc1 = nn.Linear(3, 3)
        # 隐藏层2：输入特征数3，输出特征数2
        self.fc2 = nn.Linear(3, 2)
        # 输出层：输入特征数2，输出特征数2
        self.output = nn.Linear(2, 2)

        # 1.3 对隐藏层进行参数初始化（未来不用写这一步，默认会做这件事的）
        # 隐藏层1
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.zeros_(self.fc1.bias)

        # 隐藏层2
        nn.init.kaiming_normal_(self.fc2.weight)
        nn.init.zeros_(self.fc2.bias)

    # todo：1.2 前向传播：输入层 -> 隐藏层 -> 输出层
    def forward(self, x):       # 函数名必须严格定义为forward，因为他需要被自动调用
        # 1.1 第一层 隐藏层计算：加权求和 + 激活函数Sigmoid
        # 分解版写法
        # x = self.linear(x)          # 加权求和
        # x = torch.sigmoid(x)        # 激活函数Sigmoid

        # 合并版写法
        x = torch.sigmoid(self.fc1(x))        # 加权求和 + 激活函数Sigmoid

        # 1.2 第二层 隐藏层计算：加权求和 + 激活函数ReLU
        x = torch.relu(self.fc2(x))

        # 1.3 第三层输出层计算：加权求和 + 激活函数Softmax
        x = torch.softmax(self.output(x), dim = -1)     # dim = -1在此处表示按行计算，一条样本一条样本地处理

        # 1.4 返回预测值
        return x

# todo：2.模型训练
def train():
    # 1.创建模型对象
    my_model = ModelDemo()
    print("my_model: ", my_model)

    # 2.创建数据集样本，随机生成
    data = torch.randn(size = (5, 3))
    print("data: ", data)
    print("data.shape: ", data.shape)       # 形状，（5, 3）5行3列
    print("data.requires_grad: ", data.requires_grad)       # 是否设置了自动微分，默认False

    # 3.调用神经网络模型 -> 进行模型训练
    output = my_model(data)     # 底层自动调用了forward()方法进行前向传播
    print("output: ", output)
    print("output.shape: ", output.shape)       # (5, 2)
    print("output.requires_grad: ", output.requires_grad)       # True，因为一会这些值会用于反向传播，从而反向更新参数
    print("-" * 30)

    # 4.计算和查看模型参数
    print("==================计算模型参数==================")
    # 参1：（神经网络）模型对象；参2：输入数据的维度(5, 3)
    summary(my_model, input_size=(5, 3))        # 此处input_size的shape与输入数据集data相同。在输出结果的Output Shape中，-1代表自动计算，表示不确定

    print("==================查看模型参数==================")
    for name, param in my_model.named_parameters():
        print("name：", name)
        print("param：", param)
        print()


# todo：3.测试
if __name__ == '__main__':
    train()















