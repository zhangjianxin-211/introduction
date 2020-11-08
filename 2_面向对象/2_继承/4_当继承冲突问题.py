# 每一个类都会继承一个object类，这是我们不知道
# object：基类


class Dog(object):
    def __init__(self):
        self.types = "狗"
        self.color = "大黄色"

    @staticmethod
    def eat():
        print("狗在吃东西")

    @staticmethod
    def drink():
        print("喝饮料")


class Cat(Dog):
    def __init__(self):
        super().__init__()
        self.types = "猫"

    def eat(self):
        print("猫吃东西")


cat1 = Cat()
cat1.eat()
cat1.drink()
print(cat1.types)
print(cat1.color)