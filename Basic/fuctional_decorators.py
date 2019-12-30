"""
Python 理解和学习 参考网址：https://www.cnblogs.com/yuzhanhong/p/9180212.html
"""
import time


def demo_0():
    msg = '原始的装饰器'
    print('====%s=====' % msg)

    def deco(fuc):
        def wrapper():
            start_time = time.time()
            fuc()
            end_time = time.time()
            execution_time = (end_time - start_time)*1000
            print("time is %d ms" % execution_time )
        return wrapper

    @deco
    def f():
        print("hello")
        time.sleep(1)
        print("world")

    f()


def demo_1():
    msg = '带固定参数的装饰器'
    print('====%s=====' % msg)

    def deco(f):
        def wrapper(a, b):
            start_time = time.time()
            f(a, b)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print("time is %d ms" % execution_time)

        return wrapper

    @deco
    def f(a, b):
        print("be on")
        time.sleep(1)
        print("result is %d" % (a + b))

    f(2, 3)


def demo_2():
    msg = '带不固定参数的装饰器'
    print('====%s=====' % msg)

    def deco(fun):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            fun(*args, **kwargs)
            end_time = time.time()
            execution_time_ = (end_time - start_time) * 1000
            print("time is %d ms" % execution_time_)

        return wrapper

    @deco
    def f(a, b):
        print("be on")
        time.sleep(1)
        print("result is %d" % (a + b))

    @deco
    def f1(a, b, c):
        print("be on")
        time.sleep(1)
        print("result is %d" % (a + b + c))

    f(2, 3)
    f1(2, 3, 4)


def demo_3():
    msg = '使用带多个装饰器'
    print('====%s=====' % msg)

    def deco01(f):
        def wrapper(*args, **kwargs):
            print("this is deco01")
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print("time is %d ms" % execution_time)
            print("deco01 end here")

        return wrapper

    def deco02(f):
        def wrapper(*args, **kwargs):
            print("this is deco02")
            f(*args, **kwargs)

            print("deco02 end here")

        return wrapper

    @deco01
    @deco02
    def f(a, b):
        print("be on")
        time.sleep(1)
        print("result is %d" % (a + b))

    f(2, 3)


def demo_4():
    msg = '类装饰器'
    print('====%s=====' % msg)

    class decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('before............')
            res = self.func(*args, **kwargs)
            print('after............')
            return res

    @decorator
    def run():
        print('run............')

    run()


demo_0()
demo_1()
demo_2()
demo_3()
demo_4()