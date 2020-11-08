class Dog:
    def __init__(self):
        self.name = "zs"  # 实例化属性  （普通属性）
        self.__age = 18  # 私有化属性

    def eat(self):  # 实例化方法（普通方法）
        pass

    def __drink(self):  # 私有化方法
        print("喝饮料")


dog1 = Dog()  # 实例化对象
