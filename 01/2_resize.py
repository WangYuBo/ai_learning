import cv2

# 高斯模糊值
ksize = (15, 15)

sigma = 0
# 读取图片
img = cv2.imread("/media/wyb/work/github-local-resp/ai_learning/01/lena.jpg", 0)

g_img = cv2.GaussianBlur(img, ksize, sigma)


cv2.imshow('src_img', img)

cv2.imshow('g_img', g_img)

res_img = cv2.resize(img, (1000, 1000))

cv2.imshow('res_img', res_img)

cv2.waitKey(0)