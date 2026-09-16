"""本程序用于模型测试与评估"""


# 导包
import torch
from model import ConvClassifier


# 1.定义函数，进行模型测试与评估
def test_demo():
    dummy_inputs = torch.randn(10, 1, 28, 28)
    dummy_labels = torch.randint(0, 10, (10, ))

    # 创建模型对象
    model = ConvClassifier(num_classes = 10)

    # 加载模型权重
    model.load_state_dict(torch.load('./pytorch/Day34/CNN_Image_Classification/model/demo_model.pth'))

    # 切换测试模式
    model.eval()

    with torch.no_grad():
        # 模型测试
        outputs = model(dummy_inputs)
        _, y_pred = torch.max(outputs, 1)
        total_correct = (y_pred == dummy_labels).sum().item()
        accuracy = total_correct / dummy_labels.size(0)
        print(f"Test Acc: {accuracy * 100:.2f}%")

# 2.测试
if __name__ == "__main__":
    test_demo()