# -*- coding:utf-8 -*-
import cv2
import numpy as np
# 读取图片
src = cv2.imread('./hw_03.png')

img = cv2.resize(src, (300, 300))
# 显示原图
cv2.imshow('src', img)

# 把图像转换为HSV,并显示
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

b = cv2.split(hsv)

# 显示纯色
cv2.imshow('hue', b[0])

#显示曝光度色
cv2.imshow('satutration', b[1])

# 只显示明亮度
cv2.imshow('value', b[2])

# 给图像做分离,分离成GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('COLOR_BGR2GRAY', gray)

a = cv2.split(gray)

cv2.imshow('gray', a[0]) # 此处a只有一个值a[0]


cv2.waitKey(0)

