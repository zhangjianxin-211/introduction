def makeBold(func):
    """对被装饰的函数的返回值 加粗"""
    def inner():
        return "<b>" + func() + "</b>"
    return inner

def makeItalic(func):
    """对被装饰的函数的返回值 倾斜"""
    def inner():
        return "<i>" + func() + "</i>"
    return inner


# 装饰过程  就近装饰      装饰过程: hello =makeBold(makeItalic(hello))
@makeBold
@makeItalic
def hello():
    return "hello python!!!"

print(hello())