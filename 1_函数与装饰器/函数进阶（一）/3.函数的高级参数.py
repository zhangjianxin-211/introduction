# 缺省参数，也叫默认参数：给参数一个默认值，从而传少一个参数


# def fun1(p1, p2=18):
#     name = p1
#     age = p2
#
#     print(f"名字是：{name}，年龄是：{age}")
#
#
# fun1("张三")
# fun1("李四")
# fun1("王五")
# fun1("赵六")
# fun1("田七", 19)
# fun1("王八", 17)


# 关键字参数：根据形参的名字进行传递，不需要考虑顺序问题
# def fun1(p1, p2, p3):
#     print(f"p1:{p1}")
#     print(f"p2:{p2}")
#     print(f"p3:{p3}")
#
#
# fun1(p1="哈哈", p3="嘻嘻", p2="呵呵")
#
# print("哈哈", end="@@@")


# 不定长参数：任意接收多个参数
# def fun1(*args):
#     # 默认得到的是元组
#     result = 0
#     for i in args:
#         result += i
#
#     print(result)
#
#
# fun1(10, 10, 20, 30, 40,1,2,3,4,5,6)
# fun1(10, 10, 20, 30, 40, 50)


# **kwargs：接收孤儿关键字参数
# def fun1(p1, p2, **kwargs):
#     print(f"p1:{p1}")
#     print(f"p2:{p2}")
#     # 默认得到的是字典
#     print(kwargs)
#
#
# fun1(p1=10, p2=20, name=30, age=40)


def fun1(*args, p1, p2=20, **kwargs):
    print(f"p1：{p1}")
    print(f"p2：{p2}")
    print(f"args：{args}")
    print(f"kwargs：{kwargs}")


#
#
fun1(10, 20, 30, 40, 50, p1=10, p2=20, name="haha", age=18)

# def print(*args, sep=' ', end='\n', file=None):
#
# print(end="@@@","哈哈")
