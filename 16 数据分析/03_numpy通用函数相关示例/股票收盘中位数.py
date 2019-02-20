import os
import numpy as np


closing_prices = np.loadtxt(os.path.dirname(__file__) + "/aapl.csv", 
                       delimiter=",", usecols=(6), unpack=True)

sorted_prices = np.msort(closing_prices)   # 排序
l = sorted_prices.size
median = (sorted_prices[int((l-1)/2)] + sorted_prices[int(l/2)]) / 2
print("算法", median)

median = np.median(closing_prices)
print("numpy", median)
