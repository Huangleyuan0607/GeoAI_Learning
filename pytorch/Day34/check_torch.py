"""本程序用于检查Pytorch是CPU版还是GPU版"""

# 导包
import torch

print("=" * 40)
print("torch 版本:", torch.__version__)
print("编译 CUDA 版本:", torch.version.cuda)
print("CUDA 是否可用:", torch.cuda.is_available())
print("GPU 数量:", torch.cuda.device_count())
print("cuDNN 启用:", torch.backends.cudnn.enabled)

if torch.cuda.is_available():
    print("当前 GPU:", torch.cuda.get_device_name(0))
    print("计算能力:", torch.cuda.get_device_capability(0))
else:
    print("当前环境不能使用 CUDA GPU")

if torch.version.cuda is None:
    print("结论：安装的是 CPU 版 PyTorch")
else:
    print("结论：安装的是 CUDA 版 PyTorch")
print("=" * 40)