class Father:
    def __init__(self):
        self.__name = "父亲"


class Son(Father):
    def show_name(self):
        print(self.__name)


s1 = Son()
s1.show_name()

