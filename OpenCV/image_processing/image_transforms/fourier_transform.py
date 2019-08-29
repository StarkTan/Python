"""
图片的傅里叶变换
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def fourier_transform_numpy():
    # 傅里叶转化
    img = cv.imread('../../resources/messi5.jpg', 0)
    f = np.fft.fft2(img)  # 将图片数据转化成2D傅里叶信号
    fshift = np.fft.fftshift(f)  # 将图像中的低频部分移动到图像的中心
    # 傅里叶变换将图像转换成幅值谱 ，取对数的目的为了将数据变化到较小的范围（比如0-255）
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    # 转化成图片
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    fshift[crow - 30:crow + 31, ccol - 30:ccol + 31] = 0  # 去除某一频段的数据
    f_ishift = np.fft.ifftshift(fshift)  # 将图像中的低频部分移动到图像的中心
    img_back = np.fft.ifft2(f_ishift)  # 将傅里叶信号转化成图片
    img_back = np.real(img_back)  # 将复数变化成实数
    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(img_back, cmap='gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    plt.show()


def fourier_transform_opencv():
    # 傅里叶转化
    img = cv.imread('../../resources/messi5.jpg', 0)
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT) # 离散傅里叶变换
    dft_shift = np.fft.fftshift(dft) # 将图像中的低频部分移动到图像的中心
    # 傅里叶变换将图像转换成幅值谱 取对数的目的为了将数据变化到较小的范围（比如0-255）
    magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    # 转化成图片
    rows, cols = img.shape
    crow, ccol = rows / 2, cols / 2
    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[int(crow - 30):int(crow + 30), int(ccol - 30):int(ccol + 30)] = 1
    # apply mask and inverse DFT
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)  # 将图像中的低频部分移动到图像的中心
    img_back = cv.idft(f_ishift) # 将傅里叶信号转化成图片
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1]) # 将复数变化成实数
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


fourier_transform_numpy()
fourier_transform_opencv()
