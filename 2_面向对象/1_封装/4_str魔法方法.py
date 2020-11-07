class Cat:
    def __str__(self):
        """str方法：打印或者调用对象时 就会触发"""
        return "猫在吃鱼"


cat1 = Cat()
print(cat1)