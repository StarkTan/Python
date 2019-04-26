"""
使用 getattr，hasattr，setattr，delattr 测试python 的反射功能
"""

#定义一个类
class User(object):

    def __init__(self):
        self.name = 'users'

    def method(self, arg1=0, *args):
        print(arg1)
        print(args)
        return


# 实例化
user = eval('User()')
print(type(user))
# 正常使用
print(user.name)
user.method()

# 使用hasattr 确认属性
print('=====hasattr======')
print(hasattr(user, 'name'))
print(hasattr(user, 'method'))
print(hasattr(user, 'method1'))
# 使用getattr
print('=====getattr======')
print(getattr(user, 'name'))
print(getattr(user, 'method'))
print(getattr(user, 'method2', 'not found'))
# 执行
method = getattr(user, 'method')
method(1, 2, 3, [4, '5'])
# 使用 setattr 设置属性
print('=====setattr======')
setattr(user, 'name', 'new user')
print(getattr(user, 'name'))
setattr(user, 'age', 26)
print(getattr(user, 'age'))
setattr(user, 'method2', lambda x, y: x+y)
print(getattr(user, 'method2')(1, 2))

# 使用 delattr 刪除属性
print('===== delattr ======')
delattr(user,'name')
"""
原始函数无法被删除
"""
try:
    delattr(user,'method')
except:
    print('cannot del')
delattr(user,'method2')
print(hasattr(user, 'name'))
print(hasattr(user, 'method'))
print(hasattr(user, 'method2'))

method = getattr(user, 'method')
method(1, 2, 3, [4, '5'])
