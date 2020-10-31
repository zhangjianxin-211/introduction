# def fun1(a, b):
#     return a + b
#
#
# result = fun1(10, 20)
# print(result)

# fun1 = lambda 形参1, 形参2: 函数的返回值或者你要执行的代码
fun1 = lambda a, b: a + b

result = fun1(10, 20)
print(result)

"""匿名函数小应用"""
# def fun1(p1):
#     # 如果用户传的是函数名，那么这里就要加小括号
#     result = p1()
#     print(result)
#
#
# def fun2():
#     return 10
#
#
# # 需求：把fun2的返回值，传给fun1作为参数
# # 传的是函数名，得到的是地址
# fun1(fun2)


# def jia(a, b):
#     num1 = a
#     num2 = b
#     result = num1 + num2
#     return result
#
#
# def jian(a, b):
#     num1 = a
#     num2 = b
#     result = num1 - num2
#     return result
#
#
# result1 = jia(10, 20)
# print(result1)
#
# result2 = jian(20, 10)
# print(result2)


# def jia(a, b):
#     return a + b
#
#
# def jian(a, b):
#     return a - b
#
#
# def operation(a, b):
#     result = jia(a, b)
#     print(result)
#
#
# def operation1(a, b):
#     result = jian(a, b)
#     print(result)
#
#
# operation(10, 20)
# operation1(10, 20)


# def jia(a, b):
#     return a + b
#
#
# def jian(a, b):
#     return a - b
#
#
# def operation(func):
#     result = func
#     print(result)
#
#
# operation(jia(10, 20))
# operation(jian(20, 10))


def operation(func):
    result = func(10, 20)
    print(result)


operation(lambda a, b: a + b)
operation(lambda a, b: a - b)
operation(lambda a, b: a * b)

