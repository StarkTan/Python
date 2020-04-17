"""
nonlocal 关键字
    用来在函数或其他作用域中使用外层(非全局)变量
    在内部函数修改外部函数的变量时使用
"""

class Test1(object):

    def __init__(self,num):
        self.num = num

    def change(self,num):
        self.num = num

    def __str__(self):
        return str(self.num)


def outer():
    test = Test1(1)

    def inner1():
        test = Test1(2)

    def inner2():
        nonlocal test
        test = Test1(3)

    def inner3():
        test.change(4)

    print(test)
    inner1()
    print(test)
    inner2()
    print(test)
    inner3()
    print(test)

outer()
