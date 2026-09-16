"""本程序用于模拟训练与验证流程"""

# 导包
import torch
import torch.nn as nn
import torch.optim as optim
import time
from model import ConvClassifier


# 1.定义函数，模拟构建(Batch_size = 32, Channel = 1, Height = 28, Width = 28)的图像数据与标签
def train_demo():
    """模拟构建(Batch_size = 32, Channel = 1, Height = 28, Width = 28)的图像数据与标签"""
    dummy_inputs = torch.rand(32, 1, 28, 28)
    dummy_labels = torch.randint(0, 10, (32,))

    model = ConvClassifier(num_classes = 10)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr = 1e-3)

    model.train()
    for epoch in range(1, 11):
        # 定义变量，记录：总损失，总样本数据量，预测正确样本个数，训练（开始）时间
        total_loss, total_samples, total_correct, start = 0.0, 0, 0, time.time()
        # 模型预测
        outputs = model(dummy_inputs)
        # 计算损失
        loss = criterion(outputs, dummy_labels)

        # 梯度清零 + 反向传播 + 参数更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 计算正确数
        total_correct += (torch.argmax(outputs, dim=-1) == dummy_labels).sum()
        total_loss += loss.item() * len(dummy_labels)
        total_samples += len(dummy_labels)

        print(f"Epoch: {epoch} / 10, Loss: {loss.item():.4f}, Acc: {total_correct / total_samples:.4f}, Time: {time.time() - start:.2f}s")

    # 保存模型参数
    torch.save(model.state_dict(), './pytorch/Day34/CNN_Image_Classification/model/demo_model.pth')

# 2.测试
if __name__ == "__main__":
    train_demo()