"""
图像梯度：
    1. 寻找图片的梯度和边缘
    2. 学习 cv.Sobel(), cv.Scharr(), cv.Laplacian() etc
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def find_edge():
    """
    注意，使用8位计算cv.CV_8U 容易丢失数据
    :return:
    """
    img = cv.imread('../resources/gradients.jpg', 0)
    laplacian = cv.Laplacian(img, cv.CV_64F)
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()

find_edge()
