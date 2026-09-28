# 导包
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Subset
from torchvision.datasets import FashionMNIST
from torchvision import transforms
from torchvision.utils import save_image



# 1.定义增广变换：训练用（带随机性）与测试用（只做确定性预处理）
def get_transforms():
    # 1.1 训练阶段：随机翻转 + 随机裁剪缩放 + 随机旋转 + 颜色抖动，最后转张量并归一化
    train_augs =transforms.Compose([
        transforms.RandomHorizontalFlip(p = 0.5),                       # 随机翻转，p = 0.5表示以0.5概率左右翻转
        transforms.RandomResizedCrop(size = 28, scale = (0.6, 1.0)),    # 随机裁剪缩放
        transforms.RandomRotation(degrees = 15),                    # 随机旋转，degrees = 15表示旋转角度范围为-15到15度
        transforms.ColorJitter(brightness = 0.4, contrast = 0.4),       # 颜色抖动
        transforms.ToTensor(),                                          # PIL图像 -> (C, H, W)浮点张量，并缩放到[0, 1]
        transforms.Normalize(mean = (0.2860, ), std = (0.3530, ))       # 归一化：FashionMNIST全局均值与标准差
    ])

    # 1.2 测试阶段：不做任何随机变换，保证评估口径固定
    test_augs = transforms.Compose([
        transforms.ToTensor(),                                          # PIL图像 -> (C, H, W)浮点张量，并缩放到[0, 1]
        transforms.Normalize(mean = (0.2860, ), std = (0.3530, ))       # 归一化：FashionMNIST全局均值与标准差
    ])
    return train_augs, test_augs

# 2.定义数据加载函数：augment开关控制训练集是否使用增广变换
# 参2：True表示使用增广变换，False表示不使用增广变换
def get_data_loaders(batch_size = 64, augment = True):
    train_augs, test_augs = get_transforms()       # 获取训练集和测试集的增广变换
    train_dataset = FashionMNIST(
        root = './notebooks/data', train = True, download = False, transform = train_augs if augment else test_augs)
    test_dataset = FashionMNIST(
        root = './notebooks/data', train = False, download = False, transform = test_augs)
    # 只取一部分数据保证运行速度：6k张训练 + 1k张测试
    train_dataset = Subset(train_dataset, range(6000))
    test_dataset = Subset(test_dataset, range(1000))
    train_loader = DataLoader(train_dataset, batch_size = batch_size, shuffle = True)
    test_loader = DataLoader(test_dataset, batch_size = batch_size, shuffle = False)
    return train_loader, test_loader


# 3.定义小型CNN：顺序为：Conv -> BN -> ReLU -> MaxPool
class SmallCNN(nn.Module):
    def __init__(self, num_classes = 10):
        super(SmallCNN, self).__init__()
        # 卷积层
        self.features = nn.Sequential(
            # 28 -> 14
            nn.Conv2d(1, 32, 3, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            # 14 -> 7
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        # 全连接层
        self.classifier = nn.Sequential(
            nn.Flatten(),           # 展平层：(N, 64, 7, 7) -> (N, 64 * 7 * 7) = (N, 3136)
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),            # 增广与Dropout都是抑制过拟合的手段，这里叠加使用做对照
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        return self.classifier(self.features(x))


# 4.定义训练一个epoch与测试的函数
def train_one_epoch(model, train_loader, critetion, optimizer, device):
    model.train()           # 设置模型为训练模式：BN用当前batch统计量，Dropout生效
    total_loss, total_num = 0.0, 0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        y_pred = model(x)       # 模型预测
        loss = critetion(y_pred, y)         # 计算loss
        # 梯度清零 + 反向传播 + 梯度更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.sum().item() * x.shape[0]
        total_num += x.shape[0]
    return total_loss /total_num            # 返回这一轮的平均train loss

def evaluate(model, loader,device):
    model.eval()        # 测试模式：BN层改用running统计量，Dropout关闭
    correct, total = 0, 0
    with torch.no_grad():       # 禁用梯度计算，提升运行效率
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            y_pred = model(x).argmax(dim = 1)
            correct += (y_pred == y).sum().item()
            total += y.shape[0]
        return correct /total           # 返回正确率test acc


# 5.可视化：把原图和四种变换后的结果存成一张网格图
def visualize_augmentation():
    print("=" * 60)
    print("1.增广效果可视化")
    print("=" * 60)
    base_da = FashionMNIST(root = './notebooks/data', train = True, transform = transforms.ToTensor(), download = False)
    img_tensor, label = base_da[0]      # 第一张图，标签9（T-shirt）
    pil_img = transforms.ToPILImage()(img_tensor)       # 还原成PIL图像才能喂给几何/颜色类变换

    # 每个变换各跑一次，收集成一行，第一列是原图做对照
    ops = {
        "原图": transforms.Lambda(lambda x: x),
        "翻转": transforms.RandomHorizontalFlip(1.0),                       # p = 1.0强制翻转，便于对比
        "裁剪": transforms.RandomResizedCrop(28, (0.6, 0.8)),     # 裁掉一部分再放大回原尺寸
        "旋转": transforms.RandomRotation(30),            # 固定转30度左右
        "颜色": transforms.ColorJitter(brightness = 0.6, contrast = 0.6)     # 只动明暗，不动形状
    }
    grid = [transforms.ToTensor()(op(pil_img)) for op in ops.values()]      # 5张(1, 28, 28)
    out = torch.stack(grid)          # (5, 1, 28, 28) -> nrow = 5即横排一行
    save_path = './pytorch/Day42/augmentation_demo.png'
    save_image(out, save_path, nrow = 5)
    print(f"原图标签：{label} 依次经过：{' -> '.join(ops.keys())}")
    print(f"已保存对比图：{save_path}（请打开肉眼看差异，这是唯一能看清增广效果的方式）")


# 6.主函数：只做一件事--对比有无增广，重点看train_acc和test_acc的差距
def main():
    # 1.设置设备与超参数
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("Training on", device)
    lr, epochs = 0.01, 5
    criterion = nn.CrossEntropyLoss()

    # 2.先出可视化，直观感受四种手段各自改变了什么
    visualize_augmentation()
    print("增广效果可视化已完成，请打开保存的图片查看")

    # 3.参数量一行带过：增广不改变模型结构，只改变输入数据（与Day41的BN形成对比）
    print("=" * 60)
    print("2.参数量检查")
    print("=" * 60)
    print(f"总参数量：{sum(p.numel() for p in SmallCNN().parameters()):,}（有无增广完全相同）")
    print()

    # 4.训练对比：两个模型只差"训练集要不要做增广这一个变量"
    print("=" * 60)
    print(f"3.有 / 无增广训练对比（FashionMNIST 6000张训练 / 1000张测试，lr = {lr}，epochs = {epochs}）")
    print("=" * 60)
    results = {}
    for augment in (True, False):
        name = '有增广' if augment else '无增广'
        torch.manual_seed(42)       # 固定随机种子
        train_loader, test_loader = get_data_loaders(64, augment = augment)
        model = SmallCNN().to(device)
        optimizer = optim.Adam(model.parameters(), lr = lr)
        history = []
        print(f"---------- {name} ----------")
        for epoch in range(1, epochs + 1):
            train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
            train_acc = evaluate(model, train_loader, device)
            test_acc = evaluate(model, test_loader, device)
            history.append((epoch, train_loss, train_acc, test_acc))
            print(f"epoch {epoch} train_loss = {train_loss:.4f} train_acc = {train_acc:.4f} test_acc = {test_acc:.4f} gap = {train_acc - test_acc:+.4f}")
        results[name] = history
        print()

    # 5.汇总：只看gap的变化趋势，不看绝对精度
    print("=" * 60)
    print(f"4.结果汇总（gap = train_acc - test_acc，越大说明过拟合越重）")
    print("=" * 60)
    print(f"{'epoch':<8}{'无增广 train':>13}{'无增广 test':>13}{'gap':>10}{'有增广 train':>13}{'有增广 test':>13}{'gap':>10}")
    for i in range(epochs):
        no_aug = results['无增广'][i]
        aug = results['有增广'][i]
        print(f"{i + 1:<8}{no_aug[1]:>13.4f}{no_aug[2]:>13.4f}{no_aug[1] - no_aug[2]:>10.4f}{aug[1]:>13.4f}{aug[2]:>13.4f}{aug[1] - aug[2]:>10.4f}")

    print()
    print("结论：增广会让train_acc下降（样本变难了），但test_acc更高、gap明显收窄，说明增广是用数据的多样性换泛化能力。")


# 7.测试
if __name__ == "__main__":
    main()

