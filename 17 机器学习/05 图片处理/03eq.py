import numpy as np
import cv2


original = cv2.imread("C:\\Users\\tarena\\Desktop\\sunrise.jpg")
cv2.imshow("original", original)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)   # 转换为灰度图, 不可逆的变化
cv2.imshow("gray", gray)

equlized_gray = cv2.equalizeHist(gray)   # 均衡化灰度图, 可以调亮图片
cv2.imshow("equlize_gray", equlized_gray)

yuv = cv2.cvtColor(original, cv2.COLOR_BGR2YUV)   # yuv调整, 使用亮度, 饱和度, 色度来改变颜色
cv2.imshow("yuv", yuv)

yuv[..., 0] = cv2.equalizeHist(yuv[..., 0])   # 均衡化的方式增加亮度
equalized_color = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)   # 在次转换为BGR图
cv2.imshow("equlized_color", equalized_color)

cv2.waitKey()