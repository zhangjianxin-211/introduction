class Dog:
    def __init__(self, x, y):
        self.color = "yellow"
        self.name = x
        self.age = y


dog1 = Dog("旺财", 5)
dog2 = Dog("来福", 3)

print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)
