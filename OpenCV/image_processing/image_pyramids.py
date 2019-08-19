"""
图像金字塔
    在做图形处理是，因为图像的大小通常不是固定的，所以会不断缩小图片来寻找目标
    图片在经过缩小之后再进行放大会变得模糊，所以也使用图像金子塔进行图像融合
"""

import cv2 as cv
import numpy as np

# 加载图片
A = cv.imread('../resources/apple.jpg')
B = cv.imread('../resources/orange.jpg')

# 创建高斯图片金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# 创建高斯图片金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# 通过高斯图片金字塔创建拉普拉斯图片金字塔
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1], GE)
    lpA.append(L)

# 通过高斯图片金字塔创建拉普拉斯图片金字塔
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1], GE)
    lpB.append(L)

# 对AB的高斯图片金字塔进行左右合并
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:int(cols/2)], lb[:, int(cols/2):]))
    LS.append(ls)

# 选定最小的一张图片进行大小还原
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# image with direct connecting each half
rows, cols, dpt = A.shape
real = np.hstack((A[:, :int(cols/2)], B[:, int(cols/2):]))
cv.imshow('Pyramid_blending2.jpg', ls_)
cv.imshow('Direct_blending.jpg', real)
cv.waitKey(0)
cv.destroyAllWindows()
