"""
霍夫变换，圆形检测
"""

import cv2 as cv
import numpy as np
img = cv.imread('../resources/opencv-logo-white.png',0)
img = cv.medianBlur(img, 5)  # 中值滤波，降噪处理
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
# 找出图片中的圆
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
cv.imshow(winname='houghcircle.jpg', mat=cimg)
cv.waitKey(0)
cv.destroyAllWindows()
