import numpy as np


raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])

# 手动处理, 范围缩放
mms_samples = raw_samples.copy()

for col in mms_samples.T:   # 处理列
    col_min = col.min()     # 每列中最小值
    col_max = col.max()     # 每列中最大值
    arr = np.array([        # 每列中最大值最小值构成的array
        [col_min, 1],
        [col_max, 1]])
    tmp = np.array([0, 1])
    x = np.linalg.lstsq(arr, tmp)[0]
    col *= x[0]
    col += x[1]

print(mms_samples)


# 使用sklearn

import sklearn.preprocessing as sp

mms = sp.MinMaxScaler(feature_range=(0, 1))
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)