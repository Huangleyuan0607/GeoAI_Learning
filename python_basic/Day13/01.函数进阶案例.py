# 函数进阶 - 案例
# 案例1：计算n的阶乘
# 递归调用（先层层递进，再逐层回归）：指的是在函数中自己调用自己的情况 ---> 一定得有终结点，此处终结点就是n = 1
"""
jc(10) = 10 * jc(9) = 10 * 362880 = 3628800
jc(9) = 9 * jc(8) = 9 * 40320 = 362880
jc(8) = 8 * jc(7) = 8 * 5040 = 40320
jc(7) = 7 * jc(6) = 7 * 720 = 5040
jc(6) = 6 * jc(5) = 6 * 120 = 720
jc(5) = 5 * jc(4) = 5 * 24 = 120
jc(4) = 4 * jc(3) = 4 * 6 = 24
jc(3) = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1
"""

# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n - 1)
#
# result = jc(10)     # 如果没有设置终结点，则会报错：RecursionError: maximum recursion depth exceeded
# print(result)


# 案例2：电商订单计算器。定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
# 具体规则如下:
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。
def calc_order_cost(*args, coupon = 0, score = 0, express):     # 由于积分和优惠券不是必选项 ，所以可以设置默认值，从而不用在调用函数传递
    """
    根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
    :param args:商品信息(商品名、价格、数量) ---> 如：("鼠标", 188, 2);("键盘", 388, 1)
    :param coupon:优惠券
    :param score:积分
    :param express:运费
    :return:订单总金额
    """
    # 订单总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1、计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]       # 使用推导式快速获取商品总金额
    total_cost = sum(total_price)

    # 2、扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    else:
        print("暂不满足优惠券使用情况~")

    # 3、扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:     # 因为积分只能整百抵扣，所以使用整除符号：//
        total_cost -= score // 100
    else:
        print("暂不满足积分抵扣使用情况~")

    # 4、添加运费
    total_cost += express

    return total_cost

# 测试 ---> 不定长位置参数后的参数需要用关键字参数来传递
total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 3), ("手机", 4999, 1), coupon = 10, score = 4000, express = 9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 3), ("手机", 4999, 1), express = 9.9)
print(total)





