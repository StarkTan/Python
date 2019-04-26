"""
学习 Python 的闭包

字面意思：闭包是由函数及其相关的引用环境组合而成的实体
我的理解：把函数理解成一个对象实例，这个实例持有自己的变量属性，

"""


def out_func(n):
    """
    example
    """
    count = n

    def inner_func():
        #不能修改外部变量 可以用容器代替

        return count + 1

    return inner_func


my_func = out_func(10)
print(my_func())
