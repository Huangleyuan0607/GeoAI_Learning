"""
本文件为全局配置模块，用于集中配置批次大小（Batch Size）、学习率（Learning Rate）、训练轮数（Epochs）及设备选择（CUDA/CPU）。
"""

# 导包
import torch

# 配置
class Config:
    # 超参数配置
    BATCH_SIZE = 64
    LEARNING_RATE = 0.001
    EPOCHS = 10

    # 数据集配置
    NUM_SAMPLES = 1000
    INPUT_DIM = 20
    NUM_CLASSES = 2

    # 路径与设备配置
    MODEL_SAVE_PATH = "./pytorch/Day30/model/best_model.pth"
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

config = Config()