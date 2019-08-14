"""
Goal:
    Access pixel values and modify them
    Access image properties
    Setting Region of Interest (ROI)
    Splitting and Merging images
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def pixel_values():
    print('=' * 20)
    img = cv.imread(r'../resources/messi5.jpg')
    px = img[100, 100]  # 获取某个点的像素颜色值
    print(px)
    blue = img[100, 100, 0]  # 获取每个像素点的蓝色数值
    print(blue)
    img[100, 100] = [255, 255, 255]  # 修改某个像素的颜色值
    print(img[100, 100])
    # 相对使用 numpy 定点查询和修改，img.item()更值得推荐
    print(img.item(10, 10, 2))
    img.itemset((10, 10, 2), 100)
    print(img.item(10, 10, 2))


def image_properties():
    print('=' * 20)
    img = cv.imread(r'../resources/messi5.jpg')
    # 获取图片的属性
    print(img.shape)  # 图片数据的shape
    print(img.size)  # 图片像素的个数
    print(img.dtype)  # 图片的数据格式


def image_roi():
    img = cv.imread(r'../resources/messi5.jpg')
    ball = img[280:340, 330:390]  # 截取感兴趣的部分
    img[273:333, 100:160] = ball
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # 解决颜色失真 opencv 彩色保存为BGR matplotlib 彩色识别 RGB
    plt.axis('off')  # to close axis #plt.xticks([]), plt.yticks([])
    plt.show()


def color_channel():
    img = cv.imread(r'../resources/messi5.jpg')
    b, g, r = cv.split(img)  # 获取三个颜色的 b = img[:, :, 0] ，img[:, :, 2] = 0

    img_new = np.zeros((342, 548, 3), np.uint8)
    img_new[:, :, 0] = b
    cv.imshow(winname='image', mat=img_new)
    cv.waitKey(0)
    img_new = np.zeros((342, 548, 3), np.uint8)
    img_new[:, :, 1] = g
    cv.imshow(winname='image', mat=img_new)
    cv.waitKey(0)
    img_new = np.zeros((342, 548, 3), np.uint8)
    img_new[:, :, 2] = r
    cv.imshow(winname='image', mat=img_new)
    cv.waitKey(0)
    img_new = cv.merge((b, g, r))
    cv.imshow(winname='image', mat=img_new)
    cv.waitKey(0)
    cv.destroyAllWindows()


def image_border():
    """
    为图片添加 padding
    """
    BLUE = [255, 0, 0]
    img = cv.imread(r'../resources/opencv-logo.png')

    # 参数： 图片数据，top, bottom, left, right， borderType，value
    replicate = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REPLICATE)
    reflect = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT)
    reflect101 = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT_101)
    wrap = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_WRAP)
    constant = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    plt.show()


# pixel_values()
# image_properties()
# image_roi()
# color_channel()
image_border()

