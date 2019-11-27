"""
Matplotlib 3D 使用
    1. 创建3D坐标轴
    2. 绘制散点图
    3. 绘制3d曲线
    4. 绘制3d曲面
    5. 绘制等高线
    6. 随机散点图
    7. 随机散点图
    8. 绘制3D表面图
    9. 空间文字
    10.3D柱状图
"""


# 创建3d坐标轴
def create_axes():
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    ax2 = Axes3D(fig)  # 效果和上一行相同
    # ax = fig.add_subplot(111,projection='3d') # 使用这种方式可以创建多个3d图形
    plt.show()


# 绘制散点图
def points():
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    zd = 13 * np.random.random(100)
    xd = 5 * np.sin(zd)
    yd = 5 * np.cos(zd)
    ax1 = plt.axes(projection='3d')
    ax1.scatter3D(xd, yd, zd, cmap='Blues')
    plt.show()


# 绘制3d曲线
def curvilinear():
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    z = np.linspace(0, 13, 1000)
    x = 5 * np.sin(z)
    y = 5 * np.cos(z)
    ax1 = plt.axes(projection='3d')
    ax1.plot3D(x, y, z, 'gray')
    plt.show()


# 绘制3d曲面
def curved_surface():
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()  # 定义新的三维坐标轴
    ax3 = plt.axes(projection='3d')

    # 定义三维数据
    z = np.linspace(0, 13, 1000)
    x = 5 * np.sin(z)
    y = 5 * np.cos(z)
    xx = np.arange(-10, 10, 100)
    yy = np.arange(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) + np.cos(Y)
    # 作图
    # rstride, cstride 为作图的步长，数值越小图片越清晰，需要的资源越大
    ax3.plot_surface(X, Y, Z, rstride=50, cstride=50, cmap='rainbow')
    # ax3.contour(X,Y,Z, zdim='z',offset=-2,cmap='rainbow')  # 等高线图，要设置offset，为Z的最小值
    plt.show()


# 绘制等高线
def contour():
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    xx = np.arange(-5, 5, 0.1)
    yy = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(xx, yy)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
    # 作图
    ax4 = plt.axes(projection='3d')
    ax4.plot_surface(X, Y, Z, alpha=0.3, cmap='winter')  # 生成表面， alpha 用于控制透明度
    ax4.contour(X, Y, Z, zdir='z', offset=-3, cmap="rainbow")  # 生成z方向投影，投到x-y平面
    ax4.contour(X, Y, Z, zdir='x', offset=-6, cmap="rainbow")  # 生成x方向投影，投到y-z平面
    ax4.contour(X, Y, Z, zdir='y', offset=6, cmap="rainbow")  # 生成y方向投影，投到x-z平面
    # ax4.contourf(X,Y,Z,zdir='y', offset=6,cmap="rainbow")  #生成y方向投影填充，投到x-z平面，contourf()函数
    # 设定显示范围
    ax4.set_xlabel('X')
    ax4.set_xlim(-6, 4)  # 拉开坐标轴范围显示投影
    ax4.set_ylabel('Y')
    ax4.set_ylim(-4, 6)
    ax4.set_zlabel('Z')
    ax4.set_zlim(-3, 3)
    plt.show()


# 随机散点图
def random_point():
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    #定义坐标轴
    fig4 = plt.figure()
    ax4 = plt.axes(projection='3d')
    #生成三维数据
    xx = np.random.random(20)*10-5  #取100个随机数，范围在5~5之间
    yy = np.random.random(20)*10-5
    X, Y = np.meshgrid(xx, yy)
    Z = np.sin(np.sqrt(X**2+Y**2))
    # 作图
    ax4.scatter(X,Y,Z,alpha=0.3,c=np.random.random(400),s=np.random.randint(10,20, size=(20, 40)))    #生成散点.利用c控制颜色序列,s控制大小
    # 设定显示范围
    plt.show()


# 绘制3D表面图
def surface():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='b')
    plt.show()


# 空间文字
def text_3d():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
    xs = (1, 4, 4, 9, 4, 1)
    ys = (2, 5, 8, 10, 1, 2)
    zs = (10, 3, 8, 9, 1, 8)
    for zdir, x, y, z in zip(zdirs, xs, ys, zs):
        label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
        ax.text(x, y, z, label, zdir)
    ax.text(9, 0, 0, "red", color='red')
    ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()


# 3d 柱状图
def bar_3d():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
        xs = np.arange(20)
        ys = np.random.rand(20)
        # You can provide either a single color or an array. To demonstrate this,
        # the first bar of each set will be colored cyan.
        cs = [c] * len(xs)
        cs[0] = 'c'
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# create_axes()
# points()
# curvilinear()
# curved_surface()
# contour()
# random_point()
# surface()
# text_3d()
bar_3d()
