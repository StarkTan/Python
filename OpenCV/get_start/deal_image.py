"""
read，display，save an image
"""

import cv2 as cv
import os
from matplotlib import pyplot as plt

img = cv.imread(r'blurred.png', flags=cv.IMREAD_UNCHANGED)  # 加载图片，加载失败返回空矩阵，flags 表示图片数据的处理方式
if img is None:
    print('Image load failed！')
    exit(1)
cv.imshow(winname='image', mat=img)  # 将图片显示出来,闪退
cv.waitKey(0)  # 0 表示一直等待键盘操作, 触发是可以获取键盘输入值
cv.destroyAllWindows()  # 关闭已经打开的窗口

if not os.path.exists(r'..\cache'):
    os.mkdir(r'..\cache')
cv.imwrite(r'..\cache\copy.png', img)  # 保存图片

# 使用 matplotlib 画出来
# plt.imshow(img)  # 颜色失真
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)) # 解决颜色失真 opencv 彩色保存为BGR matplotlib 彩色识别 RGB
plt.axis('off')  # to close axis #plt.xticks([]), plt.yticks([])
plt.show()












