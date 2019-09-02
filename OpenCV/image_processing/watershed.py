"""
分水岭算法找出物体
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def show_img(data):
    data = np.array(data, dtype=np.float32)
    cv.imshow(winname='test', mat=data)
    cv.waitKey(0)
    cv.destroyWindow(winname='test')


img = cv.imread('../resources/coins.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 对图像进行自动二值化处理
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
show_img(thresh)

kernel = np.ones((3, 3), np.uint8)
# 对图像进行开处理降噪 迭代两次
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
show_img(opening)
# 对降噪之后的数据进行膨胀，迭代3次
sure_bg = cv.dilate(opening, kernel, iterations=3)
show_img(sure_bg)
# 计算图像中每一个非零点距离离自己最近的零点的距离
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
show_img(dist_transform)
# 使用上面的距离进行阈值处理，可以获取目标图形的中心
ret, sure_fg = cv.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
show_img(sure_fg)
# 在膨胀图片中减去中心点（为了后面做掩膜）
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
show_img(unknown)
# 进行连通域计算
ret, markers = cv.connectedComponents(sure_fg)
show_img(markers)
markers = markers+1
# 使用掩膜处理
markers[unknown == 255] = 0
show_img(markers)
# 进行分水岭处理
markers = cv.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
show_img(img)
