"""
To find the different features of contours, like area, perimeter, centroid, bounding box etc
"""

import numpy as np
import cv2 as cv


def feature_1():
    """
    图像矩 cv.moments(cnt) ： mji 几何矩，muji 中心距，nuji 中心归一化距
    图形面积 cv.contourArea(cnt)
    图形周长 cv.arcLength(cnt, True)
    图形多边拟合 cv.approxPolyDP(cnt, epsilon, True) 图形点集，轮廓点之间的最大距离数，是否封闭图形
    图形凸包  cv.convexHull(cnt[, hull[, clockwise[, returnPoints]]) 图形点集，凸包点集，输出包点的方向，输出类型（点或索引）
    检查凸性 cv.isContourConvex(approx)
    外接矩形，外接最小矩阵
    最小包围圆
    椭圆拟合
    拟合线
    """
    img = cv.imread('../../resources/start_light.png')
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[1]

    img_copy = img.copy()
    image = cv.drawContours(img_copy, [cnt], 0, (0, 255, 0), 3)
    cv.imshow(winname='contours', mat=image)
    cv.waitKey(0)
    cv.destroyWindow(winname='contours')

    M = cv.moments(cnt)  # 计算一个图像的图像矩
    print(M)
    # 计算图像中心
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print(cx, cy)
    # 计算图像的轮廓面积
    area = cv.contourArea(cnt)
    print(area)
    # 计算图形的周长
    perimeter = cv.arcLength(cnt, True)
    print(perimeter)
    # 多边拟合函数
    epsilon = 0.06 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    img_copy = img.copy()
    image = cv.drawContours(img_copy, [approx], 0, (0, 255, 0), 3)
    cv.imshow(winname='approximation', mat=image)
    cv.waitKey(0)
    epsilon = 0.01 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    img_copy = img.copy()
    image = cv.drawContours(img_copy, [approx], 0, (0, 255, 0), 3)
    cv.imshow(winname='approximation', mat=image)
    cv.waitKey(0)
    cv.destroyWindow(winname='approximation')
    # 凸包计算
    hull = cv.convexHull(cnt)
    img_copy = img.copy()
    image = cv.drawContours(img_copy, [hull], 0, (0, 255, 0), 3)
    cv.imshow(winname='convexHull', mat=image)
    cv.waitKey(0)
    cv.destroyWindow(winname='convexHull')

    # 凸性检测 检测一个曲线是不是凸的
    print(cv.isContourConvex(approx))
    print(cv.isContourConvex(hull))

    # 外接矩形展示
    cnt = contours[2]
    x, y, w, h = cv.boundingRect(cnt)  # 计算方式一：算出矩阵起始坐标和高宽
    img_copy = img.copy()
    cv.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)  # 在图片中画出第一个矩形

    rect = cv.minAreaRect(cnt)  # 旋转获取最小外接矩阵数据 返回 ( center (x,y), (width, height), angle of rotation )
    box = cv.boxPoints(rect)  # 根据矩阵数据获取4个坐标点
    box = np.int0(box)
    cv.drawContours(img_copy, [box], 0, (0, 0, 255), 2)

    cv.imshow(winname='boundingRect', mat=img_copy)
    cv.waitKey(0)
    cv.destroyWindow(winname='boundingRect')

    # 最小包围圆
    img_copy = img.copy()
    (x, y), radius = cv.minEnclosingCircle(cnt)  # 获取最小包围圆的 圆心坐标和半径
    center = (int(x), int(y))
    radius = int(radius)
    cv.circle(img_copy, center, radius, (0, 255, 0), 2)
    cv.imshow(winname='EnclosingCircle', mat=img_copy)
    cv.waitKey(0)
    cv.destroyWindow(winname='EnclosingCircle')

    # 椭圆拟合
    img_copy = img.copy()
    ellipse = cv.fitEllipse(cnt)  # 返回旋转的包含椭圆的矩形数据
    cv.ellipse(img_copy, ellipse, (0, 255, 0), 2)  # 根据矩形数据画图
    cv.imshow(winname='fitEllipse', mat=img_copy)
    cv.waitKey(0)
    cv.destroyWindow(winname='fitEllipse')

    # 拟合线
    img_copy = img.copy()
    rows, cols = img_copy.shape[:2]  # 获取图像的长宽
    # 参数：待拟合的点集，最小距离的类型，距离参数，拟合直线所需要的径向和角度精度 输出 前俩个为方向（计算斜率），后两个为直线上一点
    [vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv.line(img_copy, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
    cv.imshow(winname='line', mat=img_copy)
    cv.waitKey(0)
    cv.destroyWindow(winname='line')


feature_1()
