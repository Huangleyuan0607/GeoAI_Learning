# 导包
import torch
from torch import nn
from torch.nn import functional as F


# 1.定义Inception块的类
class Inception(nn.Module):
    """Inception块：四条并行支路，输出在通道维拼接"""
    # 参1：输入通道数；参2：第1个路径的输出通道数；参3：第2个路径的各层输出通道数；参4：第3个路径的各层输出通道数；参5：第4个路径的各层输出通道数
    def __init__(self, in_channels, c1, c2, c3, c4, **kwargs):
        super(Inception, self).__init__(**kwargs)
        # 分支1
        self.p1_1 = nn.Conv2d(in_channels, c1, kernel_size = 1)
        # 分支2
        self.p2_1 = nn.Conv2d(in_channels, c2[0], kernel_size = 1)
        self.p2_2 = nn.Conv2d(c2[0], c2[1], kernel_size = 3, padding = 1)
        # 分支3
        self.p3_1 = nn.Conv2d(in_channels, c3[0], kernel_size = 1)
        self.p3_2 = nn.Conv2d(c3[0], c3[1], kernel_size = 5, padding = 2)
        # 分支4
        self.p4_1 = nn.MaxPool2d(3, stride = 1,padding = 1)         # MaxPool2d默认步长是3，所以我们需要手动赋值
        self.p4_2 = nn.Conv2d(in_channels, c4, kernel_size = 1)

    def forward(self, x):
        p1 = F.relu(self.p1_1(x))                       # 路径1输出
        p2 = F.relu(self.p2_2(F.relu(self.p2_1(x))))    # 路径2输出
        p3 = F.relu(self.p3_2(F.relu(self.p3_1(x))))    # 路径3输出
        p4 = F.relu(self.p4_2(self.p4_1(x)))            # 路径4输出
        return torch.cat((p1, p2, p3, p4), dim = 1)      # 将4个路径输出按第1维度（通道）拼接


# 2.定义主函数
def main():
    # 1.搭建GoogLeNet的五个模块
    b1 = nn.Sequential(  # Stage 1
        nn.Conv2d(1, 64, 7, 2, 3),
        nn.ReLU(),
        nn.MaxPool2d(3, 2, 1),
    )

    b2 = nn.Sequential(  # Stage 2
        nn.Conv2d(64, 64, 1),
        nn.ReLU(),
        nn.Conv2d(64, 192, 3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(3, 2, 1)
    )

    b3 = nn.Sequential(  # Stage 3
        Inception(192, 64, (96, 128), (16, 32), 32),
        Inception(256, 128, (128, 192), (32, 96), 64),
        nn.MaxPool2d(3, 2, 1)
    )

    b4 = nn.Sequential(  # Stage 4
        Inception(480, 192, (96, 208), (16, 48), 64),
        Inception(512, 160, (112, 224), (24, 64), 64),
        Inception(512, 128, (128, 256), (24, 64), 64),
        Inception(512, 112, (144, 288), (32, 64), 64),
        Inception(528, 256, (160, 320), (32, 128), 128),
        nn.MaxPool2d(3, 2, 1)
    )

    b5 = nn.Sequential(  # Stage 5
        Inception(832, 256, (160, 320), (32, 128), 128),
        Inception(832, 384, (192, 384), (48, 128), 128),
        nn.AdaptiveAvgPool2d((1, 1)),
        nn.Flatten()
    )

    net = nn.Sequential(b1, b2, b3, b4, b5, nn.Linear(1024, 10))

    # 2.逐模块输出形状
    print("=" * 60)
    print("GoogLeNet各模块输出形状")
    print("=" * 60)
    x = torch.randn(1, 1, 96, 96)
    print(f"输入      {tuple(x.shape)}")
    net.eval()
    with torch.no_grad():
        for name, blk, in zip(["b1", "b2", "b3", "b4", "b5"], list(net)[:5]):
            x = blk(x)
            print(f"f{name:<8}      {tuple(x.shape)}")

    out = net(torch.randn(1, 1, 96, 96))
    print(f"最终输出        {tuple(out.shape)}")

    # 3.拆解单个Inception块的四条支路
    print()
    print("=" * 60)
    print("单个Inception块的四条支路")
    print("=" * 60)
    inc = Inception(192, 64, (96, 128), (16, 32), 32)
    t = torch.randn(1, 192, 24, 24)
    with torch.no_grad():
        p1 = F.relu(inc.p1_1(t))
        p2 = F.relu(inc.p2_2(F.relu(inc.p2_1(t))))
        p3 = F.relu(inc.p3_2(F.relu(inc.p3_1(t))))
        p4 = F.relu(inc.p4_2(inc.p4_1(t)))
        cat = torch.cat((p1, p2, p3, p4), dim = 1)
    print(f"输入      {tuple(t.shape)}")
    print(f"线路1 1x1卷积   {tuple(p1.shape)}   (64 通道)")
    print(f"线路2 1x1->3x3    {tuple(p2.shape)}  (128 通道)")
    print(f"线路3 1x1->5x5    {tuple(p3.shape)}   (32 通道)")
    print(f"线路4 3x3池化->1x1  {tuple(p4.shape)}   (32 通道)")
    print(f"通道拼接后   {tuple(cat.shape)}  (64+128+32+32=256)")

    # 4.参数量统计
    total = sum(p.numel() for p in net.parameters())
    fc_params = sum(p.numel() for p in net[-1].parameters())
    print()
    print(f"总参数量: {total:,} ({total / 1e6:.2f} M)")
    print(f"全连接层参数量: {fc_params:,} (占 {fc_params / total * 100:.2f}%)")

# 3.测试
if __name__ == "__main__":
    main()
