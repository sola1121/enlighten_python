import os
import numpy as np
import cv2

im_dir = os.path.dirname(__file__) + "/study.jpg"
print(im_dir)

original = cv2.imread(os.path.dirname(__file__) + "/study.jpg")
print(original.shape)
cv2.imshow("Original", original)

# 只看蓝色
blue = np.zeros_like(original)   # 取形状与original一样的0数组
blue[..., 0] = original[..., 0]   # 0 蓝色通道
cv2.imshow("blue", blue)

# 只看绿色
green = np.zeros_like(original)   # 取形状与original一样的0数组
green[..., 1] = original[..., 1]   # 1 绿色通道
cv2.imshow("green", green)

# 只看红色
red = np.zeros_like(original)   # 取形状与original一样的0数组
red[..., 2] = original[..., 2]   # 2 红色通道
cv2.imshow("red", red)


# 通过对数组进行切片, 裁剪图片
# h, w = original.shape[:2]
# l, t = int(w)



cv2.waitKey()   # 等待键盘事件
