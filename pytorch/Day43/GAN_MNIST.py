import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.utils as vutils


# 设置超参数
batch_size = 128
z_dim = 100          # 噪声向量维度
lr = 0.0002
beta1 = 0.5
num_epochs = 50
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
os.environ['TORCHVISION_MNIST_URL'] = 'https://ossci-datasets.s3.amazonaws.com/mnist/'

# 固定随机种子
torch.manual_seed(42)

# 创建输出目录
os.makedirs("gan_output", exist_ok=True)

# 数据加载
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [0,1] -> [-1,1]
])

train_dataset = torchvision.datasets.MNIST(
    root="./pytorch/Day43/data",
    train=True,
    transform=transform,
    download=True
)

train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=0  # Windows 下建议设为 0
)

# 生成器 G03
class Generator(nn.Module):
    def __init__(self, z_dim=100):
        super(Generator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(z_dim, 256),
            nn.ReLU(True),
            nn.Linear(256, 512),
            nn.ReLU(True),
            nn.Linear(512, 1024),
            nn.ReLU(True),
            nn.Linear(1024, 28 * 28),
            nn.Tanh()  # 输出范围 [-1, 1]
        )

    def forward(self, z):
        img = self.net(z)
        return img.view(img.size(0), 1, 28, 28)

# 判别器 D
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(28 * 28, 1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()  # 输出概率
        )

    def forward(self, x):
        x = x.view(x.size(0), -1)
        return self.net(x)

# 初始化模型、损失、优化器
G = Generator(z_dim).to(device)
D = Discriminator().to(device)

criterion = nn.BCELoss()

optimizer_G = optim.Adam(G.parameters(), lr=lr, betas=(beta1, 0.999))
optimizer_D = optim.Adam(D.parameters(), lr=lr, betas=(beta1, 0.999))

# 固定噪声，用于每个 epoch 结束后可视化生成效果
fixed_noise = torch.randn(64, z_dim, device=device)

# 训练循环
for epoch in range(num_epochs):
    for i, (real_imgs, _) in enumerate(train_loader):
        real_imgs = real_imgs.to(device)
        b_size = real_imgs.size(0)

        # 真实样本标签为 1，假样本标签为 0
        real_labels = torch.ones(b_size, 1, device=device)
        fake_labels = torch.zeros(b_size, 1, device=device)

        # 1. 训练判别器 D
        optimizer_D.zero_grad()

        # 真实样本
        output_real = D(real_imgs)
        loss_D_real = criterion(output_real, real_labels)

        # 生成假样本
        z = torch.randn(b_size, z_dim, device=device)
        fake_imgs = G(z)
        output_fake = D(fake_imgs.detach())  # detach 避免梯度传到 G03
        loss_D_fake = criterion(output_fake, fake_labels)

        # 判别器总损失
        loss_D = loss_D_real + loss_D_fake
        loss_D.backward()
        optimizer_D.step()

        # 2. 训练生成器 G03
        optimizer_G.zero_grad()

        z = torch.randn(b_size, z_dim, device=device)
        fake_imgs = G(z)
        output_fake = D(fake_imgs)  # 不 detach，梯度会传到 G03

        # 生成器希望判别器把假样本判为真，所以标签用 real_labels
        loss_G = criterion(output_fake, real_labels)
        loss_G.backward()
        optimizer_G.step()

        # 打印日志
        if i % 100 == 0:
            print(
                f"[Epoch {epoch}/{num_epochs}] "
                f"[Batch {i}/{len(train_loader)}] "
                f"[D loss: {loss_D.item():.4f}] "
                f"[G loss: {loss_G.item():.4f}]"
            )

    # 每个 epoch 保存生成图片
    with torch.no_grad():
        fake = G(fixed_noise)
        vutils.save_image(
            fake,
            f"./pytorch/Day43//gan_output/epoch_{epoch+1:03d}.png",
            normalize=True
        )

print("训练完成！生成图片已保存到 gan_output/ 目录。")