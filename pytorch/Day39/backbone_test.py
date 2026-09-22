# 导包
import torch
import torch.nn as nn
from torchvision import models


# 1.定义主函数
def main():
    # 1.加载ResNet-5-（weights = None表示随机初始化，避免联网下载预训练权重）
    model = models.resnet50(weights = None)
    model.eval()

    # 2.查看网络层（顶层结构）
    print("="* 60)
    print("ResNet50 顶层结构")
    print("="* 60)
    for name, module in model.named_children():
        print(f"{name:<12} {module.__class__.__name__}")

    # 3.统计参数量
    total = sum(p.numel() for p in model.parameters())
    print()
    print(f"总参数量：{total:,} ({total / 1e6:.1f}M)")

    # 4.逐段输出feature map（观察Backbone的特征提取过程）
    x = torch.randn(1, 3, 224, 224)
    print()
    print("="* 60)
    print("Backbone 各阶段 feature map 形状")
    print("="* 60)
    with torch.no_grad():
        print(f"输入  {tuple(x.shape)}")
        x = model.conv1(x)
        print(f"conv1   {tuple(x.shape)}")
        x = model.bn1(x)
        x = model.relu(x)
        x = model.maxpool(x)
        print(f"maxpool   {tuple(x.shape)}")
        x = model.layer1(x)
        print(f"layer1  {tuple(x.shape)}")
        x = model.layer2(x)
        print(f"layer2  {tuple(x.shape)}")
        x = model.layer3(x)
        print(f"layer3  {tuple(x.shape)}")
        x = model.layer4(x)
        print(f"layer4  {tuple(x.shape)}")

    # 5.把Backbone单独截取出来（去掉avgpool和fc）
    backbone = nn.Sequential(*list(model.children())[:-2])      # -1和-2就分别是fc和avgpool
    feat = backbone(torch.randn(1, 3, 224,224))
    print()
    print(f"用 Sequential 截取的 Backbone 输出：{tuple(feat.shape)}")

    # 6.接上不同的 Task head     平均池化 -> 展平 -> 全连接
    gap = nn.AdaptiveAvgPool2d(1)           # 平均池化
    v = gap(feat).reshape(1, -1)            # 展平层
    print(f"经过 GAP 之后：{tuple(v.shape)} -> 可直接接分类头 / 分割头")


# 2.测试
if __name__ == "__main__":
    main()