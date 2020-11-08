# 私有：只能被当前类所使用，外界是不能查看和修改的


class Dog:
    def __init__(self):
        # 私有属性
        self.__name = "旺财"

    # 私有方法
    def __eat(self):
        print("狗在吃东西")


dog1 = Dog()
dog1.__name = "来福"
print(dog1.__name)
dog1.__eat()
