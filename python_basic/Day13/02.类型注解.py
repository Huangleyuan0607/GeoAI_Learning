# 类型注解
# 变量定义 - 未指定类型注解 ---> 类型推断：Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力，而无需开发者显式声明。
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count" : 2, "total" : 10}
goods = ("手机", 6999,1)

names.append("A")
# 类型推断只是起到语法提示作用，并不会影响程序运行的结果（Python是动态类型语言）。
names.append(10010)     # 因为Python解释器推断出names列表是存储str类型的列表，所以会提示警告，但也可以正常操作
names.append(10.01)
print(names)


# 变量定义 - 指定类型注解
a: int = 596
score: float = 98.5
hobby: str = "Python"
flag: bool = True
pic: None = None

names2: list[str | int] = ["A", "C", "E"]       # 这里的|表示or，指的是列表中元素可以是str或int类型数据
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count" : 2, "total" : 10}      # 指的是key类型为str，value类型为int
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("A")
names2.append(10010)
# 类型注解只是起到语法提示作用，并不会影响程序运行的结果（Python是动态类型语言）。
names2.append(10.01)    # 因为names2列表是指定了类型注解的，存储str和int类型的列表，所以会提示警告，但也可以正常操作
print(names2)


# 函数类型注解
def circle_area_len(r: float )-> tuple[float, float]:    # 函数中也存在类型推断机制，但需要给定形参的默认值，否则推断不出来。
    return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(8.5)
print(al)

def calc_order_cost(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: float = 0.0) -> float:     # 设置默认值后类型推断机制即可正确推断
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

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 3), ("手机", 4999, 1), coupon = 10, score = 4000, express = 9.9)
print(total)






