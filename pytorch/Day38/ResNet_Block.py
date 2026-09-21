# 导包
import torch
import torch.nn as nn


# 1.定义残差块的类
class Residual(nn.Module):
    """残差块：y = f(x) + x（形状不一致时用1x1卷积调整捷径分支）"""
    def __init__(self, in_channels, out_channels, use_1x1conv = False, stride = 1):
        super(Residual, self).__init__()
        # 主分支：两个3x3卷积（padding = 1保持尺寸）
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size = 3, padding = 1, stride = stride)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size = 3, padding = 1)
        # 捷径分支：需要调整形状时才用1x1卷积
        if use_1x1conv:
            self.conv3 = nn.Conv2d(in_channels, out_channels, 1, stride = stride)
        else:
            self.conv3 = None
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.bn2 = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        # 1.主分支：卷积 -> BN -> 激活函数 -> 卷积 -> BN
        y = torch.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))
        # y = self.bn2(self.conv2(torch.relu(self.bn1(self.conv1(x)))))
        # 2.捷径分支：x和y形状不一致时做1x1卷积
        if self.conv3:      # 根据conv3是否存在来判断是否需要改变输入的形状
            x = self.conv3(x)
        # 3.残差连接：主分支输出 + 捷径分支输入
        y += x
        # 4.相加后再激活
        y =  torch.relu(y)
        return y

# 2.定义一个ResNet阶段的函数
# 参1：输入通道数；参2：输出通道数；参3：残差块个数；参4：是否为第一个阶段
def resnet_block(in_channels, out_channels, num_residuals, first_block = False):
    """一个ResNet阶段：由num_residuals个残差块组成"""
    blk = []
    for i in range(num_residuals):
        if i == 0 and not first_block:
            # 每个阶段的首块：尺寸减半 + 通道数翻倍（stride = 2 + 1x1卷积）
            blk.append(Residual(in_channels, out_channels, use_1x1conv = True, stride = 2))
        else:
            blk.append(Residual(out_channels, out_channels))
    return nn.Sequential(*blk)

# 3.定义ResNet模型
class ResNet(nn.Module):
    """简化版ResNet(ResNet-18结构)"""
    def __init__(self, num_classes = 10):
        super(ResNet, self).__init__()
        # 1.输入干（网络最前面、进入残差块之前的那一小段普通卷积结构）：大卷积核快速降采样
        self.stem = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size = 7, stride = 2, padding = 3),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(3, 2, 1)
        )
        # 2.四个阶段
        self.stage1 = resnet_block(64, 64, 2, first_block = True)
        self.stage2 = resnet_block(64, 128, 2)
        self.stage3 = resnet_block(128, 256, 2)
        self.stage4 = resnet_block(256, 512, 2)
        # 3.全局平均池化 + 全连接输出
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.stem(x)
        x = self.stage1(x)
        x = self.stage2(x)
        x = self.stage3(x)
        x = self.stage4(x)
        x = self.pool(x)        # (N, 512, 3, 3) -> (N, 512, 1, 1)
        x = x.reshape(x.shape[0], -1)       # (N, 512, 1, 1) -> (N, 512 * 1 * 1) = (N, 512)
        x = self.fc(x)
        return x

# 4.定义主函数
def main():
    print("=" * 60)
    print("1.残差块的两种情况对比")
    print("=" * 60)

    # 情况1：输入输出形状一致 -> 不需要在捷径设置1x1卷积来改变输入的形状
    x = torch.randn(2, 3, 6, 6)
    blk_a = Residual(3, 3, False)
    print(f"情况1 形状一致：{tuple(x.shape)} -> {tuple(blk_a(x).shape)}（捷径没有1x1卷积）")

    # 情况2：通道数变化 + 尺寸减半 -> 不需要在捷径设置1x1卷积来改变输入的形状
    x = torch.randn(2, 3, 6, 6)
    blk_a = Residual(3, 3, True, 2)
    print(f"情况1 形状变化：{tuple(x.shape)} -> {tuple(blk_a(x).shape)}（捷径含有1x1卷积）")

    print()
    print("=" * 60)
    print("2.完整ResNet各阶段特征图形状")
    print("=" * 60)

    net = ResNet(10)
    t = torch.randn(1, 1, 96, 96)
    print(f"输入          {tuple(t.shape)}")
    with torch.no_grad():
        t = net.stem(t)
        print(f"输入干之后     {tuple(t.shape)}")
        t = net.stage1(t)
        print(f"阶段1之后     {tuple(t.shape)}")
        t = net.stage2(t)
        print(f"阶段2之后     {tuple(t.shape)}")
        t = net.stage3(t)
        print(f"阶段3之后     {tuple(t.shape)}")
        t = net.stage4(t)
        print(f"阶段4之后     {tuple(t.shape)}")

    out = net(torch.randn(1, 1, 96, 96))
    print(f"最终输出        {tuple(out.shape)}")

    # 参数量统计
    total = sum(p.numel() for p in net.parameters())
    fc_params = sum(p.numel() for p in net.fc.parameters())
    print()
    print(f"总参数量：{total} ({total / 1e6:.2f}M)")
    print(f"全连接层参数量：{fc_params} (占{fc_params / total * 100:.2f}%)")

# 5.测试
if __name__ == "__main__":
    main()









