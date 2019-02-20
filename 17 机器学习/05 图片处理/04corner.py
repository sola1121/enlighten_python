import numpy as np
import cv2


original = cv2.imread("C:\\Users\\tarena\\Desktop\\box.png")
cv2.imshow("original", original)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)   # 转换为灰度图, 不可逆的变化
cv2.imshow("gray", gray)

corners = cv2.cornerHarris(gray, 7, 5, .04)   # 获取角点
corners = cv2.dilate(corners, None)   # 锐化
mixture = original.copy()
mixture[corners > corners.max()* .01] = [0, 0, 255]  # 找出角点corners中大于其最大值的原图上的点
cv2.imshow("mixture", mixture)


cv2.waitKey()