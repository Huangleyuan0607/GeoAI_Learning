"""
本文件为数据加载模块，用于编写通用的 Dataset 与 DataLoader 数据加载封装模板。
"""

# 导包
import torch
from torch.utils.data import Dataset, DataLoader
from config import config


class SyntheticDataset(Dataset):
    """自定义合成数据集模板"""

    # 初始化时生成数据
    def __init__(self, num_samples = 1000, input_dim = 20, num_classes = 2):
        # 随机生成模拟特征与标签
        self.x = torch.randn(num_samples, input_dim)
        self.y = torch.randint(0, num_classes, (num_samples,))

    # 返回样本数量
    def __len__(self):
        return len(self.x)

    # 根据索引返回样本
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


def get_dataloaders():
    dataset = SyntheticDataset(config.NUM_SAMPLES, config.INPUT_DIM, config.NUM_CLASSES)

    # 简单划分8:2训练集与验证集
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size = config.BATCH_SIZE, shuffle = True)
    val_loader = DataLoader(val_dataset, batch_size = config.BATCH_SIZE, shuffle = False)

    return train_loader, val_loader















