"""
获取目标轮廓
"""

import numpy as np
import cv2 as cv
img = cv.imread('../../resources/test.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 使用二进制图片（灰色图片）
ret, thresh = cv.threshold(imgray, 127, 255, 0)  # 对图片进行阈值处理
# 使用阈值数据找到轮廓 参数：数据源，检索模式，计算方法，返回：轮廓数组，向量关系
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 画出所有的轮廓
img_copy = img.copy()
image = cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
cv.imshow(winname='contours', mat=image)
cv.waitKey(0)

# 画出指定的轮廓
img_copy = img.copy()
image = cv.drawContours(img_copy, contours, 1, (0, 255, 0), 3)
cv.imshow(winname='contours', mat=image)
cv.waitKey(0)

# 画出指定的轮廓
img_copy = img.copy()
cnt = contours[2]
image = cv.drawContours(img_copy, [cnt], 0, (0, 255, 0), 3)
cv.imshow(winname='contours', mat=image)
cv.waitKey(0)
cv.destroyAllWindows()
