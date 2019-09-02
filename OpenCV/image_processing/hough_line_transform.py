"""
霍夫变换，直线检测
使用 cv.HoughLines()探测直线，cv.HoughLinesP()补全直线
"""

import cv2 as cv
import numpy as np
img = cv.imread(cv.samples.findFile('../resources/sudoku.png'))
img_copy = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 先对图片进行边缘探测
edges = cv.Canny(gray, 50, 150, apertureSize=3)
# 从边缘探测中获取直线
lines = cv.HoughLines(edges, 1, np.pi/180, 200)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img_copy, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow(winname='houghlines3.jpg', mat=img_copy)
cv.waitKey(0)
cv.destroyAllWindows()

# 进行直线补全
img_copy = img.copy()
# 获取用于补全直线的字段
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imshow(winname='houghlines3.jpg', mat=img_copy)
cv.waitKey(0)
cv.destroyAllWindows()
