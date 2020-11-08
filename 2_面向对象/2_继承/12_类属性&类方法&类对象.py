# 类属性、类方法、类对象：只会触发一次
# 什么时候用这些类的东西？如果所有的对象，他们有某个属性，全部都是一样的话，并且不改的情况下


class Dog:
    # 类属性
    type = "狗"

    def __init__(self):
        self.types = "狗"

    def show_types(self):
        print(f"类型是：{self.types}")

    @classmethod  # 类方法：装饰器
    def show_type(cls):
        """类方法用的是cls参数"""
        print(f"类型是：{cls.type}")


dog1 = Dog()  # 类对象
dog1.show_type()


dog1 = Dog()
dog1.show_types()

dog2 = Dog()
dog2.show_types()

dog3 = Dog()
dog3.show_types()

