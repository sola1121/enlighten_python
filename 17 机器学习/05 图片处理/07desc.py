import cv2
import numpy as np
import matplotlib.pyplot as plt

original = cv2.imread("C:\\Users\\tarena\\Desktop\\table.jpg")
cv2.imshow("original", original)

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)   # 转换为灰度图, 不可逆的变化
cv2.imshow("gray", gray)

star = cv2.xfeatures2d.StarDetector_create()   # 二维特征
keypoints = star.detect(gray)   # 其中特征点
mixture = original.copy()
cv2.drawKeypoints(original, keypoints, mixture, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)   # 绘制star特征点

sift = cv2.xfeatures2d.SIFT_create()
keypoints, desc = sift.compute(gray, keypoints)   # 计算特征点, 生成描述矩阵
print("keypoints类型", type(keypoints))
print("生成的描述矩阵形状", desc.shape)
cv2.imshow("mixture", mixture)

plt.matshow(desc, cmap="jet", fignum="Description")
plt.title("Description")
plt.xlabel("Feature", fontsize=12)
plt.ylabel("sample", fontsize=12)
plt.tick_params(which="both", top=False, labeltop=False, labelbottom=True, labelsize=10)
plt.show()


cv2.waitKey()