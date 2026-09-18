# 导包
import torch
import torch.nn as nn


# 1.定义AlexNet网络结构类
class AlexNet(nn.Module):
    """AlexNet网络结构（2012）：5个卷积层 + 3个全连接层"""
    def __init__(self, num_classes = 1000):
        super(AlexNet, self).__init__()
        # 特征提取部分：5个卷积层（每层后接ReLU激活函数，共3次最大池化）
        self.features = nn.Sequential(
            # 第1组：卷积 -> 激活 -> 池化
            nn.Conv2d(3, 64, 11, 4, 2),
            nn.ReLU(inplace = True),         # 是否开辟新内存：True 不开辟 False 开辟，选择不开辟，直接在原有内存上操作从而节省内存
            nn.MaxPool2d(3, 2),

            # 第2组：卷积 -> 激活 -> 池化
            nn.Conv2d(64, 192, 5, 1, 2),
            nn.ReLU(inplace=True),          # 是否开辟新内存：True 不开辟 False 开辟，选择不开辟，直接在原有内存上操作从而节省内存
            nn.MaxPool2d(3, 2),

            # 第3-5组：连续3个卷积层（不改变空间尺寸）
            nn.Conv2d(192, 384, 3, 1, 1),
            nn.ReLU(inplace=True),          # 是否开辟新内存：True 不开辟 False 开辟，选择不开辟，直接在原有内存上操作从而节省内存
            nn.Conv2d(384, 256, 3, 1, 1),
            nn.ReLU(inplace=True),          # 是否开辟新内存：True 不开辟 False 开辟，选择不开辟，直接在原有内存上操作从而节省内存
            nn.Conv2d(256, 256, 3, 1, 1),
            nn.ReLU(inplace=True),          # 是否开辟新内存：True 不开辟 False 开辟，选择不开辟，直接在原有内存上操作从而节省内存
            nn.MaxPool2d(3, 2)
        )

        self.classifier = nn.Sequential(
            nn.Dropout(p = 0.5),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(p = 0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        # 1.特征提取：(N, 3, 224, 224) -> (N, 256, 6, 6)
        x = self.features(x)

        # 2.展平：(N, 256, 6, 6) -> (N, 256 * 6 * 6) = (N, 9216)
        x = x.reshape(x.shape[0], -1)       # 第0维不变，合并后三维到第1维，即(N, 256 * 6 * 6) -> (N, 9216)

        # 3.全连接分类：(N, 9216) -> (N, num_classes)
        x = self.classifier(x)
        return x

# 2.定义主函数
def main():
    # 1.创建模型对象
    model = AlexNet(num_classes = 1000)
    print("====================================== AlexNet网络结构 =======================================")
    print(model)

    # 2.统计参数量
    total = sum(p.numel() for p in model.parameters())
    conv_params = sum(p.numel() for p in model.features.parameters())
    fc_params = sum(p.numel() for p in model.classifier.parameters())
    print("=" * 70)
    # {total:,}：千位分隔符格式；{total / 1e6:.1f} M：把数字除以 100 万，保留 1 位小数
    print(f"总参数量：{total:,} ({total / 1e6:.1f} M)")
    # {conv_params / total * 100:.1f}%：计算卷积层参数占总参数的百分比，保留 1 位小数。
    print(f"卷积层参数：{conv_params:,} ({conv_params / total * 100:.1f}%)")
    # {fc_params / total * 100:.1f}%：计算全连接层参数占总参数的百分比，保留 1 位小数。
    print(f"全连接层参数：{fc_params:,} ({fc_params / total * 100:.1f}%)")

    # 3.输入随机图片测试前向传播
    x = torch.randn(1, 3, 224, 224)
    model.eval()
    with torch.no_grad():
        y = model(x)
    print("=" * 70)
    print(f"输入图片形状：{tuple(x.shape)}")
    print(f"输出结果形状：{tuple(y.shape)}")

# 3.测试
if __name__ == "__main__":
    main()
