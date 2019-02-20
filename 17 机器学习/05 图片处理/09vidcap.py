import cv2
import numpy as np


video_cap = cv2.VideoCapture(0)   # 0 视频捕捉设备的编号

while True:
    frame = video_cap.read()[1]   # 读取帧
    cv2.imshow("VideoCapture", frame)
    if cv2.waitKey(timeout=33) == 27:   # ESC键的序号, 设置了超时, 每33毫秒捕获一帧
        break

video_cap.release()   # 释放设备, 解除对设备的占用
cv2.destoryAllWindows()   # 关闭所有窗口, 以达到释放所有内存
