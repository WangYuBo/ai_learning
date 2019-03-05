import  cv2
import math

# 读取图片
img = cv2.imread("./lena.jpg")



# 显示图片
cv2.imshow('lena img ', img)

cv2.waitKey(0)