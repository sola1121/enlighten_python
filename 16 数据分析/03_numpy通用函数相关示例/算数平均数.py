import numpy as np
import matplotlib.pyplot as plt

closing_prices = np.loadtxt("E:/达内学习文件/16 数据分析/03_numpy通用函数相关示例/aapl.csv", delimiter=",", usecols=(6), unpack=True)

mean = 0
for closing_prices in closing_prices:
    mean += closing_prices

mean /= closing_prices.size
print("算法:", mean, end=",  ")   

mean = np.mean(closing_prices)
print("numpy:", mean)

# plt.show()
