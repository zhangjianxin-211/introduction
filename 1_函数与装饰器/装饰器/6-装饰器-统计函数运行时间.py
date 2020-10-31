import time


def gettime(f):
    def inner():
        begin = time.time()
        f()
        end = time.time()
        print("花费了%f 秒" % (end-begin))

    return inner


@gettime
def f1():
    time.sleep(2.3)
    print("in f1")


@gettime
def f2():
    for i in range(3):
        time.sleep(1)
        print("in f2")


f1()
f2()