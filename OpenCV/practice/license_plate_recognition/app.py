"""
https://blog.csdn.net/weixin_41695564/article/details/79712393
OpenCV实战：车牌识别
"""
import cv2
import numpy as np
import OpenCV.practice.license_plate_recognition.utils as utils


def show_img(name, img_data):
    cv2.imshow(name, img_data)
    cv2.waitKey()
    cv2.destroyWindow(name)


# 加载图片
img = utils.load_pic('resources/test_1.png')
show_img('img', img)
# 将图片转换成灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show_img('gray_img', gray_img)
# 限制图片的大小
resize_img = utils.resize_pic(gray_img)
# show_img('resize_img', resize_img)
# 对图片进行高斯降噪
blur_img = cv2.GaussianBlur(gray_img, (5,5), 0, 0, cv2.BORDER_DEFAULT)
# show_img('blur_img', blur_img)
# 对图片进行形态学处理：开运算，获取模块
kernel = np.ones((24, 24), np.uint8)
open_img = cv2.morphologyEx(blur_img, cv2.MORPH_OPEN, kernel)
# show_img('open_img', open_img)
# 将目标放在模块上
open_img = cv2.addWeighted(blur_img, 1, open_img, -1, 0)
# show_img('open_img', open_img)
# 对图片进行阈值分割
ret3, otsu_img = cv2.threshold(open_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# show_img('otsu_img', otsu_img)
# 进行边缘检测
edges_img = cv2.Canny(otsu_img, 100, 200)
# show_img('edges_img', edges_img)
# 再对图像进行闭运算和开运算，获取模块
kernel = np.ones((10, 10), np.uint8)
close_img = cv2.morphologyEx(edges_img, cv2.MORPH_CLOSE, kernel)
# show_img('close_img', close_img)
open_img = cv2.morphologyEx(close_img, cv2.MORPH_OPEN, kernel)
show_img('open_img', open_img)
# 获取图片存在的矩形区域
contours, hierarchy = cv2.findContours(open_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 获取可能的车牌矩形范围
car_plates = utils.chose_licence_plate(contours)

for car_plate in car_plates:
    row_min, col_min = np.min(car_plate[:, 0, :], axis=0)
    row_max, col_max = np.max(car_plate[:, 0, :], axis=0)
    cv2.rectangle(img, (row_min, col_min), (row_max, col_max), (0, 255, 0), 2)
    card_img = img[col_min:col_max, row_min:row_max, :]
    show_img('img', img)
    cv2.imwrite("E:/card_img.jpg", card_img)
    break


# 处理车牌
card_img = utils.load_pic('E:/card_img.jpg')
show_img('card_img', card_img)
card_img = utils.remove_plate_upanddown_border(card_img)
show_img('card_img', card_img)






