import numpy as np


raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])

# 手动, 二值化
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 1.4] = 0
bin_samples[bin_samples > 1.4] = 1
print(bin_samples)


# 使用skleran, 二值化器

import sklearn.preprocessing as sp

binarizer =  sp.Binarizer(threshold=1.4)
bin_samples = binarizer.transform(raw_samples)
print(bin_samples)