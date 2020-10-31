# 返回值作用：1.告诉给调用者一个结果；2.会终止后面的程序继续运行(跳出函数)
def fun1():
    num1 = 10
    num2 = 20

    return num1 + num2
    print("return后面同等缩进的代码不会被执行，")


# 函数出现None的原因，代表没有返回值
# 有返回值的函数，得到的是一个结果；
# 没有返回值的函数，得到的是一个功能；


fun1()  # 只有返回值，没有输出需要一个变量来接收，在打印去查看结果
num = fun1()
print(num)


def fun2():
    """一个return可以返回多个数据的，得到的是元组"""

    return 10, 20, 30


num = fun2()
print(num)


def fun3():
    """在分支语句中可以多次使用return"""
    num3 = 5
    if num3 == 5:
        return 5
    elif num3 == 10:
        return 10


num = fun3()
print(num)


def fun1():
    num1 = 10
    num2 = 20
    print("1")
    print("2")
    return num1 + num2


num = fun1()
print(num)
