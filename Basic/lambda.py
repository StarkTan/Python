"""
Lambda 函数
"""
# lambda 函数 指将一个方法实例化，然后进行调用
add = lambda x, y: x + y


# 回调函数
def add_use(x, y, fun):
    return fun(x, y)


print(add_use(1, 2, add))

lists = [1, -3, 2, -5, -4, 7, 8, 4, 3]

sorted_list = sorted(lists, key=lambda x: abs(x))
print(sorted_list)
