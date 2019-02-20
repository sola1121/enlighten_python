import numpy as np


raw_samples = np.array([
    [1, 3, 2],
    [7, 5, 4],
    [1, 8, 6],
    [7, 3, 9]])

print(raw_samples)

code_tables = list()
for col in raw_samples.T:           # 处理每列
    code_table = dict()
    for val in col:                 # 处理每列值 
        code_table[val] = None
    code_tables.append(code_table)

for code_table in code_tables:
    size = len(code_table)
    for one, key in enumerate(sorted(code_table.keys())):
        code_table[key] = np.zeros(shape=size, dtype=int)
        code_table[key][one] = 1

ohe_samples = list()
for raw_sample in raw_samples:
    ohe_sample = np.array([], dtype=int)
    for i, key in enumerate(raw_sample):
        ohe_sample = np.hstack( (ohe_sample, code_tables[i][key]) )
        ohe_samples.append(ohe_sample)

print(np.array(ohe_samples))



# 使用sklearn, 独热编码

import sklearn.preprocessing as sp

one_hot_encoder = sp.OneHotEncoder(sparse=False, dtype=int)
ohe_samples = one_hot_encoder.fit_transform(raw_samples)
print(ohe_samples)
