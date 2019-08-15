"""
目的：模糊降噪
使用多种低通过滤的方式平滑图片，减少噪声
创建使用自己的过滤方式
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def convolution_2d():
    """
    使用filter2D对图片进行自定义卷积处理
    """
    img = cv.imread(r'..\resources\opencv-logo.png')
    kernel = np.ones((5, 5), np.float32) / 25  # 定义自己的 kernel
    dst = cv.filter2D(img, -1, kernel)  # 调用用 filter2D 对源图片进行卷积运算
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()


def image_blurring():
    """
    使用opencv提供的方法对图片进行平滑处理
    """
    img = cv.imread(r'..\resources\opencv-logo.png')
    # blur = cv.blur(img, (5, 5)) # 对应上面使用 5x5 的kernel的处理
    # blur = cv.GaussianBlur(img, (5, 5), 0)
    # blur = cv.medianBlur(img, 5)
    blur = cv.bilateralFilter(img, 9, 75, 75)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


# convolution_2d()
image_blurring()
