# 函数的定义<不执行代码>
def func():
    print('in func')


# 函数的调用 执行函数代码
# 函数名：一个指向了函数代码空间的应用
f = func
print(id(f), id(func))
f()
