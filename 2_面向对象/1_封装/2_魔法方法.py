

class Dog():
    """
    定义属性，需要一个魔法方法：init
    前后俩个下划线：叫做魔法方法。不需要调用，会自动在特定的场景调用
    init会在，创建对象时，自动调用
    init的魔法方法，主要用于定义属性。也叫初始化方法
    """
    def __init__(self):
        """
        定义属性
        self：当前对象
        """
        self.color = "yellow"
        self.types = "狗"
        self.name = "旺财"

    # @staticmethod
    def eat(self):
        print("狗在吃东西")


dog1 = Dog()
print(dog1.name)

dog2 = Dog()
dog2.name = "来福"
print(dog2.name)
dog1.eat()


