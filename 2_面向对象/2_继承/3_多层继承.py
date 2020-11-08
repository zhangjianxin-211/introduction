class GrandFather:
    def eat(self):
        print("吃东西")


class Father(GrandFather):
    pass


class Son(Father):
    pass


son1 = Son()
son1.eat()
