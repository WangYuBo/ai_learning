# -*- coding:utf-8 -*-
import cv2
import numpy as np
# 读取图片
img = cv2.imread('./lena.jpg')

# cv2.imshow('src', img)

# 给图像做分离,分离成GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('COLOR_BGR2GRAY', gray)

a = cv2.split(gray)

cv2.imshow('blue', a[0])

cv2.waitKey(0)


# 把图像转换为HSV,并显示
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

b = cv2.split(hsv)

# 显示纯色
cv2.imshow('hue', b[0])

#显示曝光度色
cv2.imshow('satutration', b[1])

# 只显示明亮度
cv2.imshow('value', b[2])

cv2.waitKey(0)

