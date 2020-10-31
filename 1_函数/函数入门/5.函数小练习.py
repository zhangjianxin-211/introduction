# 写一个函数打印一条横线
def line():
    print("-" * 50)


# 打印自定义行数的横线
def lines(par):
    for i in range(par):
        # 函数的嵌套
        line()


lines(2)
lines(3)


# 写一个函数求三个数的和
def sum(p1, p2, p3):
    return p1 + p2 + p3


sum(10, 5, 5)


# 写一个函数求三个数的平均值
def avg(p1, p2, p3):
    num = sum(p1, p2, p3)
    print(num / 3)


avg(10, 20, 30)
