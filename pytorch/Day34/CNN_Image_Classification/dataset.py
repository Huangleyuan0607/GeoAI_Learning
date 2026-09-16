""" 本程序用于数据预处理与加载器构建"""


# 导包
import torch
from torch.utils.data import DataLoader, TensorDataset
from torchvision import transforms


# 1.定义函数，模拟构建Dataset与DataLoader流水线
def get_data_loaders(batch_size = 32):
    """
    模拟构建Dataset与DataLoader流水线
    包含简单的Resize、ToTensor和Normalize预处理逻辑
    """
    # 1.定义数据预处理流水线Pipeline
    # 参1：列表，包含多个预处理操作
    transform = transforms.Compose([
        transforms.Normalize(mean = [0.5], std = [0.5])     # 图像张量归一化至[-1, 1]
    ])

    # 2.模拟1000张单通道28x28的图像数据及对应的10分类标签
    dummy_x = torch.randn(1000, 1, 28, 28)
    dummy_y = torch.randint(0, 10, (1000,))
    # 对模拟数据应用归一化变换
    dummy_x = transform(dummy_x)

    # 3.划分训练集(800张)和测试集(200张)
    train_dataset = TensorDataset(dummy_x[:800], dummy_y[:800])
    test_dataset = TensorDataset(dummy_x[800:], dummy_y[800:])

    # 4.构建DataLoader批处理加载器
    train_loader = DataLoader(train_dataset, batch_size = batch_size, shuffle = True)
    test_loader = DataLoader(test_dataset, batch_size = batch_size, shuffle = False)

    return train_loader, test_loader


# 2.测试
if __name__ == '__main__':
    train_loader, test_loader = get_data_loaders(batch_size = 32)
    # 打印训练集和测试集批数     800 / 32 = 25                   200 / 32 = 6.25 -> 7
    print(f"Train batches: {len(train_loader)}, Test batches: {len(test_loader)}")
















