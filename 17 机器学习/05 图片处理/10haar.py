import cv2
import numpy as np


fd = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\face.xml")
ed = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\eye.xml")
nd = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\nose.xml")

video_cap = cv2.VideoCapture(0)   # 0 视频捕捉设备的编号

while True:
    frame = video_cap.read()[1]   # 读取帧
    faces = fd.detectMutiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv2.ellipse(frame, (l+a, t+b), (a, b), 0, 0, 360, (255,0,255), 2)   # 画一个椭圆, 圆心, 长短轴, 旋转角度为0, 弧度0~360, 颜色, 线段
        face = frame[t:t+h, l:l+w]
        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv2.ellipse(face, (l+a, t+b), (a, b), 0, 0, 360, (0,0,255), 2)   # 画一个椭圆, 圆心, 长短轴, 旋转角度为0, 弧度0~360, 颜色, 线段
            noses = nd.detectMultiScale()
            for l, t, w, h in eyes:
                a, b = int(w / 2), int(h / 2)
                cv2.ellipse(face, (l+a, t+b), (a, b), 0, 0, 360, (255,0,0), 2)   # 画一个椭圆, 圆心, 长短轴, 旋转角度为0, 弧度0~360, 颜色, 线段
                cv2.imshow("VideoCapture", frame)
                if cv2.waitKey(timeout=33) == 27:   # ESC键的序号, 设置了超时, 每33毫秒捕获一帧
                    break

video_cap.release()   # 释放设备, 解除对设备的占用
cv2.destoryAllWindows()   # 关闭所有窗口, 以达到释放所有内存
