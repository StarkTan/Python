import numpy as np


def example():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))
    b = np.array([6, 7, 8])
    print(b)
    print(type(b))


def array_creation():
    b = np.array([1.2, 3.5, 5.1])
    print(b.dtype)
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b)
    c = np.array([[1, 2], [3, 4]], dtype=complex)
    print(c)
    print(np.zeros((3, 4)))
    print(np.ones((2, 3, 4), dtype=np.int16))
    print(np.empty((2, 3)))
    print(np.arange(10, 30, 5))
    print(np.arange(0, 2, 0.3))
    print(np.linspace(0, 2, 9))
    x = np.linspace(0, 2 * np.pi, 100)
    f = np.sin(x)
    print(x)
    print(f)


def print_array():
    print(np.arange(6))
    print(np.arange(12).reshape(4, 3))
    print(np.arange(24).reshape(2, 3, 4))
    print(np.arange(10000))
    np.set_printoptions(threshold=1000)  # 配置展示数量 实际数据数量大于配置 数据就会被折叠
    print(np.arange(10000).reshape(100, 100))


def basic_opration():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    print(a)
    print(b)
    print(a - b)
    print(b ** 2)
    print(10 * np.sin(a))
    print(a < 35)
    A = np.array([[1, 1],
                  [0, 1]])
    B = np.array([[2, 0],
                  [3, 4]])
    print(A * B)  # 元素乘法
    print(A @ B)  # 向量乘法
    print(A.dot(B))  # 向量乘法2
    a = np.ones((2, 3), dtype=int)
    b = np.random.random((2, 3))
    a *= 3
    print(a)
    b += a
    print(b)
    # a += b  b 不能从 float64 转化成 int
    a = np.random.random((2, 3))
    print(a)
    print(a.sum())
    print(a.min())
    print(a.max())

    b = np.arange(12).reshape(3, 4)
    print(b)
    print(b.sum(axis=0))
    print(b.min(axis=1))
    print(b.cumsum(axis=1))  # 当前列之前的和加到当前列上


def universal_function():
    B = np.arange(3)
    print(B)
    print(np.exp(B))
    print(np.sqrt(B))
    C = np.array([2., -1., 4.])
    print(np.add(B, C))


def index_slice_iterate():
    a = np.arange(10) ** 3
    print(a)
    print(a[2])
    print(a[2:5])
    a[:6:2] = -1000
    print(a)
    print(a[::-1])
    for i in a:
        print(i ** (1 / 3.))

    def f(x, y):
        return 10 * x + y

    b = np.fromfunction(f, (5, 4), dtype=int)
    print(b)
    print(b[2, 3])
    print(b[0:5, 1])
    print(b[:, 1])
    print(b[1:3, :])
    print(b[-1])  # Equivalent to b[-1,:]
    c = np.array([[[0, 1, 2],  # a 3D array (two stacked 2D arrays)
                   [10, 12, 13]],
                  [[100, 101, 102],
                   [110, 112, 113]]])
    print(c.shape)
    print(c[1, ...])  # same as c[1,:,:] or c[1]
    print(c[..., 2])  # same as c[:,:,2]
    for row in b:
        print(row)
    for element in b.flat:
        print(element)


# example()
# array_creation()
# print_array()
# basic_opration()
# universal_function()
index_slice_iterate()
