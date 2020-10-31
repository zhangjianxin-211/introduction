# 引用：内存地址
# 变量的赋值，不是把值传给变量；实际上是把内存地址的东西传给了变量
# a = 10
# list1 = [1,2,3,4]
# print(id(list1))


# 当它们地址是一样，对于其中一个增删改，那么另外一个，也会跟着变化
# list1 = [1, 2, 3]
# list2 = list1
#
# list2.append(4)
#
# print("我是list2：", list2)
# print("我是list1：", list1)

# dict1 = {"name":"zs"}
# dict2 = dict1
#
# dict2["age"] = 18
#
# print(dict1)
# print(dict2)

# a = "haha"
# b = a
# b = b + "hehe"
#
# print(a)
# print(b)

# a = 10
# b = a
# b = b + 10
# print(a)
# print(b)


# 英文字母跟数字，默认的地址是一样的
# 为什么数字跟英文字母会一样的呢？它们有缓存
str1 = "haha"
str2 = "haha"

print(id(str1))
print(id(str2))

num1 = 10
num2 = 10

print(id(num1))
print(id(num2))
