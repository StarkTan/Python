"""
使用
 cv.getTickCount,
 cv.getTickFrequency
检查程序性能
"""
import cv2 as cv
img1 = cv.imread('messi5.jpg')
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()

count = (e2 - e1)  # 代码运行占用时钟周期数
frequency = cv.getTickFrequency()  # 每秒内时钟的周期数
use = count/frequency  # 代码运行时间
print(use)
