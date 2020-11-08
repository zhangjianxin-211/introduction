class Dog:
    def __init__(self):
        self.__name = "旺财"

    # 需求：让外面的人修改这个私有属性
    def deal_name(self, x):
        self.__name = x

    def show_name(self):
        # 让外面查看私有的东西
        print(f"他的名字叫：{self.__name}")


dog1 = Dog()
dog1.deal_name("来福")
dog1.show_name()
