# -*- coding:utf-8 -*-
"""
灰度直方图/大津算法;

从大津算法五种结果看,效果都不是很让人满意,都分割的不清晰;
to_zero_inv把人物分割出了立体感.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
src = cv2.imread('./lena.jpg')
# 灰度处理
img = cv2.cvtColor(src, cv2.COLOR_BGRA2GRAY)
# 灰度直方图

color = ('b', 'g', 'r')
for i,col in enumerate(color):
    histr = cv2.calcHist([src], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()

# 大津算法
ret, t1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, t2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, t3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, t4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, t5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['orgin', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']

imgs = [img, t1, t2, t3, t4, t5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


# 区域生长算法
def fill_color_demo(img):
    copyImg  = src.copy() # 复制出原图副本
    h, w = img.shape[:2]  # 读取图像宽高
    mask = np.zeros([h + 2, w + 2], np.uint8)  # 新建图像矩阵
    cv2.floodFill(img, mask, (5, 5), (0, 0, 255), (255, 255, 255), (5, 5, 5), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow("fill_color", copyImg)


fill_color_demo(img)
cv2.waitKey(0)



