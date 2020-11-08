class A:
    def __init__(self):
        self.name = 'A'

    def eat(self):
        print("吃东西")


class B:
    def __init__(self):
        self.name = 'B'

    def drink(self):
        print("喝饮料")


class C(A, B):
    pass


c1 = C()
c1.eat()
c1.drink()
print(c1.name)