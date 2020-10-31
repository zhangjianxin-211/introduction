def some(name):
    """外层函数接收数据"""
    def say(data):
        """内层函数可以使用外层函数接收到的数据"""
        print("%s 说话 %s" % (name, data))

    return say


tom = some("Tom")
tom("jerry 你在哪儿")
tom("晚上撸个串")

summy = some("summy")
summy("jerry 你在哪儿")
