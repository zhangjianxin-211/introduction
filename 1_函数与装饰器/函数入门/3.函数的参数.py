# 作用：可以让函数，更加的灵活，不再是一成不变
# 注意：！！！！！形参不要当作变量使用！！！！！！


def fun1(p1, p2):  # 形参：未知数
    num1 = p1
    num2 = p2
    print(num1 * num2)


fun1(10, 20)  # 实参：会把真正的数据传到函数的形参中去
fun1(20, 50)


def fun2(list1):
    for i in list1:
        print(i)
        # print(type(i))
        # print(type(list1))


fun2(['a', 'b', 'c'])
fun2([1, 2, 3])
