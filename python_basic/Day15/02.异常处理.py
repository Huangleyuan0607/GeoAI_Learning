# 异常处理
# try:
#     print("==============================")
#     # print(my_name)
#     # print(1 / 0)
#     # print("ABC"[10])
#     print("ABC".Hello)
#     print("==============================")
# except NameError as e:   # 捕获的是NameError类型的异常，其他类型的异常(如：ZeroDivisionError)捕获不了
#     print("名字不存在，请检查变量或函数名字，异常信息：", e)
# except ZeroDivisionError as z:   # 捕获的是NameError类型的异常，其他类型的异常(如：ZeroDivisionError)捕获不了
#     print("0不能做被除数，异常信息：", z)
# except IndexError as i:
#     print("索引错误，异常信息：", i)
# except Exception as e:      # 捕获所有异常，也可以直接写成：except :，但最好还是具体到异常类型
#     print("程序运行出错了，请联系管理员，错误信息:", e)
# finally:    # 无论程序是否正常运行，finally代码块中的代码都会运行
#     print("资源释放~")


# 异常传递
def fun1():
    print("fun1... running ...")
    fun2()

def fun2():
    print("fun2... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了，请联系管理员，错误信息：", e)

