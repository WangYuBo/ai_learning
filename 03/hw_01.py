# -*- coding:utf-8 -*-
import cv2
import numpy as np

# 卷积核大小
ksize = (9, 9)

# 读取原始图像
src = cv2.imread('./lena.jpg')

# 使用平均滤波处理图像
b_img = cv2.blur(src, ksize)

cv2.imshow('平均滤波', b_img)

# 使用高斯平滑滤波处理图像
g_img = cv2.GaussianBlur(src, ksize, sigmaX=0, sigmaY=0)

cv2.imshow('高斯滤波处理的图像', g_img)


# 使用中值滤波处理图像

m_img = cv2.medianBlur(src, 15, 0)

cv2.imshow('中值滤波处理图', m_img)




cv2.waitKey(0)
