import os
import warnings
import cv2
import numpy as np
import hmmlearn.hmm as hl


# warnings.filterwarnings("ignore", category="DeprecationWarning")
# .setter(all="ignore")

def search_objects(directory):
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


train_objects = search_objects("E:\\达内学习文件\\17 机器学习\\data\\objects\\training")

train_x, train_y = list(), list()

for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # 转为灰度图
    # 统一图片大小
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        gray = cv2.resize(gray, None, fx=f, fy=f)
    # star 特征
        star = cv2.xfeatures2d.StarDetector_create()
        keypoints = star.detect(gray)
        sift = cv2.xfeatures2d.SIFT_create()
        _, desc = sift.compute(gray, keypoints)   # 获得特征矩阵
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    train_x.append(descs)
    train_y.append(label)

# 训练模型
models = dict()
for descs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_componets=4, covariance_type="diag", n_iter=1000)
    models[label] = model.fit(descs)


# 开始测试

test_objects = search_objects("E:\\达内学习文件\\17 机器学习\\data\\objects\\testing")

test_x, test_y, test_z = list(), list(), list()

for label, filenames in train_objects.items():
    test_z.append([])
    descs = np.array([])
    for filename in filenames:
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # 转为灰度图
    # 统一图片大小
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        gray = cv2.resize(gray, None, fx=f, fy=f)
    # star 特征
        star = cv2.xfeatures2d.StarDetector_create()
        keypoints = star.detect(gray)
        sift = cv2.xfeatures2d.SIFT_create()
        _, desc = sift.compute(gray, keypoints)   # 获得特征矩阵
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    test_x.append(descs)
    test_y.append(label)

# 进行测试
pred_test_y = list()
for descs in test_x:
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(descs)
        if (best_score is None) or (best_score < score):
            best_score, best_label = score, label
    
    pred_test_y.append(best_label)

i = 0
for label, pred_label, images in zip(test_y, pred_test_y, test_z):
    for image in images:
        i += 1
        cv2.imshow("{} - {} {} {}".format(i, label, "==" if label == pred_label else "!=", pred_label, image))