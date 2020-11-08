class Dog:
    name = "张三"

    # def __init__(self):
    #     self.name = "李四"

    def show_name(self):
        print(self.name)

    # @classmethod
    # def show_name(cls):
    #     print(cls.name)


dog1 = Dog()
# print(dog1.name)
dog1.show_name()
