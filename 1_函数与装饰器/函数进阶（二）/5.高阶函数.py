# map函数：把列表中，每一个数据，单独拿出来运算

# list1 = [1, 2, 3]
# list2 = []
#
# for i in list1:
#     list2.append(i + 1)
#
# print(list2)


# list1 = [1, 2, 3]
#
#
# def fun1(x):
#     # x：每一个数据
#     return x * 2
#
#
# # map(函数名, 列表)
# result = map(fun1, list1)
#
# print(list(result))


# names = ["james", "rose", "jack", "tony"]
#
#
# def fun1(x):
#     return x[0].upper() + x[1:]
#
#
# result = map(fun1, names)
# print(list(result))


# import functools
# # reduce函数：把列表中所有数据，组合起来进行运算，最终得出一个结果
# list1 = [1, 2, 3, 4]
#
#
# def fun1(x1, x2):
#     return x1 + x2
#
#
# result = functools.reduce(fun1, list1)
# print(result)


# filter函数：做过滤的作用
# list1 = [i for i in range(100)]
#
#
# def fun1(x):
#     return x % 2 == 0
#
#
# result = filter(fun1, list1)
# print(list(result))


names = ["James", "tony", "Rose", "jack"]


def fun1(x):
    return x[0].isupper()


result = filter(fun1, names)
print(list(result))


# 小总结：map和filter最后需要转换类型，不然默认得到的是地址
