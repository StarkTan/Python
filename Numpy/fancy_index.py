import numpy as np


def index_with_array_1():
    a = np.arange(12) ** 2
    i = np.array([1, 1, 3, 8, 5])
    print(a[i])
    j = np.array([[3, 4], [9, 7]])
    print(a[j])
    palette = np.array([[0, 0, 0],  # black
                        [255, 0, 0],  # red
                        [0, 255, 0],  # green
                        [0, 0, 255],  # blue
                        [255, 255, 255]])  # white
    image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                      [0, 3, 4, 0]])
    print(palette[image])  # the (2,4,3) color image

    a = np.arange(12).reshape(3, 4)
    print(a)
    i = np.array([[0, 1],  # indices for the first dim of a
                  [1, 2]])
    j = np.array([[2, 1],  # indices for the second dim
                  [3, 3]])
    print(a[i, j])  # i and j must have equal shape
    print(a[i, 2])
    print(a[:, j])  # i.e., a[ : , j]


def index_with_array_2():
    time = np.linspace(20, 145, 5)  # time scale
    data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
    print(time)
    print(data)
    ind = data.argmax(axis=0)  # index of the maxima for each series
    print(ind)
    time_max = time[ind]  # times corresponding to the maxima
    data_max = data[ind, range(data.shape[1])]  # => data[ind[0],0], data[ind[1],1]...
    print(time_max)
    print(data_max)
    print(np.all(data_max == data.max(axis=0)))

    a = np.arange(5)
    print(a)
    a[[1, 3, 4]] = 0
    print(a)
    a = np.arange(5)
    a[[0, 0, 2]] = [1, 2, 3]
    print(a)
    a = np.arange(5)
    a[[0, 0, 2]] += 1
    print(a)


def index_with_boolean():
    a = np.arange(12).reshape(3, 4)
    b = a > 4
    print(b)
    print(a[b])
    a[b] = 0
    print(a)

    a = np.arange(12).reshape(3, 4)
    b1 = np.array([False, True, True])
    b2 = np.array([True, False, True, False])
    print(a[b1, :])
    print(a[b1])
    print(a[:, b2])
    print(a[b1, b2])


def ix_fuction():
    a = np.array([2, 3, 4, 5])
    b = np.array([8, 5, 4])
    c = np.array([5, 4, 6, 8, 3])
    ax, bx, cx = np.ix_(a, b, c)
    print(ax)
    print(bx)
    print(cx)
    print(ax.shape, bx.shape, cx.shape)
    result = ax + bx * cx
    print(result)
    print(result[3, 2, 4])
    print(a[3] + b[2] * c[4])


# index_with_array_1()
# index_with_array_2()
# index_with_boolean()
ix_fuction()
