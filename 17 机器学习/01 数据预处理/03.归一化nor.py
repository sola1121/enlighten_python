import numpy as np


raw_samples = np.array([
    [2, -6, 9, 2],
    [-1.9, 8, 5, 6.7],
    [0, 7, -3, -2]])


# 手动计算, 归一
nor_samples = raw_samples.copy()
for row in nor_samples:
    row_absum = abs(row).sum()
    row /= row_absum
print(nor_samples)


# 使用sklearn

import sklearn.preprocessing as sp

nor_samples = sp.normalize(raw_samples, norm="l1")
print(nor_samples)
