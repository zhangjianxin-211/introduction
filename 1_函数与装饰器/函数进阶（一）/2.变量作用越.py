# 变量作用域：变量的使用范围
# 局部变量：在函数内部定义的变量。只能在当前函数内使用
# 全局变量：在函数外部定义的变量。所有人都能使用的
# 全局覆盖全局。局部覆盖局部

num = 5


def fun1():
    # 局部变量   函数优先使用局部变量
    # 局部变量提升为全局变量
    # global num
    num = 10
    print(num)


def fun2():
    print(num)


fun1()
fun2()


for i in range(3):
    num = 10


print(num)

