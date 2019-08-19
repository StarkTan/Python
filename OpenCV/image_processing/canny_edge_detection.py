"""
进行图像边缘探测
    Canny Edge Detection，边缘检测
    1. 将图像转为灰度(grayscale)
    2. 计算梯度(gradient)
    3. 通过检测到物体边界，进而得到该物体形状
"""


import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../resources/messi5.jpg', 0)
edges = cv.Canny(img, 100, 200)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

