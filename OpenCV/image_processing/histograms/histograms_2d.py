"""
展示带颜色图片的2D直方图
"""


import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../../resources/home.jpg')
# 2D 直方图需要把图片格式转化 从 BGR 转化到 HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# channels = [0,1] because we need to process both H and S plane.
# bins = [180,256] 180 for H plane and 256 for S plane.
# range = [0,180,0,256] Hue value lies between 0 and 180 & Saturation lies between 0 and 256.
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv.imshow(winname ='home', mat=img)
plt.imshow(hist,interpolation='nearest')
plt.show()