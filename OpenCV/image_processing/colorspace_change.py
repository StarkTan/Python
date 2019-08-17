"""
In this tutorial, you will learn how to convert images from one color-space to another,
        like BGR ↔ Gray, BGR ↔ HSV etc.
You will learn following functions : cv.cvtColor(), cv.inRange() etc.
"""

import cv2 as cv
import numpy as np


def list_method():
    flags = [i for i in dir(cv) if i.startswith('COLOR_')]
    print(flags)


def object_tracking():
    # cap = cv.VideoCapture(r'../resources/test2.mp4')
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()  # 获取一帧的图片数据
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # 将图片数据从BGR格式转换成HSV格式
        lower_blue = np.array([110, 50, 50])  # 定义要捕获颜色的下限
        upper_blue = np.array([130, 255, 255])  # 定义要捕获颜色的上限
        mask = cv.inRange(hsv, lower_blue, upper_blue)  # 处理图片获取掩膜
        res = cv.bitwise_and(frame, frame, mask=mask)  # 将掩膜作用在图片上，显示目标区域
        cv.imshow('frame', frame)
        cv.imshow('mask', mask)
        cv.imshow('res', res)
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()


# list_method()
object_tracking()
