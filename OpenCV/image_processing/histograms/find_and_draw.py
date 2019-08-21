"""
生成图片的直方图。
直方图用于分析图片的光对照，明暗等
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def draw_1():
    """
    直接使用 matplotlib 画出直方图
    """
    img = cv.imread('../../resources/home.jpg', 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def draw_2():
    """
    使用opencv 分别对红绿蓝做直方图计算
    """
    img = cv.imread('../../resources/home.jpg')
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])  # 计算某个颜色的直方图数据
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def draw_3():
    """
    将整张图片和图片部分的直方图数据作对比
    """
    img = cv.imread('../../resources/home.jpg', 0)
    # create a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:300, 100:400] = 255
    masked_img = cv.bitwise_and(img, img, mask=mask)
    # Calculate histogram with mask and without mask
    # Check third argument for mask
    hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()


# draw_1()
# draw_2()
draw_3()
