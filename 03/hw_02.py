# -*- coding:utf-8 -*-
import cv2
import numpy as np
# import matplotlib.pyplot as plt

# 卷积核大小
ksize = 3
# 读取图像
src = cv2.imread('./lena.jpg')

# Sobel处理图像
# src 表示 源图像;cv2.CV_64 64;

s_x = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize)

s_y = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize)

s_xy = cv2.Sobel(src, cv2.CV_64F, 1, 1, ksize)


cv2.imshow('sobel_x', s_x)
cv2.imshow('s_y', s_y)
cv2.imshow('s_xy', s_xy)

cv2.waitKey(0)
