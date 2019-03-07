# -*- coding:utf-8 -*-
"""
使用米粒图像，分割得到各米粒，首先计算各区域(米粒)的面积、长度等信息，
进一步计算面积、长度的均值及方差，分析落在3sigma范围内米粒的数量
"""

import cv2
import numpy as np

from matplotlib import pyplot as plt

ksize = (3, 3)

# 读取图片
src = cv2.imread('./rice.jpg')

# 查看图像,发现有很多噪点
cv2.imshow('origin img', src)

# 复制图像
img = src.copy()

# 先做灰度处理
gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# 先用高斯滤波,得到清晰图像(danjieguobingbulixiang)
gs_img = cv2.GaussianBlur(img, ksize, sigmaX=0, sigmaY=0)


#
cv2.imshow('gaussian blur', gs_img)

# sobel

# s_img = cv2.Sobel(gs_img,cv2.CV_64F, 0, 1, ksize)

# cv2.imshow('Sobel img', s_img)

# canny
# https://blog.csdn.net/on2way/article/details/46812121
c_img = cv2.Canny(gs_img, 100, 300, True)
cv2.imshow('g-img', gs_img)
cv2.imshow('c-img', c_img) # canny suanfa

# 再用大津算法分割图像
retVal, t_img = cv2.threshold(c_img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('t_img', t_img)

# 统计有米粒数量,长宽,面积等信息;


# 计算在3sigma之间的米粒数量


cv2.waitKey(0)