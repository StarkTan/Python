"""
像素阈值 解释 ：https://www.jianshu.com/p/ffc0fe523fdc
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def simple_threshold():
    """
    全局简单阈值处理
    """
    img = cv.imread(r'../resources/gradient.png', 0)
    # 阈值化处理 参数：原图片数据，阈值，极大值，处理方式
    ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # 二进制阈值 大于 127 的像素设置为225，小于设置为0
    ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  # 反二进制阈值
    ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  # 截断阈值化 大于 127 的像素设置为127
    ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # 阈值化为0 小于 127的像素设置为0
    ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # 反阈值化为0 大于 127的像素设置为0
    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def adaptive_threshold():
    """
    自适应阈值 adaptiveThreshold、自动根据周围阈值设置阈值大小
    参数 ： 数据源，最大灰度值，阈值类型，计算阈值的方法，计算阈值的区域大小，计算阈值的偏移（减）
    """
    img = cv.imread(r'../resources/sudoku.png', 0)
    img = cv.medianBlur(img, 5)
    ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # 简单阈值处理
    th2 = cv.adaptiveThreshold(img, 255,
                               cv.ADAPTIVE_THRESH_MEAN_C,  # 阈值取自相邻区域的平均值
                               cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(img, 255,
                               cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # 阈值取值相邻区域的加权和，权重为一个高斯窗口
                               cv.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def otsu_binarization():
    """
    Otsu’s 二值化, 简单来说就是对一副双峰图像自动根据其直方图计算出一个阈值
    """
    img = cv.imread(r'../resources/sudoku.png', 0)
    ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    blur = cv.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
              'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
              'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()


# simple_threshold()
# adaptive_threshold()
otsu_binarization()
