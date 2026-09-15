# 导包
import torch
import torch.nn as nn


# 1.定义类，用于表示简单的CNN网络（借鉴LeNet结构）
class SimpleLeNet(nn.Module):
    def __init__(self):
        super(SimpleLeNet, self).__init__()

        # 卷积层1
        self.conv1 = nn.Conv2d(1, 6, 5, padding = 2)
        self.relu = nn.ReLU()
        # 池化层1
        self.pool1 = nn.MaxPool2d(2, 2)

        # 卷积层2
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 池化层1
        self.pool2 = nn.MaxPool2d(2, 2)

        # 全连接层
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 第一模块：Conv -> ReLU -> Pool
        x = self.pool1(self.relu(self.conv1(x)))
        # 第二模块：Conv - -> ReLU -> Pool
        x = self.pool2(self.relu(self.conv2(x)))
        # 展平维度：(Batch_size, Channels, H, W) -> (Batch_size, Channels * H * W)
        x = x.view(x.size(0), -1)
        # 全连接分类
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# 2.定义主函数
def main():
    print("=== 1、池化层 (Pooling Layer) 计算验证 ===")
    x_test = torch.tensor([[[1., 2., 3., 4.],
                            [5., 6., 7., 8.],
                            [9., 10., 11., 12.],
                            [13., 14., 15., 16.]]]).unsqueeze(0)        # Shape:(1, 4, 4) -> (1, 1, 4, 4)

    max_pool = nn.MaxPool2d(2, 2)
    avg_pool = nn.AvgPool2d(2, 2)

    print(f"原始张量 Shape:{x_test.shape}")
    print(f"2x2 Max Pooling 输出：\n{max_pool(x_test)}")
    print(f"2x2 Avg Pooling 输出：\n{avg_pool(x_test)}")

    print("=== 2、SimpleLeNet前向传播与维度检验 ===")
    # 模拟一个单通道28x28的图像输入（如MNIST数据）
    input_img = torch.randn(1, 1, 28, 28)
    model = SimpleLeNet()
    output = model(input_img)

    print(f"输入图像 Shape：{input_img.shape}")
    print(f"网络输出 Shape (10分类类别概率 / Logits)：{output.shape}")


# 3.测试
if __name__ == "__main__":
    main()
