tuple1 = ("刘德华", "黎明")

# print(tuple1[0])
# print(tuple1[1])

# 拆包：把元组分别赋值到对应的变量
# 多个变量，对应多个元组数据，会自动拆包
# a, b = ("刘德华", "黎明")
#
# print(a)
# print(b)


# print("%s%d" % (name, age))

# dict1 = {"name":"zs", "age":18}

# for key,value in dict1.items():


# 需求：交互值
a = 10
b = 20

# c = a
# a = b
# b = c

a, b = b, a

print(a)
print(b)



# 组包：什么情况下，数据会变成元组
# 一个对应多个数据，会自动组成一个元组

# a = 10,20,40
# print(a)

# def fun1():
#     return 10,20,30,40
#
#
# result = fun1()
# print(result)

# def fun1(*args):
#     print(args)
#
#
# fun1(10,20,30,40)

