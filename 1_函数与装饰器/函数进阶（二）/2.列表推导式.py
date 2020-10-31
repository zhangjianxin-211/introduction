# 列表推导式：快速帮我们创建有规律的列表

# list1 = []
#
# for i in range(1, 101):
#     list1.append(i)

# list1 = [计算公式(每次循环过后的代码，都会在这里追加) for i in range(1, 101)]
# list1 = [i for i in range(1, 101)]

# list1 = [i for i in range(1, 101) if i % 2 == 0]

# list1 = [i for i in range(5) for j in range(5)]

list1 = ["666" for i in range(10)]

# print(list1)

a = [x for x in range(1,101)]
b = [a[x:x+3] for x in range(0, len(a), 3)]

# 0-100   0,3,6,9

# a[9:12]
# b = [[1,2,3], [4,5,6], [7,8,9]]
print(b)
