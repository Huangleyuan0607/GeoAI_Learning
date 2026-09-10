"""
本文件为模型加载与推理评估模块，用于编写包含Loss记录、Acc评估及最佳权重保存的标准训练与测试循环逻辑。
"""


# 导包
import torch
from config import config
from model import ClassificationMLP


def load_and_predict():
    # 实例化模型并加载权重
    model = ClassificationMLP().to(config.DEVICE)
    model.load_state_dict(torch.load(config.MODEL_SAVE_PATH))
    model.eval()
    print("模型权重加载成功！")

    # 模拟单条样本推理
    dummy_input = torch.randn(1, config.INPUT_DIM).to(config.DEVICE)
    with torch.no_grad():
        output = model(dummy_input)
        probabilities = torch.softmax(output, dim = 1)
        pred_class = torch.argmax(probabilities, dim = 1).item()

    print(f"输入特征维度：{dummy_input.shape}")
    print(f"预测分类结果: Class {pred_class} (概率: {probabilities[0][pred_class].item():.4f})")


# 测试
if __name__ == "__main__":
    load_and_predict()
