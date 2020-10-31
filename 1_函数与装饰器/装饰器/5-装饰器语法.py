# 装饰器基于 闭包实现<装饰器函数> 类实现<类装饰>
# 为什么需要装饰器？在不修改代码情况对函数的功能进行扩展
# def login():
#     """业务逻辑"""
#     print("正在检查")
#     print("正在登录")


def check(f):
    """参数就是需要加功能的函数引用"""

    def inner():
        print("正在做安全检查")
        f()

    return inner


@check
def login():
    """业务逻辑"""
    print("正在登录")


# 灵魂代码
# login = check(login)

login()
