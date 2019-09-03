"""
Harris 角点探测
角点是一幅图像上最明显与重要的特征，对于一阶导数而言，角点在各个方向的变化是最大的，而边缘区域在只是某一方向有明显变化
"""


import numpy as np
import cv2 as cv


def find_conner():
    filename = '../resources/chessboard.png'
    img = cv.imread(filename)
    img = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # img - Input image, it should be grayscale and float32 type.
    # blockSize - It is the size of neighbourhood considered for corner detection
    # ksize - Aperture parameter of Sobel derivative used.
    # k - Harris detector free parameter in the equation.
    dst = cv.cornerHarris(gray, 2, 3, 0.04)

    # result is dilated for marking the corners, not important
    dst = cv.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01*dst.max()] = [0, 0, 255]
    cv.imshow('dst', img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


def find_corner_with_subpixel():
    filename = '../resources/chessboard.png'
    img = cv.imread(filename)
    img = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # find Harris corners
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)
    ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    # find centroids
    ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
    # define the criteria to stop and refine the corners
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    # Now draw them
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    img[res[:, 1], res[:, 0]] = [0, 0, 255]
    img[res[:, 3], res[:, 2]] = [0, 255, 0]
    # 放大才可以看到
    cv.imshow('dst', img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


#find_conner()
find_corner_with_subpixel()
