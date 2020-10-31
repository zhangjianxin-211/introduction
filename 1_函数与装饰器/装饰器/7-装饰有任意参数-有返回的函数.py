import time

def gettime(f):
    def inner(*args, **kwargs):
        """*args接收所有的位置参数 (1,) **kwargs接收所有的关键字参数{"n2":22}"""
        begin = time.time()
        # 暂存 原函数的返回值 在最后位置返回即可
        ret = f(*args, **kwargs)  # 拆包 f(1,n2=22)
        end = time.time()
        print("花费了%f 秒" % (end-begin))
        return ret
    return inner

@gettime
def f1(number1):
    time.sleep(2.3)
    print("in f1")
    return 1001
# f1 = gettime(f1)

@gettime
def f2(n1,n2):
    for i in range(3):
        time.sleep(1)
        print("in f2")
# f2=gettime(f2)

print(f1(1))
f2(1, n2=22)