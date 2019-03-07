# -*- coding:utf-8 -*-
import cv2
import numpy as np

"""
作业总结:
卷积核为(3,3),中值为3时,观察lena睫毛及眼睛,图形形态学先开后闭,图形图像学最清晰,中值比高斯清晰,均值最模糊.
"""

# 卷积核大小
ksize = (3, 3)

# 读取原始图像
src = cv2.imread('./lena.jpg')

# 使用平均滤波处理图像
b_img = cv2.blur(src, ksize)

cv2.imshow('平均滤波', b_img)


# 使用中值滤波处理图像

m_img = cv2.medianBlur(src, 3, 0)

cv2.imshow('中值滤波处理图', m_img)


# 使用高斯平滑滤波处理图像
g_img = cv2.GaussianBlur(src, ksize, sigmaX=0, sigmaY=0)

cv2.imshow('高斯滤波处理的图像', g_img)


# 使用图像图形学处理
a_img = cv2.morphologyEx(src, cv2.MORPH_OPEN, ksize, 1)
b_img = cv2.morphologyEx(a_img, cv2.MORPH_CLOSE, ksize, 1)

cv2.imshow('图形形态学-open', b_img)
cv2.imshow('图形形态学-open&clos ', b_img)

cv2.waitKey(0)


