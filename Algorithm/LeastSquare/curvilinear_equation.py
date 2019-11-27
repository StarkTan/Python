"""
使用最小二分法找出最佳曲线方程参数
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

Xi = np.array([1, 2, 3, 4, 5, 6])
Yi = np.array([9.1, 18.3, 32, 47, 69.5, 94.8])


def func(p, x):
    a, b, c = p
    return a*x*x+b*x+c


def error(p, x, y):
    return func(p, x)-y


p0 = np.array([10, 10, 10])
Para = leastsq(error, p0, args=(Xi, Yi))
a, b, c=Para[0]
print("a=", a, "b=", b, "c=", c)
print("cost："+str(Para[1]))
print("求解的拟合直线为:")
print("y="+str(round(a, 2))+"x*x+"+str(round(b, 2))+"x+"+str(c))

plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color="green", label="Data Point", linewidth=2)

x = np.linspace(0, 12, 100)
y = a*x*x+b*x+c
plt.plot(x, y, color="red", label="Best Line",linewidth=2)
plt.legend()  # 绘制图例
plt.show()
