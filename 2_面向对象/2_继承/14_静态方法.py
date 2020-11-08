# 静态方法：当你方法中用不上self参数，建议你把他变成静态，从而优化程序


class Dog(object):
    def __init__(self):
        self.name = "旺财"

    @staticmethod
    def eat():
        print("吃东西")


dog1 = Dog()
dog1.eat()

