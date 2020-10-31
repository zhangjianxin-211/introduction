def func(number1):
    print("in func")

    def func_in(number2):
        print("in func_in %d" % (number1 + number2))
    return func_in


"""
闭包语法特点：
1、嵌套定义
2、外层函数返回内层函数的应用
3、内层函数可以使用外层函数提供的变量  自由变量  环境变量  继承
"""
# f = func_in
f = func(99)
f(1)
