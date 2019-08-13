import numpy as np
import cv2 as cv


img = np.zeros((512, 512, 3), np.uint8)  # 创建全黑的图片数据

cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # 添加对角的蓝线 大小为 5px

cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 添加矩形 参数为 两个对角坐标、颜色、大小

cv.circle(img, (447, 63), 63, (0, 0, 255), -1)  # 添加圆形 参数为中心、半径、颜色、线条大小（-1 表示内部填满）

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))  # 转化为三维数据
cv.polylines(img, [pts], True, (0, 255, 255))  # 添加多边形

font = cv.FONT_HERSHEY_SIMPLEX
#  添加文字 参数： 图片数据，文字，坐标，字体，字体大小，颜色，线条像素，轮廓
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 8, cv.LINE_AA)

cv.imshow(winname='image', mat=img)  # 将图片显示出来,闪退
cv.waitKey(0)  # 0 表示一直等待键盘操作, 触发是可以获取键盘输入值
cv.destroyAllWindows()  # 关闭已经打开的窗口


