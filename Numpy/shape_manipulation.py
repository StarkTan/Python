import numpy as np


def change_shape():
    a = np.floor(10 * np.random.random((3, 4)))
    print(a)
    print(a.shape)
    print(a.ravel())  # 展开数组
    print(a.reshape(6, 2))
    print(a.T)  # 转置
    a.resize((2, 6))  # 修改源数组
    print(a)
    print(a.reshape(3, -1))  # 遇见-1会自动补充


def stack_together():
    a = np.floor(10 * np.random.random((2, 2)))
    print(a)
    b = np.floor(10 * np.random.random((2, 2)))
    print(b)
    print(np.vstack((a, b)))  # shape[0] 增加
    print(np.hstack((a, b)))  # shape[1] 增加
    print(np.column_stack((a, b)))  # 仅对2D数组与hstack相同,


def split_array():
    a = np.floor(10 * np.random.random((2, 12)))
    print(a)
    print(np.hsplit(a, 3))
    print(np.hsplit(a, (3, 4)))  # Split a after the third and the fourth column


# change_shape()
# stack_together()
split_array()
