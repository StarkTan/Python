"""
直方图均衡
    直方图均衡化是使用图像直方图对对比度进行调整的图像处理方法。
    目的在于提高图像的全局对比度，使亮的地方更亮，暗的地方更暗
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def equalization_numpy():
    """
    使用 numpy 进行直方图均衡
    """
    img = cv.imread('../../resources/wiki.jpg', 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img2 = cdf[img]
    cv.imshow(winname='xx', mat=img2)
    cv.waitKey(0)

    hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.plot(cdf_normalized, color='b')
    plt.hist(img2.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


def equalization_opencv():
    """
    使用 opencv 中的cv.equalizeHist(img) 进行直方图均衡
    """
    img = cv.imread('../../resources/wiki.jpg', 0)
    equ = cv.equalizeHist(img)
    res = np.hstack((img, equ))  # stacking images side-by-side
    cv.imshow('res.png', res)
    cv.waitKey(0)
    cv.destroyAllWindows()


def equalization_opencv_clahe():
    """
    使用 opencv 的普通直方图均衡和 clahe 的均衡
    """
    img = cv.imread('../../resources/clahe.jpg', 0)
    cv.imshow('clahe', img)
    cv.waitKey(0)

    equ = cv.equalizeHist(img)
    cv.imshow('clahe', equ)
    cv.waitKey(0)

    # 创建一个 CLAHE 对象
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)
    cv.imshow('clahe', cl1)
    cv.waitKey(0)
    cv.destroyAllWindows()


# equalization_numpy()
# equalization_opencv()
equalization_opencv_clahe()
