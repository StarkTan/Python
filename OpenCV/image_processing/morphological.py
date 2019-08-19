"""

形态学操作
We will learn different morphological operations like Erosion, Dilation, Opening, Closing etc.
We will see different functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.
"""
import cv2 as cv
import numpy as np
import random


def noise(data, noise_data):
    """
    为图片增加噪点
    """
    data = data.copy()
    height, width = data.shape
    count = int(data.size*0.02)
    for i in range(0, count):
        x = int(height*random.random())
        y = int(width*random.random())
        data[x][y] = noise_data
    return data


img_array = []
img = cv.imread(r'../resources/j.png', 0)

kernel = np.ones((5, 5), np.uint8)  # 使用5x5为1的矩阵作为核心
erosion = cv.erode(img, kernel, iterations=1)  # 腐蚀 图片内容
erosion = np.hstack((img, erosion))
img_array.append(erosion)

dilation = cv.dilate(img, kernel, iterations=1)  # 膨胀 图片内容
dilation = np.hstack((img, dilation))
img_array.append(dilation)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开运算 先腐蚀后膨胀，去除噪点
noise_img = noise(img, 255)
opening = np.hstack((noise_img, opening))
img_array.append(opening)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭运算 先膨胀后腐蚀，去除噪点
noise_img = noise(img, 0)
closing = np.hstack((noise_img, closing))
img_array.append(closing)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)  # 形态学梯度 一幅图像膨胀与腐蚀的差别，结果看上去是物体的轮廓
gradient = np.hstack((img, gradient))
img_array.append(gradient)

kernel = np.ones((9, 9), np.uint8)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)  # 礼帽：原始图-开运算的图像=礼帽图像
tophat = np.hstack((img, tophat))
img_array.append(tophat)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)  # 黑帽 闭运算图像-原始图像
blackhat = np.hstack((img, blackhat))
img_array.append(blackhat)

for img in img_array:
    cv.imshow(winname='morphological', mat=img)
    cv.waitKey(0)

cv.destroyAllWindows()

# 内置卷积核
print(cv.getStructuringElement(cv.MORPH_RECT, (5, 5)))  # 矩形卷积核
print(cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)))  # 椭圆形卷积核
print(cv.getStructuringElement(cv.MORPH_CROSS, (5, 5)))  # 十字形卷积核
