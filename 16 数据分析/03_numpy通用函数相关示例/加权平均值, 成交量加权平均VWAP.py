import numpy as np
import matplotlib.pyplot as plt

closing_prices, volumes = np.loadtxt("E:/达内学习文件/16 数据分析/03_numpy通用函数相关示例/aapl.csv", 
                          delimiter=",", usecols=(6, 7), unpack=True)

vwap, vsum = 0, 0

for closing_price , volume in zip(closing_prices, volumes):
    vwap += closing_price * volume
    vsum += volume
vwap /= vsum
print("算法:", vwap, end=",  ")

vwap = np.average(closing_prices, weights=volumes)
print("numpy:", vwap)

# plt.show()
