def foo():
    print("starting...")
    while True:
        print('circle start')
        res = yield 4
        print("res:", res)
        print('circle end')


g = foo()
# print(g.send(7)) # can't send non-None value to a just-started generator
print(next(g))  # 函数开始运行,进入循环，到res = yield 4 看做return 4，函数阻塞
print("*" * 20)
print(next(g))  # 函数从 res = yield 4 继续开始运行，但语句不会对res进行赋值
print("*" * 20)
print(g.send(7))  # 函数从 res = yield 4 继续开始运行,执行 res = 7,循环到res = yield 4后阻塞


# 当做迭代器使用
def foo(num):
    print("starting...")
    while num < 10:
        num = num + 1
        yield num


for n in foo(0):
    print(n)
