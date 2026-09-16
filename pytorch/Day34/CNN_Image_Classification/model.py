"""本程序用于定义CNN分类模型"""


# 导包
import torch
import torch.nn as nn


# 1.定义类，用于图像分类的Simple CNN网络
class ConvClassifier(nn.Module):
    """用于图像分类的Simple CNN网络"""
    def __init__(self, num_classes = 10):
        super(ConvClassifier, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding = 1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),     # (B, 16, 14, 14)
            nn.Conv2d(16, 32, 3, padding = 1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),     # (B, 32, 7, 7)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
