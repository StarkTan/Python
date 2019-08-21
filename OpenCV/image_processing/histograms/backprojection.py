"""
    反向投影
    反向投影图就是图像对应位置像素的数量统计，也可以看做是密度统计。
    反向投影图在某一位置的值是原图对应位置的像素值在原图的总数目

"""

import numpy as np
import cv2 as cv

# 加载目标图片
target = cv.imread('../../resources/messi5.jpg')
# 获取感兴趣区域
roi = target[275:300, 0:120]
# 进行数据格式转换
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# 计算感兴趣区域的2D直方图
roihist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# 归一化处理
cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
# 使用感兴趣区域对目标区域进行反向投影
dst = cv.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
# 创建卷积核
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# 对2D图像进行卷积运算
cv.filter2D(dst, -1, disc, dst)

# 进行阈值处理
ret, thresh = cv.threshold(dst, 50, 255, 0)
thresh = cv.merge((thresh, thresh, thresh))

# 进行图片位Add
res = cv.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv.imwrite('../../cache/res.jpg', res)

