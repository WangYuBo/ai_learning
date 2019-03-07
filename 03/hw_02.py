# -*- coding:utf-8 -*-
"""
tuxiang jiance fangfa
"""

import cv2
import numpy as np
# import matplotlib.pyplot as plt

# 卷积核大小
ksize = 5
# 读取图像
img = cv2.imread('./lena.jpg')

# 灰度处理图像
src = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# Sobel处理图像
# src 表示 源图像;cv2.CV_64 64;

s_x = cv2.Sobel(src, cv2.CV_64F, 1, 0, ksize)

#参数0,1为只在y方向求一阶导数，最大可以求2阶导数,卷积核5*5
#对y滤波就显示x波形
s_y = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize)

s_xy = cv2.Sobel(src, cv2.CV_64F, 1, 1, ksize)


cv2.imshow('sobel_x', s_x)
cv2.imshow('s_y', s_y)
cv2.imshow('s_xy', s_xy)


# 使用lapalace算子检测图像边缘
# #cv2.CV_64F 输出图像的深度（数据类型），可以使用-1与源图像保持一致
l = cv2.Laplacian(src, cv2.CV_64F)

cv2.imshow('lapalace', l)


# 使用canny检测图像边缘;
#
c1 = cv2.Canny(src, 190, 200, False)

c2 = cv2.Canny(src, 100, 200, True)

cv2.imshow('Canny 01', c1)
cv2.imshow('canny 02', c2)

cv2.waitKey(0)


