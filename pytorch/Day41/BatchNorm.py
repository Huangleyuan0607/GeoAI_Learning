# 导包
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Subset         # Subset用于切分数据集，这里用于切分训练集和测试集的数量，提升运行速度
from torchvision.datasets import FashionMNIST
from torchvision.transforms import ToTensor


# 1.从零实现批量归一化层BatchNorm
class MyBatchNorm(nn.Module):
    """批量归一化：训练阶段用当前batch的统计量，推理阶段用累积的滑动平均统计量"""
    # 参1：特征数（卷积层传通道数，全连接层传特征数）；参2：数据维度（4表示卷积层的(N, C, H, W)，2表示全连接层的(N, C)）
    # 参3：放在分母上的小参数，避免除零；参4：momentum：滑动平均的动量
    def __init__(self, num_features, num_dims = 4, eps = 1e-5, momentum = 0.1):
        super(MyBatchNorm, self).__init__()
        # 1.定义可学习的缩放参数gamma和平移参数beta，对标准化时被抹掉的信息做补偿
        if num_dims == 2:           # 全连接层
            shape = (1, num_features)               # 全连接层输出形状：(N, C)
        else:                       # 卷积层
            shape = (1, num_features, 1, 1)         # 卷积层输出形状：(N, C, H, W)
        self.gamma = nn.Parameter(torch.ones(shape))
        self.beta = nn.Parameter(torch.zeros(shape))

        # 2.定义训练过程中的累计滑动平均统计量（不参与梯度更新，但要跟着模型加载到GPU上）
        # register_buffer 用来把一个张量注册为模型的缓冲区，不是可训练参数，属于模型状态，随模型移动，但不参与梯度计算
        self.register_buffer('moving_mean', torch.zeros(shape))     # 初始时假设全局均值为0
        self.register_buffer('moving_var', torch.ones(shape))       # 初始时假设全局方差为1
        self.num_dims = num_dims
        self.eps = eps
        self.momentum = momentum

    def forward(self, x):
        # 1.推理阶段：直接用训练时累计的running mean / running var，不再依赖当前batch
        if not self.training:
            x_hat = (x - self.moving_mean) / torch.sqrt(self.moving_var + self.eps)

        # 2.训练阶段：用当前batch的统计量做标准化
        else:
            # 2.1 按通道求均值和方差：4维在(N, H, W)上求，二维在N上求
            if self.num_dims == 2:       # 全连接层
                mean = x.mean(dim = 0)
                var = ((x - mean) ** 2).mean(dim = 0)
            else:                       # 卷积层
                mean = x.mean(dim = (0, 2, 3), keepdim = True)
                var = ((x - mean) ** 2).mean(dim = (0, 2, 3), keepdim = True)
            # 2.2 标准化
            x_hat = (x - mean) / torch.sqrt(var + self.eps)
            # 2.3 缩放和平移
            self.moving_mean = self.momentum * self.moving_mean + (1.0 - self.momentum) * mean.detach()
            self.moving_var = self.momentum * self.moving_var + (1.0 - self.momentum) * var.detach()

         # 3.缩放 + 平移
        return self.gamma * x_hat + self.beta       # y = γ * x_hat + β


# 2.定义小型CNN（LeNet结构）：use_bn控制是否在卷积 / 全连接层后接批量归一化
class SmallCNN(nn.Module):
    # 参2：是否使用BN层；参3：分类类别数（输出层的输出通道数）
    def __init__(self, use_bn = False, num_classes = 10):
        super(SmallCNN, self).__init__()
        self.use_bn = use_bn
        # 1.卷积部分：Conv -> (BN) -> ReLU -> Maxpool
        self.conv1 = nn.Conv2d(1, 6, 5, padding = 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.relu = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        # 2.全连接层部分
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, num_classes)
        # 3.BN层：只有use_bn = True时才创建（用从零实现的MyBatchNorm，也可以使用nn.BatchNorm2d / nn.BatchNorm1d）
        if use_bn:
            self.bn1 = MyBatchNorm(6)               # num_dims默认是4，即卷积层，输出是4维(N, C, H, W)
            self.bn2 = MyBatchNorm(16)              # num_dims默认是4，即卷积层，输出是4维(N, C, H, W)
            self.bn3 = MyBatchNorm(120, num_dims = 2)       # 全连接层输出是2维(N, C)
            self.bn4 = MyBatchNorm(84, num_dims = 2)       # 全连接层输出是2维(N, C)

    def forward(self, x):
        # 1.卷积块1：Conv(1->6) + Maxpool, 28x28 -> 14x14
        x = self.conv1(x)
        if self.use_bn:     # 是否使用BN层
            x = self.bn1(x)
        x = self.relu(x)
        x = self.pool1(x)

        # 2.卷积块2：Conv(6->16) + Maxpool, 14x14 -> 5x5
        x = self.conv2(x)
        if self.use_bn:     # 是否使用BN层
            x = self.bn2(x)
        x = self.relu(x)
        x = self.pool1(x)

        # 3.展平层
        x = x.reshape(x.shape[0], -1)       # (N, C, H, W) -> (N, C * H * W)

        # 4.全连接层：Linear -> (BN) -> ReLU
        x = self.fc1(x)         # 全连接层1
        if self.use_bn:     # 是否使用BN层
            x = self.bn3(x)
        x = self.relu(x)
        x = self.fc2(x)         # 全连接层2
        if self.use_bn:  # 是否使用BN层
            x = self.bn4(x)
        x = self.relu(x)
        x = self.fc3(x)         # 输出层
        return x


# 3.定义数据加载函数（复用项目里已有的FashionMNIST，取子集保证运行效率）
def get_data_loaders(batch_size = 64):
    transform = ToTensor()
    # 数据已在notebooks/data目录下，download = False表示不再下载
    # 参1：数据集路径；参2：是否是训练集；参3：数据预处理 -> 张量数据；参4：是否联网下载数据集（这里我们已经下载到了本地）
    train_dataset = FashionMNIST(root = './notebooks/data', train = True, transform = transform, download = False)
    test_dataset = FashionMNIST(root = './notebooks/data', train = False, transform = transform, download = False)
    # 只取一部分数据保证运行速度：6k张训练 + 1k张测试
    train_dataset = Subset(train_dataset, range(6000))
    test_dataset = Subset(test_dataset, range(1000))
    train_loader = DataLoader(train_dataset, batch_size = batch_size, shuffle = True)       # shuffle参数True表示打乱数据顺序
    test_loader = DataLoader(test_dataset, batch_size = batch_size, shuffle = False)       # shuffle参数False表示不打乱数据顺序
    return train_loader, test_loader


# 4.定义训练一个epoch与测试函数
# 参1：模型；参2：数据加载器；参3：损失函数；参4：优化器；参5：设备
def train_one_epoch(model, train_loader, criterion, optimizer, device):
    model.train()       # 切换模型状态到训练模式
    total_loss, total_num = 0.0, 0          # 定义总损失和总个数
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        y_pred = model(x)       # 模型预测（前向传播）
        loss = criterion(y_pred, y)
        # 梯度清零 + 反向传播 + 梯度更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # 计算总损失和总个数
        total_loss += loss.item() * x.shape[0]          # x.shape[0]就是batch_size，表示当前批的样本个数
        total_num += x.shape[0]                         # x.shape[0]就是batch_size，表示当前批的样本个数
    return total_loss / total_num       # 返回平均损失

def evaluate(model, test_loader, device):       # 测试函数
    model.eval()        # 切换模型状态到测试模式，BN层改用running统计量
    correct, total = 0, 0       # 定义总正确数和总个数
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            y_pred = model(x).argmax(dim = 1)           # 模型预测，这里的argmax函数用于获取最大值的索引，作为预测结果
            correct += (y_pred == y).sum().item()       # 计算总正确数
            total += y.shape[0]       # 计算总个数
    return correct / total      # 返回正确率


# 5.定义主函数
def main():
    # 1.设置随机种子、设备与其他预先设定的参数
    torch.manual_seed(42)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')       # 有显用显，无显用C
    print("Training on", device)        # 打印训练设备是显卡还是CPU
    lr, epochs = 0.1, 5         # 定义训练轮数和学习率
    train_loader, test_loader = get_data_loaders(64)        # 每个样本数量设置为64
    criterion = nn.CrossEntropyLoss()       # 多分类任务因此选用多分类交叉熵损失函数

    # 2.验证从零实现的BN层：标准化后每个通道均值 ≈ 0，方差 ≈ 1
    print("=" * 60)
    print("1.从零实现的BN层验证")
    print("=" * 60)
    bn = MyBatchNorm(3)     # 设置通道数为3
    x = torch.randn(4, 3, 8, 8) * 5 + 2     # 人为放大并平移，模拟"分布跑偏"的中间层输出
    y = bn(x)       # y为BN层的输出
    # 输出标准化前的统计量
    print(f"标准化前 各通道均值：{[round(v, 4) for v in x.mean(dim = (0, 2, 3)).tolist()]}")
    # unbiased = False表示计算的是有偏方差，即除以N而不是N−1
    print(f"标准化前 各通道方差：{[round(v, 4) for v in x.var(dim = (0, 2, 3), unbiased = False).tolist()]}")
    # 输出的统计量验证了从零实现的 BN 层功能正确：标准化后各通道均值 ≈ 0，方差 ≈ 1。
    # 由于归一化时减去了该通道的均值，所以y的均值在数值精度内为 0
    print(f"标准化后 各通道均值：{[round(v, 4) for v in y.mean(dim=(0, 2, 3)).tolist()]}")
    # 归一化时除以了标准差，所以y的方差为1
    print(f"标准化后 各通道方差：{[round(v, 4) for v in y.var(dim=(0, 2, 3), unbiased=False).tolist()]}")

    # 3.对比训练阶段和推理阶段的统计量来源
    print()
    print("=" * 60)
    print("2.训练阶段和推理阶段的统计量来源")
    print("=" * 60)
    bn_demo = MyBatchNorm(3)
    print(f"训练前 running mean：{[round(v, 4) for v in bn_demo.moving_mean.reshape(-1).tolist()]}")
    print(f"训练前 running var：{[round(v, 4) for v in bn_demo.moving_var.reshape(-1).tolist()]}")
    bn_demo.train()     # 训练模式：用当前batch统计量做标准化，并更新running统计量
    for _ in range(5):          # 模拟训练5个epoch
        bn_demo(torch.randn(4, 3, 8, 8) * 5 + 2)
    print(f"训练5个batch后 running mean：{[round(v, 4) for v in bn_demo.moving_mean.reshape(-1).tolist()]}")
    print(f"训练5个batch后 running var：{[round(v, 4) for v in bn_demo.moving_var.reshape(-1).tolist()]}")
    bn_demo.eval()      # 推理模式：不再看当前batch，直接用running统计量
    x_test = torch.randn(2, 3, 8, 8) * 5 + 2
    print(f"推理阶段：输入均值 {x_test.mean().item():.4f} -> 用running统计量标准化后输出均值 {bn_demo(x_test).mean().item():.4f}")

    # 4.参数量对比（BN层每个通道多2个可学习参数：gamma和beta）
    print()
    print("=" * 60)
    print("3.有无BN的模型参数量对比")
    print("=" * 60)
    for use_bn in (False, True):        # 第一次不使用BN，第二次使用BN
        net = SmallCNN(use_bn = use_bn)         # 实体化网络
        total = sum(p.numel() for p in net.parameters())            # 计算总参数量
        print(f"use_bn = {str(use_bn):<6} 总参数量：{total:,}")

    # 5.训练对比：同样数据和学习率，两个模型只差一组BN层
    print()
    print("=" * 60)
    print(f"4.训练对比（FashionMNIST 6000张训练 / 1000张测试，lr = {lr}，epochs = {epochs}）")
    print("=" * 60)
    results = {}        # 定义存放两种结果的字典，因为字典的索引可以是字符串
    for use_bn in (False, True):        # 第一次不使用BN，第二次使用BN
        name = "有BN" if use_bn else "无BN"
        torch.manual_seed(42)       # 固定随机种子
        model = SmallCNN(use_bn = use_bn).to(device)
        optimizer = optim.SGD(model.parameters(), lr = lr)      # 定义优化器，采用SGD随机梯度下降
        history = []
        print(f"---------- {name} ----------")
        for epoch in range(1, epochs + 1):
            train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
            test_acc = evaluate(model, test_loader, device)
            history.append((train_loss, test_acc))
            print(f"epoch {epoch} train_loss = {train_loss:.4f} test_acc = {test_acc:.4f}")
        results[name] = history         # 分别存放有无BN的模型运行结果

    # 6.汇总对比
    print()
    print("=" * 60)
    print("5.训练结果汇总")
    print("=" * 60)
    print(f"{'epoch':<8}{'无BN loss':>12}{'无BN acc':>12}{'有BN loss':>12}{'有BN acc':>12}")        # 打印结果表头
    for i in range(1, epochs + 1):
        no_bn_loss, no_bn_acc = results['无BN'][i - 1]
        bn_loss, bn_acc = results['有BN'][i - 1]
        print(f"{i:<8}{no_bn_loss:>12.4f}{no_bn_acc:>12.4f}{bn_loss:>12.4f}{bn_acc:>12.4f}")

    print()
    print("结论：同样的数据和超参数下，有BN层的网络收敛更快，曲线更平稳，说明BN层确实能加速训练，稳定梯度")

# 6.测试
if __name__ == "__main__":
    main()