def func(number1):
    print("in func")
    data = []

    def func_in(number2):
        nonlocal number1
        data.append("xx")
        # 可变类型 就不用生明；不可变类型 需要 nonlocal
        # 生明 number1 是一个自由变量<外部函数提供给内部函数使用> 不能和全局变量混淆
        number1 += 1
        print("in func_in %d" % (number1 + number2))
    return func_in


f = func(99)
f(1)
