#-*- coding:utf-8 -*-
import cv2
import sys

# 检查是否有指定输入影像
#if(len(sys.argv) != 2):
#   print "usage: " + sys.argv[0] + "<Image_Path>"
#    sys.exit(-1);

# 读取图片
#img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
img = cv2.imread("./lena.jpg")
# 建立窗口
cv2.namedWindow("Display Image ", cv2.WINDOW_AUTOSIZE);

# 用窗口显示图像
cv2.imshow('Display Image', img)

#显示窗口,直到有任何新键盘输入后离开.
cv2.waitKey(0)





