"""
Learn to apply different geometric transformation to images
    like translation, rotation, affine transformation etc.
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def scale():
    """
    对图片进行缩放的两种方法
    """
    img = cv.imread(r'../resources/messi5.jpg')
    cv.imshow(winname='image', mat=img)
    cv.waitKey(0)
    # 对图片进行 x ， y上的缩放
    res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
    cv.imshow(winname='image', mat=res)
    cv.waitKey(0)
    height, width = img.shape[:2]
    # 将图片缩放到指定大小
    res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)
    cv.imshow(winname='image', mat=res)
    cv.waitKey(0)

    cv.destroyAllWindows()


def translation():
    """
    对图片进行平移操作，使用函数  cv.warpAffine() 针对灰色处理后的数据
    向量公式
     M = | 1  0 tx |
        | 0  1 ty |
    :return:
    """
    img = cv.imread(r'../resources/messi5.jpg', flags=cv.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    # 分别在x，y上正向移动 100,50
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    # 进行向量计算获取目标数据
    dst = cv.warpAffine(img, M, (cols, rows))

    cv.imshow('img', img)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def rotation():
    """
    对图片进行旋转
    普通旋转的 使用向量：
    M=[cosθ−sinθ
       sinθcosθ]
    但 openCV中支持旋转带缩放，使用向量
    M=[ α β (1−α)⋅center.x−β⋅center.y
       −β α β⋅center.x+(1−α)⋅center.y]
    其中 α=scale⋅cosθ, β=scale⋅sinθ
    M 使用 getRotationMatrix2D 来获取
    """
    img = cv.imread(r'../resources/messi5.jpg', flags=cv.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    # 参数 ： 旋转中心点，角度，放大倍数
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 0.5)
    dst = cv.warpAffine(img, M, (cols, rows))

    cv.imshow('img', img)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


def affine_transformation():
    """
    仿射变换,变换的向量 M 可以通过 定出原图中的三个点和目标图中的三个点
    使用 cv.getAffineTransform 获取需要的向量
    """

    img = cv.imread(r'../resources/messi5.jpg')
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv.getAffineTransform(pts1, pts2)  # 使用三个点对应的变换获取向量
    dst = cv.warpAffine(img, M, (cols, rows))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


def perspective_transformation():
    """
    透视变化,变换的向量 M 可以通过 定出原图中的4个点和目标图中的4个点
    使用 cv.getPerspectiveTransform 获取需要的向量
    :return:
    """
    img = cv.imread(r'../resources/messi5.jpg')
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv.getPerspectiveTransform(pts1, pts2) # 使用四个点对应的变换获取向量
    dst = cv.warpPerspective(img, M, (300, 300))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


# scale()
# translation()
# rotation()
# affine_transformation()
perspective_transformation()
