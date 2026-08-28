"""
案例：
    演示梯度下降优化方法

梯度下降相关介绍：
    概述：
        梯度下降是结合本次损失函数的导数（作为梯度）基于学习率来更新权重的
    公式：
        W新 = W旧 - 学习率 * （本次的）梯度
    存在的问题：
        1.遇到平缓区，梯度下降（权重更新）可能会慢
        2.可能会遇到鞍点（梯度为0）
        3.可能会遇到局部最小值
    解决思路：
        从上述的学习率、梯度入手，进行优化，如：动量法Momentum，自适应学习率AdaGrad、RMSProp，自适应矩估计Adam

    动量法Momentum：
        公式：
            St = β * St-1 + (1 - β) * Gt
        解释：
            St：当前时刻指数移动加权平均结果
            β：调节权重系数，越大数据越平缓，历史指数移动加权平均权重越大，本次梯度权重越小
            St-1：历史指数移动加权平均结果
            Gt：本次计算出的梯度（不考虑历史梯度）
        加入动量法后的梯度更新公式：
            W新 = W旧 - 学习率 * St

    自适应学习率AdaGrad(Adaptive Gradient Estimation)：
        公式：
            累计平方梯度：
                St = St-1 + Gt * Gt
                解释：
                    St：累计平方梯度
                    St-1：历史累计平方梯度
                    Gt：本次梯度
            学习率：
                学习率 = 学习率 / (sqrt(St) + 小常数σ)
                解释：
                    小常数σ：1e-10，防止分母变为0
            梯度下降公式：
                W新 = W旧 - 调整后的学习率 * Gt
        缺点：
            可能会导致学习率过早过量地减低，导致模型训练后期学习率太小，较难找到最优解

    自适应学习率RMSProp(Root Mean Square Propagation) -> 可以看作是对AdaGrad做的优化，加入调和权重系数：
        公式：
            指数加权平均累计历史平方梯度：
                St = β * St-1 + (1 - β) * Gt * Gt
                解释：
                    St：累计平方梯度
                    St-1：历史累计平方梯度
                    Gt：本次梯度
                    β：调和权重系数
            学习率：
                学习率 = 学习率 / (sqrt(St) + 小常数σ)
                解释：
                    小常数σ：1e-10，防止分母变为0
            梯度下降公式：
                W新 = W旧 - 调整后的学习率 * Gt
        优点：
            RMSProp通过引入衰减系数β，控制历史梯度对历史梯度信息获取地多少

    自适应矩估计Adam(Adaptive Moment Estimation)：
        思路：
            即优化学习率，又优化梯度
        公式：
            一阶矩：算均值
                Mt = β1 * Mt-1 + (1 - β1) * Gt          # 充当梯度
                St = β2 * St-1 + (1 - β2) * Gt * Gt     # 充当学习率
            二阶矩：梯度的方差
                Mt^ = Mt / (1 - β1 ^ t)
                St^ = St / (1 - β2 ^ t)
            权重更新公式：
                W新 = W旧 - 学习率 / (sqrt(St^) + 小常数σ) * Mt^
        大白话翻译：
            Adam = RMSProp + Momentum

总结：如何选择梯度下降优化方法
    简单任务和较小的模型：SGD，动量法Momentum
    复杂任务或有大量数据：Adam
    需要处理稀疏数据或文本数据：AdaGrad、RMSProp
"""

# 导包
import torch
import torch.optim as optim

# 1.定义函数，演示：梯度下降优化方法 -> 动量法Momentum
def dm01_Momentum():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

    # 2.定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 3.创建优化器（函数对象） -> 基于SGD（随机梯度下降），加入参数momentum，就是动量法
    # 参1：待优化的参数列表；参2：学习率；参3：动量参数
    optimizer = optim.SGD(params = [w], lr = 0.01, momentum = 0.9)      # 细节：momentum = 0（默认），只考虑：本次梯度

    # 4.计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w}, w.grad:{w.grad}")

    # 5.重复上述步骤，第2次更新权重参数
    # 5.1 定义损失函数
    criterion = ((w ** 2) / 2.0)
    # 5.2 计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    # 5.3 打印结果
    print(f"w:{w}, w.grad:{w.grad}")

# 2.定义函数，演示：梯度下降优化方法 -> 自适应学习率AdaGrad
def dm02_AdaGrad():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

    # 2.定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 3.创建优化器（函数对象）
    # 思路1：基于SGD（随机梯度下降），加入参数momentum，就是动量法
    # 参1：待优化的参数列表；参2：学习率；参3：动量参数
    # optimizer = optim.SGD(params=[w], lr=0.01, momentum=0.9)  # 细节：momentum = 0（默认），只考虑：本次梯度

    # 思路2：基于AdaGrad(自适应学习率)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01）
    optimizer = optim.Adagrad(params = [w], lr = 0.01)

    # 4.计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w}, w.grad:{w.grad}")

    # 5.重复上述步骤，第2次更新权重参数
    # 5.1 定义损失函数
    criterion = ((w ** 2) / 2.0)
    # 5.2 计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    # 5.3 打印结果
    print(f"w:{w}, w.grad:{w.grad}")

# 3.定义函数，演示：梯度下降优化方法 -> 自适应学习率RMSProp
def dm03_RMSProp():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

    # 2.定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 3.创建优化器（函数对象）
    # 思路1：基于SGD（随机梯度下降），加入参数momentum，就是动量法
    # 参1：待优化的参数列表；参2：学习率；参3：动量参数
    # optimizer = optim.SGD(params=[w], lr=0.01, momentum=0.9)  # 细节：momentum = 0（默认），只考虑：本次梯度

    # 思路2：基于AdaGrad(自适应学习率)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01）
    # optimizer = optim.Adagrad(params=[w], lr=0.01)

    # 思路3：基于RMSProp(自适应学习率)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01），参3：调节权重系数（默认alpha = 0.99）
    optimizer = optim.RMSprop(params=[w], lr=0.01, alpha = 0.99)

    # 4.计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w}, w.grad:{w.grad}")

    # 5.重复上述步骤，第2次更新权重参数
    # 5.1 定义损失函数
    criterion = ((w ** 2) / 2.0)
    # 5.2 计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    # 5.3 打印结果
    print(f"w:{w}, w.grad:{w.grad}")

# 4.定义函数，演示：梯度下降优化方法 -> 自适应矩估计Adam
def dm04_Adam():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

    # 2.定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 3.创建优化器（函数对象）
    # 思路1：基于SGD（随机梯度下降），加入参数momentum，就是动量法
    # 参1：待优化的参数列表；参2：学习率；参3：动量参数
    # optimizer = optim.SGD(params=[w], lr=0.01, momentum=0.9)  # 细节：momentum = 0（默认），只考虑：本次梯度

    # 思路2：基于AdaGrad(自适应学习率)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01）
    # optimizer = optim.Adagrad(params=[w], lr=0.01)

    # 思路3：基于RMSProp(自适应学习率)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01），参3：调节权重系数（默认alpha = 0.99）
    # optimizer = optim.RMSprop(params=[w], lr=0.01, alpha=0.99)

    # 思路3：基于Adam(自适应矩估计)
    # 参1：待优化的参数列表；参2：学习率（默认lr = 0.01），参3：调节权重系数（betas = (梯度用的衰减系数，学习率用的衰减系数)）
    optimizer = optim.Adam(params=[w], lr=0.01, betas = (0.9, 0.999))       # betas = (梯度用的衰减系数，学习率用的衰减系数)

    # 4.计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w}, w.grad:{w.grad}")

    # 5.重复上述步骤，第2次更新权重参数
    # 5.1 定义损失函数
    criterion = ((w ** 2) / 2.0)
    # 5.2 计算梯度值：先做梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    # 5.3 打印结果
    print(f"w:{w}, w.grad:{w.grad}")

# 5.测试
if __name__ == "__main__":
    # dm01_Momentum()
    # dm02_AdaGrad()
    # dm03_RMSProp()
    dm04_Adam()

