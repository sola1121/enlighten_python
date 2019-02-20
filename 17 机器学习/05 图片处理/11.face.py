import os
import cv2
import numpy as np
import sklearn.preprocessing as sp

# 级联器
fd = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\face.xml")
ed = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\eye.xml")
nd = cv2.CascadeClassifier("E:\\达内学习文件\\17 机器学习\\data\\haar\\nose.xml")

def search_face(directory):
    """遍历目录, 子目录, 包含文件"""
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory %s doesn't exist." % directory)
    objects = dict()
    for cur_dir, sub_dirs, files in os.walk(directory):   # 查询每一个目录, 当前目录, 子目录, 文件
        for jepg in (file for file in files if file.endswith("jpg")):   # 文件以jpg结尾的
            path = os.path.join(cur_dir, jepg)   # 得到一个完整的文件路径
            label = path.split(os.path.sep)[-2]   # 以路径的分隔符分割, 取其上级目录
            if label not in objects:
                objects[label] = list()
            objects[label].append(path)
    return objects


train_faces = search_face("E:\\达内学习文件\\17 机器学习\\data\\faces\\training")

codec = sp.LabelEncoder()
codec.fit(train_faces.keys())

train_x, train_y = list(), list()
for label, filenames in train_faces.items():
    for filename in filenames:
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = fd.detectMutiScale(gray, 1.1, 2, minSize=(100, 200))
        for l, t, w, h in faces:
            train_x.append(gray[t:t+h, l:l+w])
            train_y.append(codec.transform([label])[0])

train_y = np.array(train_y)

# 局部二值模式直方图人脸识别器
model = cv2.faceLBPHFaceRecognizer_create()

TODO: