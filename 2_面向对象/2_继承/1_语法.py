# 继承的作用：把别人跟我差不多的代码，继承过来使用，从而减少代码量


class Dog:
    def __init__(self):
        self.name = "旺财"

    def eat(self):
        print("吃东西")

    def drink(self):
        print("喝东西")


class Cat(Dog):
    pass


dog1 = Dog()
dog1.eat()

cat1 = Cat()
cat1.eat()
cat1.drink()
print(cat1.name)