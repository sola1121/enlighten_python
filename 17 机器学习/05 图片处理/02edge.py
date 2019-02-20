import numpy as np
import cv2


original = cv2.imread("C:\\Users\\tarena\\Desktop\\study.jpg")
cv2.imshow("original", original)

canny = cv2.Canny(original, 50, 50)

cv2.imshow("canny", canny)

cv2.waitKey()