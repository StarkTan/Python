import numpy as np
from matplotlib import pylab as plt


def sample():
    x = np.linspace(0, 10, 20)
    y = x * x + 2
    # figure 相当于绘画用的画板，而 axes 则相当于铺在画板上的画布。我们将图像绘制在画布上，于是就有了 plot，set_xlabel 等操作。
    fig, axes = plt.subplots(figsize=(16, 9), dpi=50)  # 通过 figsize 调节尺寸, dpi 调节显示精度
    axes.plot(x, y, 'r')
    plt.show()
    # 绘制子图
    # fig, axes = plt.subplots(nrows=1, ncols=2)  # 子图为 1 行，2 列
    # for ax in axes:
    #     ax.plot(x, y, 'r')
    # plt.show()


def simple_1():
    x = np.linspace(0, 10, 20)

    fig, axes = plt.subplots()

    axes.set_xlabel('x label')
    axes.set_ylabel('y label')
    axes.set_title('title')

    axes.plot(x, x ** 2)
    axes.plot(x, x ** 3)
    # loc 参数标记图例位置，1，2，3，4 依次代表：右上角、左上角、左下角，右下角；0 代表自适应
    axes.legend(["y = x**2", "y = x**3"], loc=2)

    plt.show()


def simple_2():
    x = np.linspace(0, 10, 20)
    fig, ax = plt.subplots(figsize=(12, 6))
    # 线宽
    ax.plot(x, x + 1, color="blue", linewidth=0.25)
    ax.plot(x, x + 2, color="blue", linewidth=0.50)
    ax.plot(x, x + 3, color="blue", linewidth=1.00)
    ax.plot(x, x + 4, color="blue", linewidth=2.00)

    # 虚线类型
    ax.plot(x, x + 5, color="red", lw=2, linestyle='-')
    ax.plot(x, x + 6, color="red", lw=2, ls='-.')
    ax.plot(x, x + 7, color="red", lw=2, ls=':')

    # 虚线交错宽度
    line, = ax.plot(x, x + 8, color="black", lw=1.50)
    line.set_dashes([5, 10, 15, 10])

    # 符号
    ax.plot(x, x + 9, color="green", lw=2, ls='--', marker='+')
    ax.plot(x, x + 10, color="green", lw=2, ls='--', marker='o')
    ax.plot(x, x + 11, color="green", lw=2, ls='--', marker='s')
    ax.plot(x, x + 12, color="green", lw=2, ls='--', marker='1')

    # 符号大小和颜色
    ax.plot(x, x + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
    ax.plot(x, x + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)
    ax.plot(x, x + 15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
    ax.plot(x, x + 16, color="purple", lw=1, ls='-', marker='s', markersize=8, markerfacecolor="yellow",
            markeredgewidth=2, markeredgecolor="blue")
    plt.show()


def simple_3():
    x = np.linspace(0, 10, 20)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].plot(x, x ** 2, x, x ** 3, lw=2)
    # 显示网格
    axes[0].grid(True)
    axes[1].plot(x, x ** 2, x, x ** 3)
    # 设置坐标轴范围
    axes[1].set_ylim([0, 60])
    axes[1].set_xlim([2, 5])

    plt.show()


def simple_4():
    # 绘制散点图、梯步图、条形图、面积图
    x = np.linspace(0, 10, 20)
    n = np.array([0, 1, 2, 3, 4, 5])

    fig, axes = plt.subplots(1, 4, figsize=(16, 5))

    axes[0].scatter(x, x + 0.25 * np.random.randn(len(x)))  # scatter散点图
    axes[0].set_title("scatter")

    axes[1].step(n, n ** 2, lw=2)  # 梯步图
    axes[1].set_title("step")

    axes[2].bar(n, n ** 2, align="center", width=0.5, alpha=1)  # 柱状图 alpha 透明度
    axes[2].set_title("bar")

    axes[3].fill_between(x, x ** 2, x ** 3, color="green", alpha=0.5)  # 面积图
    axes[3].set_title("fill_between")

    plt.show()


def simple_5():
    n = np.random.randn(100000)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(n)  # 默认分布直方图
    axes[0].set_title("Default histogram")
    axes[0].set_xlim((min(n), max(n)))

    axes[1].hist(n, cumulative=True, bins=50)  # cumulative=True 累计直方图
    axes[1].set_title("Cumulative detailed histogram")
    axes[1].set_xlim((min(n), max(n)))

    plt.show()


def simple_6():
    alpha = 0.7
    phi_ext = 2 * np.pi * 0.5

    def flux_qubit_potential(phi_m, phi_p):
        return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p)

    phi_m = np.linspace(0, 2 * np.pi, 100)
    phi_p = np.linspace(0, 2 * np.pi, 100)
    X, Y = np.meshgrid(phi_p, phi_m)
    Z = flux_qubit_potential(X, Y).T

    fig, ax = plt.subplots()

    ax.contour(Z, cmap=plt.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])

    plt.show()


# sample()
# simple_1()
# simple_2()
# simple_3()
# simple_4()
# simple_5()
simple_6()
