# 导包
import torch
import torch.nn as nn


# 1.定义函数，用于定义VGG块结构
def vgg_block(num_convs, in_channels, out_channels):
    """VGG块：num_convs个3x3卷积核（padding = 1保持输出尺寸不变） + 1个2x2最大池化层"""
    layers = []
    for _ in range(num_convs):      # 循环创建num_convs个3x3卷积核
        layers.append(nn.Conv2d(in_channels, out_channels, kernel_size = 3, padding = 1))
        layers.append(nn.ReLU(inplace = True))
        in_channels = out_channels      # 块内后续卷积的输入通道等于本块的输出通道
    layers.append(nn.MaxPool2d(kernel_size = 2, stride = 2))
    return nn.Sequential(*layers)

# 2.定义函数，用于定义VGG网络结构
def vgg(conv_arch, num_classes = 1000):
    """按卷积配置列表conv_arch搭建VGG网络"""
    conv_blks = []
    in_channels = 3
    for (num_convs, out_channels) in conv_arch:
        conv_blks.append(vgg_block(num_convs, in_channels, out_channels))
        in_channels = out_channels
    return nn.Sequential(
        *conv_blks,
        nn.Flatten(),        # 展平层：(N, 512, 7, 7) -> (N, 512 * 7 * 7) = (N, 25088)
        nn.Linear(out_channels * 7 * 7, 4096),
        nn.ReLU(inplace = True),
        nn.Dropout(p = 0.5),
        nn.Linear(4096, 4096),
        nn.ReLU(inplace = True),
        nn.Dropout(p = 0.5),
        nn.Linear(4096, num_classes)
    )

# 3.定义主函数
def main():
    # 卷积配置列表：(每个块的卷积核个数， 输出通道数)
    conv_arch_vgg11 = ((1, 64), (1, 128), (2, 256), (2, 512), (2, 512))     # 8个卷积层 + 3个全连接层 = VGG11
    conv_arch_vgg16 = ((2, 64), (2, 128), (3, 256), (3, 512), (3, 512))     # 13个卷积层 + 3个全连接层 = VGG16

    for name, arch in (("VGG11", conv_arch_vgg11), ("VGG16", conv_arch_vgg16)):
        net = vgg(arch)
        x = torch.randn(1, 3, 224 ,224)
        print("=" * 60)
        print(f"{name}网络各层特征图尺寸：")
        with torch.no_grad():
            for i, blk in enumerate(net):
                x = blk(x)
                if i < 5:
                    print(f"Block {i + 1} 输出：{tuple(x.shape)}")

        # 参数量统计
        total = sum(p.numel() for p in net.parameters())
        conv_params = sum(p.numel() for p in net[:5].parameters())      # 前5层是VGG块（卷积 + 池化）
        fc_params = sum(p.numel() for p in net[5:].parameters())        # 后5层是全连接层
        print(f"总参数量：{total:,} ({total / 1e6:.1f} M)")
        print(f"卷积部分：{conv_params:,} ({conv_params / total * 100:.1f}%)")
        print(f"全连接部分：{fc_params:,} ({fc_params / total * 100:.1f}%)")
        print(f"最终输出Shape：{tuple(net(torch.randn(1, 3, 224, 224)).shape)}")


# 4.测试
if __name__ == "__main__":
    main()