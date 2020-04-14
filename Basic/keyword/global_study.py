"""
global 关键字
    如果python函数内想要改变函数外的变量则需要先使用global进行定义
    python 函数内可以直接调用函数外对象的函数
"""



class Test(object):
    xxx = 123

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def print(self):
        print(self.num)


num = 1
cla = Test(1111)


def change():

    global num, cla
    num = 3
    cla = Test(2222)


class Test2(object):

    def change(self):
        global num, cla
        num = 99
        cla = Test(3333)


def use():
    print(num.bit_length())
    cla.print()


use()
change()
print(num, cla)
Test2().change()
print(num, cla)
use()