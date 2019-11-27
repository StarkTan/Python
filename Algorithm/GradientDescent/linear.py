"""
使用梯度下降法拟合直线
"""

import numpy as np
import matplotlib.pyplot as plt

# 创建数据集
m = 20  # 数据集大小
X0 = np.ones((m, 1))
X1 = np.arange(1, m+1).reshape(m, 1)
X = np.hstack((X0, X1))  # 创建 x 轴数据，并进行向量数据填充 ax + b

y = np.array([
    3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
    11, 13, 13, 16, 17, 18, 17, 19, 21
]).reshape(m, 1)  # 创建 y 轴数据

# 展示点集数据
plt.figure(figsize=(8, 6))  # 指定图像比例： 8：6
plt.scatter(X1.reshape(1,-1), y.reshape(1, -1), color="green", label="Data Point", linewidth=2)
plt.show()

# 设置学习率/步长
alpha = 0.01


# 定义代价函数
def error_function(theta, X, y):
    diff = np.dot(X, theta) - y  # 获取所有的差值向量
    return (1./2*m) * np.dot(np.transpose(diff), diff)  # 计算当前点的所有的差值


# 代价函数的梯度(获取当前测试值的梯度值)
def gradient_function(theta, X, y):
    diff = np.dot(X, theta) - y
    return (1./m) * np.dot(np.transpose(X), diff)  # 获取当前的a，b的梯度值


# 梯度下降迭代算法
def gradient_descent(X, y, alpha):
    theta = np.array([1, 1]).reshape(2, 1)  # 设置初始的代价函数
    gradient = gradient_function(theta, X, y)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, y)
    return theta


optimal = gradient_descent(X, y, alpha)
print('optimal:', optimal)
print('error function:', error_function(optimal, X, y)[0, 0])

# 画拟合直线
plt.figure(figsize=(8, 6))  # 指定图像比例： 8：6
plt.scatter(X1.reshape(1,-1), y.reshape(1, -1), color="green", label="Data Point", linewidth=2)
x = np.linspace(0, 20, 100)  # 在0-20直接画100个连续点
y = optimal[1][0]*x + optimal[0][0] # 函数式
plt.plot(x, y, color="red", label="Best Line",linewidth=2)
plt.legend(loc='lower right')  # 绘制图例
plt.show()