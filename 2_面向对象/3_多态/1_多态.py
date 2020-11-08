# 其他语言是不能既调用父类，又调用子类的。其他语言想要实现多态需要写一段代码


"""多态：即可调用父类，又可调用子类"""


class Father:
    def eat(self):
        print('我会吃饭')


class Son(Father):
    def drink(self):
        print('我会喝水')


class Person:
    def show_eat(self):
        s1 = Son()
        s1.eat()
        s1.drink()


p1 = Person()
p1.show_eat()


