# -*- coding:utf-8 -*-
"""
本部分为学习角点检测，
练习并对比Harris、SIFT、ORB三种角点检测方法；

"""

import cv2
from matplotlib import pyplot as plt

# 读取图片
src = cv2.imread('./blox.jpg')

img = src.copy()

# 转化为灰度图片
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

"""
Harris算法：
参数一：mat类图像，且单通道8位或浮点型；
参数二：blocksize,邻域大小；更多的详细信息在cornerEigenValsAndVecs中有讲到
参数三：ksize,Sobel算子卷积核大小；
参数四：k,harris参数，在0.02~0.04之间均可；原因不详；

"""
h_dst = cv2.cornerHarris(gray, 3, 3, 0.04)

""""
dst>0.01*dst.max()这么多返回是满足条件的dst索引值，根据索引值来设置这个点的颜色；
这里是设定0.01*h_dst.max()为阀值，只要大于的，都是角点；
的dst其实就是一个个角度分数R组成的
当 λ 1 和 λ 2 都很大，并且 λ 1 ～λ 2 中的时，R 也很大，
（λ 1 和 λ 2 中的最小值都大于阈值）说明这个区域是角点。
那么这里为什么要大于０．０１×ｄｓｔ.max()呢？
注意了这里Ｒ是一个很大的值　
我们选取里面最大的Ｒ　
然后，只要dst里面的值大于百分之一的Ｒ的最大值
那么此时这个dst的Ｒ值也是很大的　可以判定他为角点
也不一定要０．０１
可以根据图像自己选取不过如果太小的话　可能会多圈出几个不同的角点
src:https://www.cnblogs.com/DOMLX/p/8763369.html
"""
img[h_dst > 0.01*h_dst.max()] = [0, 0, 255]



"""
SIFT算法
1. 直接灰度图上处理，sift算法检测到很多角点，其中包括非角点误检，噪音误检；
harris算法检测误检较少；
但两者正确检测的数量相差不多；

2. 猜测：去除噪点后，sift噪音误检率会下降；
实际：高斯&形态学去噪后，在处理效果一样差；
"""
s_img = img.copy()

# 高斯去噪 效果不好
#s_img = cv2.GaussianBlur(s_img, (3, 3), 0)

# 图像形态学去噪，
s_img = cv2.morphologyEx(s_img, cv2.MORPH_OPEN, (5, 5))

# 这个是静态方法；
sift = cv2.xfeatures2d.SIFT_create()

# 检测角点
kp = sift.detect(s_img, None)

# 画出角点
s_img = cv2.drawKeypoints(s_img, kp, s_img)


""""
ORB算法
"""
o_img = src.copy()

orb = cv2.ORB_create()

kp_orb = orb.detect(img)

kp_orb, des = orb.compute(o_img,kp_orb)

o_img = cv2.drawKeypoints(o_img, kp_orb, o_img, color=(0, 255, 0), flags=0)


# 展示的图片标题
img_names = ['origin', 'harris_img', 'SIFT', 'ORB_img']
imgs = [src, img, s_img, o_img]

for i in range(len(imgs)):
    plt.subplot(2, 3, i+1), plt.imshow(imgs[i], 'gray')
    plt.title(img_names[i])
    plt.xticks([]), plt.yticks([])

plt.show()