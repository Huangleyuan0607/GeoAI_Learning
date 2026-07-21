# 导入模块
# 1、导入模块 ---> 调用方式：模块名.功能名 / 别名.功能名
# import random
# import random as rd

# 2、导入模块中的功能 from ... import ... ---> 调用方式：功能名 / 别名
# from random import randint
# from random import randint as rint
from random import *    # 调用random模块中所有功能，调用时直接通过功能名调用


# for i in range(100):
#     print(rd.randint(1, 100),end = " ")

for i in range(100):
    print(randint(1, 100),end = " ")






