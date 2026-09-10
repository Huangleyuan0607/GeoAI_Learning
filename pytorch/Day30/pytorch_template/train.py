"""
本文件为训练主程序，用于编写包含 Loss 记录、Acc 评估及最佳权重保存的标准训练与测试循环逻辑。
"""


# 导包
import torch
import torch.nn as nn
import torch.optim as optim
from config import config
from dataset import get_dataloaders
from model import ClassificationMLP


def train_epoch(model, train_loader, criterion, optimizer, device):
    model.train()       # 切换模型状态
    running_loss = 0.0
    correct = 0
    total = 0

    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)       # 把inputs和labels都移动到指定的device上，通常是GPU或CPU。

        # 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # 梯度清零 + 反向传播 + 优化参数
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 累加损失值 -> 经过整个epoch后，running_loss就是所有样本的总损失之和。
        running_loss += loss.item() * inputs.size(0)        # 因为loss是平均损失，乘以样本数就还原成这个batch的总损失。
        # 第一个是最大值（这里用 _ 忽略）；第二个是最大值所在的索引，赋给preds
        _, preds = torch.max(outputs, 1)        # 沿维度1（类别维度）取最大值
        correct += (preds == labels).sum().item()       # preds == labels逐元素比较，返回布尔张量，True 表示预测正确。
        total += labels.size(0)     # labels.size(0)是当前batch的样本数。累加到total，得到到目前为止参与统计的总样本数。

    epoch_loss = running_loss / total
    epoch_acc =  correct / total
    return epoch_loss, epoch_acc


def evaluate(model, val_loader, criterion, device):
    model.eval()        # 切换模型状态
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for inputs, labels in val_loader:
            # 把inputs和labels都移动到指定的device上，通常是GPU或CPU。
            inputs, labels = inputs.to(device), labels.to(device)

            # 模型预测
            outputs = model(inputs)

            # 计算损失
            loss = criterion(outputs, labels)

            # 累加损失值 -> 经过整个epoch后，running_loss就是所有样本的总损失之和。
            running_loss += loss.item() * inputs.size(0)  # 因为loss是平均损失，乘以样本数就还原成这个batch的总损失。
            # 第一个是最大值（这里用 _ 忽略）；第二个是最大值所在的索引，赋给preds
            _, preds = torch.max(outputs, 1)  # 沿维度1（类别维度）取最大值
            correct += (preds == labels).sum().item()  # preds == labels逐元素比较，返回布尔张量，True 表示预测正确。
            total += labels.size(0)  # labels.size(0)是当前batch的样本数。累加到total，得到到目前为止参与统计的总样本数。

    val_loss = running_loss / total
    val_acc = correct / total
    return val_loss, val_acc


def main():
    print(f"使用设备：{config.DEVICE}")
    train_loader, val_loader = get_dataloaders()

    model = ClassificationMLP().to(config.DEVICE)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr = config.LEARNING_RATE)

    best_val_acc = 0.0

    for epoch in range(1, config.EPOCHS + 1):
        train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, config.DEVICE)
        val_loss, val_acc = evaluate(model, val_loader, criterion, config.DEVICE)


        print(f"Epoch [{epoch:02d}/{config.EPOCHS:02d}] "
              f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc*100:.2f}% "
              f"| Val Loss: {val_loss:.4f} | Val Acc: {val_acc*100:.2f}%")

        # 保存最佳模型权重
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), config.MODEL_SAVE_PATH)

# 测试
if __name__ == "__main__":
    main()
