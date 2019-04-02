# -*- coding:utf-8 -*-

"""
1. 在测试视频(OpenCV安装目录\sources\samples\data)上，使用基于混合高斯模型的背景提取算法，提取前景并显示(显示二值化图像，前景为白色)。
2. 在1基础上，将前景目标进行分割，进一步使用不同颜色矩形框标记，并在命令行窗口中输出每个矩形框的位置和大小。
3. 安装ImageWatch，并在代码中通过设置断点，观察处理中间结果图像。
4. 使用光流估计方法，在前述测试视频上计算特征点，进一步进行特征点光流估计。

"""
import cv2
import numpy as nup
from matplotlib import pyplot as plt


"""
实现步骤：
"""
# 第一步：读取视频
cap = cv2.VideoCapture('vtest.avi')


# 打开视频
#cap.open('./vtest.avi')

print(cap.isOpened())

# 第二步：设定卷积核为3*3
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# 第三步：创建背景分割对象，构建高斯混合模型
mog = cv2.createBackgroundSubtractorMOG2()

while(True):
    # 第四步：读取视频中图片，并使用高斯模型拟合
    ret, frame = cap.read()

    # 使用高斯模型拟合，背景分割器，计算前景掩码
    fgmk = mog.apply(frame)

    # 第五步： 二值化处理，
    th = cv2.threshold(fgmk, 40, 255, cv2.THRESH_BINARY)[1]

    # 第六步：计算图像轮廓
    con_img, conts, hcy = cv2.findContours(fgmk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in conts:
        # 第v七步：判断前景轮廓，画出外接矩阵方格；
        #length = cv2.arcLength(c, True)
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

        cv2.imshow('fgmk', fgmk)
        cv2.imshow('frame', frame)

    # 按Q健退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# 释放窗口资源
cap.release()
cv2.destroyAllWindows()

# TODO 使用LK金字塔算法,并与普通LK算法比较 ;