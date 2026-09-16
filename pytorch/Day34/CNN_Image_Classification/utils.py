"""本程序用于定义辅助工具函数：准确率计算与计算设备选择"""


# 导包
import torch


# 1.定义函数，用于：获取当前可用的计算设备(GPU / CPU)
def get_device():
    """获取当前可用的计算设备(GPU / CPU)"""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2.定义函数，用于：计算当前Batch的分类预测准确率
def calculate_accuracy(outputs, targets):
    """
    计算当前Batch的分类预测准确率
    :param outputs: 模型的预测输出，形状为(Batch_size, Num_classes)
    :param targets: 真实标签，形状为(Batch_size, )
    """
    _, y_pred = torch.max(outputs, dim = 1)
    correct = (y_pred == targets).sum().item()
    return correct / targets.size(0)

# 3.测试
if __name__ == "__main__":
    device = get_device()
    print(f"当前可用的计算设备为：{device}")
