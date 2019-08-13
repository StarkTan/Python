import numpy as np
import cv2 as cv


drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def draw_circle_one(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


def draw_circle_two(event, x, y, flags, param):
    """
    创建回调函数
    """
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode is True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode is True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)  # 创建一张黑色图片数据
cv.namedWindow('image')  # 创建窗口
cv.setMouseCallback('image', draw_circle_two)  # 为窗口绑定回调函数
while 1:
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:  # 按 Esc 退出
        break
cv.destroyAllWindows()
