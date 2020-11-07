# class SweetPotato:
# 属性：状态、总时间
# 方法：烧烤、判断时间
# 输出：状态和总时间


class SweetPotato:
    def __init__(self):
        self.state = "生的"
        self.time = 0

    def cook(self, cook_time):
        self.time += cook_time

        if 0 <= self.time < 3:
            self.state = '生的'
        elif 3 <= self.time < 6:
            self.state = '半生不熟'
        elif 6 <= self.time < 8:
            self.state = '熟了'
        else:
            self.state = '糊了'

    def __str__(self):
        return f"当前地瓜的状态:{self.state};烧烤的总时间:{self.time}分钟"


spud = SweetPotato()
spud.cook(1)
spud.cook(3)
spud.cook(3)
print(spud)
