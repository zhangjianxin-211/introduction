import time

"""给装饰器传入更多参数目的: 希望装饰器内部代码能够根据参数 实现不一样的逻辑
    但是  装饰器只能接收一个参数
    解决方法: 将装饰器函数放到一个外部函数中 由外部函数接收参数 装饰器可以直接使用
"""
def get_run_time(flag):
    def gettime(f):
        def inner(*args, **kwargs):
            """*args接收所有的位置参数 (1,) **kwargs接收所有的关键字参数{"n2":22}"""
            begin = time.time()
            # 暂存 原函数的返回值 在最后位置返回即可
            ret = f(*args, **kwargs)  # 拆包 f(1,n2=22)
            end = time.time()
            if flag == 0:
                print("花费了%d 秒" % int(end - begin))
            else:
                print("花费了%f 秒" % (end-begin))
            return ret
        return inner
    return gettime


@get_run_time(1)
def f1(number1):
    time.sleep(2.3)
    print("in f1")
    return 1001

# 1 执行 get_time = get_run_time(1)   2 @gettime 开始对下面函数进行装饰
# 一步理解  f1 = get_run_time(1)(f1)


print(f1(1))