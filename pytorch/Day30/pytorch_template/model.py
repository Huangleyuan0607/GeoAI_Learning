"""
本文件为网络结构定义模块，用于编写模块化的神经网络定义模板。
"""


# 导包
import torch
import torch.nn as nn
from config import config


class ClassificationMLP(nn.Module):
    """通用多层感知机模板"""
    def __init__(self, input_dim = config.INPUT_DIM, num_classes = config.NUM_CLASSES):
        super(ClassificationMLP, self).__init__()

        # 定义层结构
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),       # 隐藏层1
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(64, 32),      # 隐藏层2
            nn.ReLU(),

            nn.Linear(32, num_classes),         # 输出层
        )

    def forward(self, x):
        return self.net(x)