import numpy as np
import cv2


original = cv2.imread("C:\\Users\\tarena\\Desktop\\table.jpg")
cv2.imshow("original", original)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)   # 转换为灰度图, 不可逆的变化
cv2.imshow("gray", gray)

sift = cv2.xfeatures2d.SIFT_create()   # 二维特征
keypoints = sift.detect(gray)   # 进行检测
mixture = original.copy()
cv2.drawKeypoints(original, keypoints, mixture, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # 画出特征点
cv2.imshow("mixture", mixture)

cv2.waitKey()