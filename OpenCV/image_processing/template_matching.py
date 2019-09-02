"""
模式匹配，图像识别
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../resources/messi5.jpg', 0)
img2 = img.copy()
template = cv.imread('../resources/messi_face.jpg', 0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED',  # 平方差匹配法、归一化平方差匹配法
           'cv.TM_CCORR','cv.TM_CCORR_NORMED',  # 相关匹配法、 归一化相关匹配法
           'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']  # 系数匹配法、归一化系数匹配法

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # 进行匹配计算
    res = cv.matchTemplate(img, template, method)
    # 计算结果中的最大值、最小值，给出位置
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # 系数匹配法和归一化系数匹配法取最小值为最佳匹配，其它的是最大值最佳匹配
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

# 多个匹配
import numpy as np
img_rgb = cv.imread('../resources/mario.jpg')
img_copy = img_rgb.copy()
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('../resources/mario_coin.jpg', 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

img_rgb = np.hstack((img_copy, img_rgb))
cv.imshow(winname='res.png', mat=img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()
