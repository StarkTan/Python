"""
    Learn several arithmetic operations on images like addition, subtraction, bitwise operations etc.
    You will learn these functions : cv.add(), cv.addWeighted() etc.
"""
import cv2 as cv
import numpy as np


def image_add():
    """
    展示 add()
    :return:
    """
    x = np.uint8([250])
    y = np.uint8([10])
    print(cv.add(x, y))  # 250+10 = 260 => 255
    print(x + y)  # 250+10 = 260 % 256 = 4


def image_blend():
    """
    展示  cv.addWeighted() 将两张图片进行重叠
    :return:
    """
    img1 = cv.imread('ml.png')
    img2 = cv.imread('opencv-logo.png')
    # 修改图片二的大小和图片一相同
    img2 = cv.resize(img2, (img1.shape[1],img1.shape[0]), interpolation=cv.INTER_CUBIC)
    print(img1.shape)
    print(img2.shape)
    # dst=α⋅img1+β⋅img2+γ  参数： 图片数据1，权重（α），图片数据2，权重（β），补偿（γ）
    dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def bitwise():
    """
    对图片进行位操作
    :return:
    """
    img1 = cv.imread('messi5.jpg')
    img2 = cv.imread('opencv-logo-white.png')

    # 根据图片二的大小在图片一种选定操作区域
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 将图片转化成黑白
    # 对输入单通道矩阵逐像素进行固定阈值分割。典型应用是从灰度图像获取二值图像，或消除灰度值过大或过小的噪声
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)  # 对数据进行非操作，获取掩膜
    img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)  # 为操作区域添加掩膜
    img2_fg = cv.bitwise_and(img2, img2, mask=mask)  # 获取掩膜区域对应的颜色
    dst = cv.add(img1_bg, img2_fg)  # 将两个数据进行相加
    img1[0:rows, 0:cols] = dst # 对目标图像进行替换

    cv.imshow('res', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()


# image_add()
# image_blend()
bitwise()

