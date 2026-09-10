"""
案例：
    演示基础的图像操作

图像分类：
    二值图：        1通道，每个像素点由0，1组成
    灰度图：        1通道，每个像素点的范围：[0, 255]
    索引图：        1通道，每个像素点的范围：[0, 255]，像素点表示颜色表的索引
    RGB真彩图：     3通道，Red，Green，Blue，红绿蓝

涉及到的API：
    imshow()：基于HWC展示图像
    imread()：读取图像，获取HWC
    imsave()：基于HWC，保存图片
"""

# 导包
import numpy as np
import matplotlib.pyplot as plt
import torch


# 1.定义函数，绘制：全黑，全白图
def dm01():
    # 1.定义全黑图片：像素点越接近0越黑，越接近255越白
    # HWC：H高度，W宽度，C通道数
    img1 = np.zeros((200, 200, 3))
    # print(f"img1: {img1}")

    # 2.绘制全黑图片
    plt.imshow(img1)
    plt.axis('off')         # 关闭坐标系
    plt.show()

    # 3.定义全白图片
    img2 = np.full((200, 200, 3), 255)
    # print(f"img2: {img2}")

    # 4.绘制全白图片
    plt.imshow(img2)
    plt.axis('off')         # 关闭坐标系
    plt.show()

# 2.定义函数，加载图片
def dm02():
    # 1.读取图片
    img1 = plt.imread('./pytorch/Day30/data/wallhaven-rr2591.jpg')
    # print(f"img1: {img1}")
    print(f"img1.shape: {img1.shape}")      # (1440, 2560, 3)分别代表H高度、W宽度、C通道数

    # 2.保存图像
    # plt.imsave('./pytorch/Day30/data/wallhaven-rr2591_copy.png', img1)

    # 3.展示图像
    plt.imshow(img1)
    plt.axis('off')         # 关闭坐标系
    plt.show()

 # 3.测试
if __name__ == '__main__':
    # dm01()
    dm02()











