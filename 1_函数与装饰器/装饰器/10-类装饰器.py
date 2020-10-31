# 用类实现装饰器的功能


class MyClass(object):
    def __init__(self, func):
        """类似于闭包中外部函数  接收参数"""
        self.func = func

    def __call__(self, *args, **kwargs):
        """类似于闭包中内部函数  执行扩展功能原有功能"""
        # 执行扩展的新功能
        print("正在进行安全检查")
        # 执行原函数功能
        ret = self.func(*args, **kwargs)
        return ret


@MyClass
def f1():
    print("in f1")


# f1 = MyClass(f1)   实例对象 = 类()
# callable可调用 对象()  # 对象() === 对象.__call__()
# 可调用 对象:  函数名/类名/方法名/匿名函数对象/实现了 __call__方法的实例对象

f1()
