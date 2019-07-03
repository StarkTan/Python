import numpy as np


def no_copy():
    a = np.arange(12)
    b = a
    print(b is a)
    b.shape = 3, 4
    print(a.shape)
    print(id(a))
    print(id(b))


def view_or_shallow_copy():
    a = np.arange(12)
    b = a
    b.shape = 3, 4
    c = a.view()
    print(c is a)
    print(c.base is a)
    print(c.flags.owndata)
    c.shape = 2, 6
    print(a.shape)  # shape 不会变化
    print(a)
    c[0, 4] = 1234
    print(a)  # data 会被改变
    s = a[:, 1:3]  # s 是a的view
    s[:] = 10
    print(a)


def deep_copy():
    a = np.arange(12)
    b = a
    b.shape = 3, 4
    d = a.copy()
    print(d is a)
    print(d.base is a)
    d[0, 0] = 9999
    print(a)

    a = np.arange(int(1e8))
    b = a[:100].copy()
    del a  # the memory of ``a`` can be released.


# no_copy()
# view_or_shallow_copy()
deep_copy()
