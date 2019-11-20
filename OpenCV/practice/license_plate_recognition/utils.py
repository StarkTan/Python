import cv2
import numpy as np


def load_pic(path, flag=cv2.IMREAD_COLOR):
    """
    IMREAD_COLOR 彩色图像
    IMREAD_GRAYSCALE 灰度图像
    IMREAD_ANYCOLOR 任意图像
    """
    return cv2.imread(path, flag)


def resize_pic(img_data, max_width=1000):
    rows, cols = img_data.shape[:2]  # 获取图像的高宽
    if cols > max_width:
        change_rate = max_width / cols
        img_data = cv2.resize(img_data, (max_width, int(rows * change_rate)), interpolation=cv2.INTER_AREA)
    return img_data


def chose_licence_plate(contours, min_area=2000):
    temp_contours = []
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            temp_contours.append(contour)
    car_plate = []
    for temp_contour in temp_contours:
        # 算出最小外包矩形
        rect_tupple = cv2.minAreaRect(temp_contour)
        rect_width, rect_height = rect_tupple[1]
        if rect_width < rect_height:
            rect_width, rect_height = rect_height, rect_width
        aspect_ratio = rect_width / rect_height
        # 车牌正常情况下宽高比在2 - 5.5之间
        if 2 < aspect_ratio < 5.5:
            car_plate.append(temp_contour)
            rect_vertices = cv2.boxPoints(rect_tupple)
            rect_vertices = np.int0(rect_vertices)
    return car_plate


def find_waves(threshold, histogram):
    up_point = -1  # 上升点
    is_peak = False
    if histogram[0] > threshold:
        up_point = 0
        is_peak = True
    wave_peaks = []
    for i, x in enumerate(histogram):
        if is_peak and x < threshold:
            if i - up_point > 2:
                is_peak = False
                wave_peaks.append((up_point, i))
        elif not is_peak and x >= threshold:
            is_peak = True
            up_point = i
    if is_peak and up_point != -1 and i - up_point > 4:
        wave_peaks.append((up_point, i))
    return wave_peaks


def remove_plate_upanddown_border(card_img):
    """
    这个函数将截取到的车牌照片转化为灰度图，然后去除车牌的上下无用的边缘部分，确定上下边框
    输入： card_img是从原始图片中分割出的车牌照片
    输出: 在高度上缩小后的字符二值图片
    """
    plate_gray_Arr = cv2.cvtColor(card_img, cv2.COLOR_BGR2GRAY)
    ret, plate_binary_img = cv2.threshold(plate_gray_Arr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    row_histogram = np.sum(plate_binary_img, axis=1)  # 数组的每一行求和
    row_min = np.min(row_histogram)
    row_average = np.sum(row_histogram) / plate_binary_img.shape[0]
    row_threshold = (row_min + row_average) / 2
    wave_peaks = find_waves(row_threshold, row_histogram)
    # 接下来挑选跨度最大的波峰
    wave_span = 0.0
    for wave_peak in wave_peaks:
        span = wave_peak[1] - wave_peak[0]
        if span > wave_span:
            wave_span = span
            selected_wave = wave_peak
    plate_binary_img = plate_binary_img[selected_wave[0]:selected_wave[1], :]
    # cv2.imshow("plate_binary_img", plate_binary_img)

    return plate_binary_img