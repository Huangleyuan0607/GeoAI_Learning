"""
案例：
    演示参数初始化的7种方式

参数初始化的目的：
    1.防止梯度消失或梯度爆炸
    2.提高收敛速度
    3.打破对称性

参数初始化的方式：
    无法打破对称性的：
        全0，全1，固定值（优点均为操作简单）
    可以打破对称性的：
        随机初始化，正态分布初始化，kaiming初始化，xavier初始化

总结：
    1.记忆kaiming初始化，xavier初始化，全0初始化
    2.关于初始化的选择上：
        激活函数ReLU及其系列：优先用kaiming
        激活函数非ReLU：优先用xavier
        如果是浅层网络：可以考虑使用随机初始化
"""

# 导包
import torch.nn as nn       # nn:neural network, 神经网络

# 1.均匀分布随机初始化
def test01():
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行随机初始化，从0-1均匀分布产生参数
    nn.init.uniform_(linear.weight)
    # 3.对偏置(b)进行随机初始化，从0-1均匀分布产生参数
    nn.init.uniform_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 2.固定值初始化
def test02():
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行固定值初始化，设置固定值为3
    nn.init.constant_(linear.weight, 3)
    # 3.对偏置(b)进行固定值初始化，设置固定值为3
    nn.init.constant_(linear.bias, 3)
    print(linear.weight.data)
    print(linear.bias.data)

# 3.全0初始化
def test03():
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行全0初始化
    nn.init.zeros_(linear.weight)
    # 3.对偏置(b)进行全0初始化
    nn.init.zeros_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 4.全1初始化
def test04():
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行全1初始化
    nn.init.ones_(linear.weight)
    # 3.对偏置(b)进行全1初始化
    nn.init.ones_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 5.正态分布随机初始化
def test05():
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行正态分布随机初始化
    nn.init.normal_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

# 6.kaiming初始化
def test06():
    # kaiming正态分布初始化
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行kaiming正态分布初始化
    nn.init.kaiming_normal_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

    # kaiming均匀分布初始化
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行kaiming均匀分布初始化
    nn.init.kaiming_uniform_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

# 7.xavier初始化
def test07():
    # xavier正态分布初始化
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行kaiming正态分布初始化
    nn.init.xavier_normal_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

    # xavier均匀分布初始
    # 1.创建一个线性层，输入维度5，输出维度3
    linear = nn.Linear(5, 3)
    # 2.对权重(w)进行kaiming正态分布初始化
    nn.init.xavier_uniform_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

# 测试
if __name__ == '__main__':
    # test01()      # 均匀分布随机初始化
    # test02()      # 固定值初始化
    # test03()      # 全0初始化
    # test04()      # 全1初始化
    # test05()      # 正态分布初始化
    # test06()      # kaiming初始化
    test07()      # xavier初始化









