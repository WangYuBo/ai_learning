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
src = cv2.imread('./rice.png')

# 查看图像,发现有很多噪点
# cv2.imshow('原图', src)

# 复制图像
img = src.copy()

# 先做灰度处理
gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)


#  图形形态学 去噪 效果不错
# 
gs_img = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, (5, 5))
# gs_img = cv2.morphologyEx(gray_img, cv2.MORPH_CLOSE, (5, 5))

# 先用高斯滤波,得到清晰图像(jieguobingbulixiang)
# gs_img = cv2.GaussianBlur(img, ksize, 0)

# 大津算法分割图像
ret, t_img = cv2.threshold(gs_img, 10, 255, cv2.THRESH_OTSU)

# cv2.imshow('高斯滤波处理图', gs_img)

# sobel

# s_img = cv2.Sobel(gs_img,cv2.CV_64F, 0, 1, ksize)

# cv2.imshow('Sobel img', s_img)

#  canny 这个参数范围内表现不错，
# https://blog.csdn.net/on2way/article/details/46812121
c_img = cv2.Canny(gs_img, 100, 300, True)


# cv2.imshow('canny边缘检测后图', c_img)

# 再用大津算法分割图像，测试阈值范围：(0,50)（10,250），（10,200），（10,150），（10,100），（10,50）；（50,250），（50,200），
# ret, t_img = cv2.threshold(c_img, 10, 300, cv2.THRESH_OTSU)

# 使用自适应阈值分割，效果也不好，同大津算法；自适应阈中，参数thrshhodtype 只能是THRESH_BINARY或THRESH_BINARY_INV,否则报找不到类型错误
# t_img = cv2.adaptiveThreshold(c_img, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)

# 统计米粒数量,长宽,面积等信息;
# 统计所有轮廓,统计,返回 contours 定義爲“vector<vector<Point>>contours”，是一個向量，
# 並且是一個二維向量，向量內每個元素保存了一組由連續的Point點構成的點的集合的向量，每一組Point點集就是一個輪廓。有多少輪廓，向量contours就有多少元素
con_img, conts, hcy = cv2.findContours(t_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


ric = [] # 每个米粒的长度和面积
area_l = []  # 所有米粒的面积
arcl_l = []  # 所有米粒的周长

rec_img = []

# 计算各米粒面积和周长,并给米粒圈方框
for c in conts:
    area = cv2.contourArea(c)  # 计算每个米粒面积
    l = cv2.arcLength(c, True)  # 计算每个完整的米粒周长
    if area < 10:  # 过小的可能是噪声，过滤之；
        continue
    ric.append([area, l])
    area_l.append(area)
    arcl_l.append(l)


    """
    传入图像轮廓，xy是左上角的点，wh是矩形边框宽度高度
    """
    x, y, w, h = cv2.boundingRect(c)
    # 给每个米粒画上包围矩形
    cv2.rectangle(img, (x, y),  (x+w, y+h), (0, 0, 255))

    # 获得最小的矩形轮廓，可能带旋转角度
    rect = cv2.minAreaRect(c)

    # 计算最小区域坐标
    box = cv2.boxPoints(rect)

    # 坐标规范化为整数
    box = np.int0(box)

    # 画出轮廓
    cv2.drawContours(img, [box], 0, (0, 0, 255), 1)

    print '米粒面积 %s, 米粒周长 %s' % (area,l)


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
are_std_list = [] # 用来存储符合三个标准差之间的米粒的面积
for ar in area_l:
    if ar < (avg_area - 3*std_area) or ar > (avg_area + 3*std_area):
        continue

    are_std_list.append(ar)

# 在3sigma之间米粒数量为：
# print '在3sigma之间米粒数量为：%s' % len(are_std_list)

# 用matlib显示图像
imgs = [src, gs_img, c_img, t_img, img] # 用来存储每个步骤处理过后的图片
# titles = ['原图', '高斯模糊', 'Canny边缘检测', '大津分割', '识别处理并加框'] # 每个图片对应标题
titles = ['orgin_img', 'noise elimination', 'canny', 'ostu', 'rectangle']

for i in range(len(imgs)):
    plt.subplot(2, 3, i+1), plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# TODO str = '在3sigma之间米粒数量为：%s' % len(are_std_list)
# plt.text(3, 10, '在3sigma之间米粒数量为：85', size = 10, rotation(30), ha='bottom', )
plt.show()


cv2.waitKey(0)