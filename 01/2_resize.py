# -*- coding:utf-8 -*-
import cv2

# 高斯模糊值
ksize = (15, 15)

sigma = 0
# 读取图片
img = cv2.imread("/media/wyb/work/github-local-resp/ai_learning/01/lena.jpg", 0)
# 显示原图
cv2.imshow('src_img', img)

# 对图片进行高斯平滑转换
g_img = cv2.GaussianBlur(img, ksize, sigma)
# 显示高斯过后图
cv2.imshow('g_img', g_img)


# 获取图像宽和高
h, w = img.shape[:2]

# 修改图长和宽为原图一半,并显示;
res_img = cv2.resize(img, (w/2, h/2))
cv2.imshow('res_img', res_img)


cv2.waitKey(0)