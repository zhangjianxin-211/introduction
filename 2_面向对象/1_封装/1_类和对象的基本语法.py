class Dog:  # 定义类
    def eat(self, p1):  # 定义方法
        print(f'{p1}在吃东西')


dog1 = Dog()  # 创建对象，
dog1.name = "旺财"  # 设置属性   对象.属性名 = 值
dog1.eat(dog1.name)  # 调用方法。 对象.方法名()
# print(dog1.name)

dog2 = Dog()
dog2.name = "来福"
dog2.eat(dog2.name)
# print(dog2.name)

