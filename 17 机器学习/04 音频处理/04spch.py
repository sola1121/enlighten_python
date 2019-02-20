import os
import warnings
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as spfea
import hmmlearn.hmm as hl

# 设置忽略警告
warnings.filterwarnings("ignore", category=UserWarning)
np.seterr(all="ignore")


def search_speeches(directory, speeches):
    """递归的找指定后缀文件"""
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory '{}' doesn't exist!".format(directory))
    for entry in os.listdir(directory):
        label = directory[directory.rfind(os.path.sep)+1:]
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            search_speeches(path, speeches)
        elif os.path.isfile(path) and path.endswith(".wav"):
            if label not in speeches:
                speeches[label] = list()
            speeches[label].append(path)


train_speeches = dict()
# 获取文件
search_speeches(os.path.dirname(__file__) + "/speeches", train_speeches)
# print(train_speeches)

train_x = list()
train_y = list()

for label, filenames in train_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = spfea.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)

    train_x.append(mfccs)
    train_y.append(label)


# TODO:
models = dict()
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4, covariance_type="diag", n_iter=1000)   # 高斯分布, 即正态分布
    models[label] = model.fit(mfccs)
