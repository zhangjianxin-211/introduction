class Cat:
    def __init__(self):
        self.types = '猫'


class Dog:
    def __init__(self, x):
        self.name = x

    def __del__(self):
        """
        del 方法：当前对象被删除前一刻，会自动触发
        等用于临终遗言
        """
        print(f"{self.name}对象被删除了")


while True:
    dog1 = Dog('旺财')
    dog2 = Dog('来福')