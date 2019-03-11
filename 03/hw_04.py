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

# TODO 统计有米粒数量,长宽,面积等信息;
# 统计所有轮廓,统计,返回 contours 定義爲“vector<vector<Point>>contours”，是一個向量，
# 並且是一個二維向量，向量內每個元素保存了一組由連續的Point點構成的點的集合的向量，每一組Point點集就是一個輪廓。有多少輪廓，向量contours就有多少元素
con_img, conts, hcy = cv2.findContours(t_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow('con_img', con_img)
print '米粒数量', len(conts)

# 给所有米粒画出轮廓
# d_img = cv2.drawContours(con_img, conts, -1, (0, 0, 255))
# cv2.imshow('d_img', d_img)


ric = [] # 每个米粒的长度和面积
area_l = []  # 所有米粒的面积
arcl_l = []  # 所有米粒的周长

rec_img = [];
# 计算各米粒面积和周长
for c in conts:
    area = cv2.contourArea(c)  # 计算每个米粒面积
    l = cv2.arcLength(c, False)  # 计算每个完整的米粒周长
    if area < 10:  # 过小的可能是噪声，过滤之；
        continue
    ric.append([area, l])
    area_l.append(area)
    arcl_l.append(l)

    x, y, w, h = cv2.boundingRect(c)
    # 给每个米粒画上包围矩形
    cv2.rectangle(con_img, (x, y),  (x+w, y+h), (0, 255, 0))

    print '米粒面积 %s, 米粒周长 %s' % (area,l)

cv2.imshow('米粒识别', con_img)

# ric[] 第一个值是图形总面积,总周长,不计入均值统计
del ric[0]
del area_l[0]  # 删除第一个值,第一个值是大图形总面积,
del arcl_l[0]  # 同理

area_l.sort()
arcl_l.sort()

del area_l[len(arcl_l)-1]
del area_l[len(area_l)-1]


# 计算米粒面积和周长的均值
avg_area = np.mean(area_l)
avg_arcl = np.mean(arcl_l)


# 求米粒面积和周长方差area_l[0]
var_area = np.var(area_l)
var_arcl = np.var(arcl_l)

# 米粒标准差
std_area = np.std(area_l)
std_arcl = np.std(arcl_l)

print '米粒均长 %s, 面积 %s; \r 周长方差 %s, 面积方差 %s; \r 周长标准差 %s, 面积标准差 %s;' % \
      (avg_arcl, avg_area, var_arcl, var_area, std_arcl, std_area)


# TODO 计算在3sigma之间的米粒数量


cv2.waitKey(0)