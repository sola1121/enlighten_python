import numpy as np


raw_samples = np.array([
    [2, -6, 9, 2],
    [-1.9, 8, 5, 6.7],
    [0, 7, -3, -2, 4]
])

# 手动处理, 均值移除

print(raw_samples)
print(raw_samples.mean(axis=0))   # 样本平均值
print(raw_samples.std(axis=0))    # 样本标准差

std_samples = raw_samples.copy()

for col in std_samples.T:     # 处理列
    col_mean = col.mean()     # 每列的平均值
    col_std = col.std()       # 每列的标准差
    col -= col_mean           # 列各元素减去列均值
    col /= col_std            # 列个元素除以列标准差

print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))


# 使用sklearn做数据预处理, 均值移除

import sklearn.preprocessing as sp

std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
