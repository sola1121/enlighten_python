import os
import numpy as np

# 价格波动范围 = 最高的最高价 - 最低的最低价

highest_prices, lowest_prices = np.loadtxt(os.path.dirname(__file__) + "/aapl.csv", 
                       delimiter=",", usecols=(4, 5), unpack=True)

max_highest_price, min_lowest_price = highest_prices[0], lowest_prices[0]
for highest_price, lowest_price in zip(highest_prices, lowest_prices):
    if highest_price > max_highest_price:
        max_highest_price = highest_price
    if lowest_price < min_lowest_price:
        min_lowest_price = lowest_price
scope = max_highest_price - min_lowest_price
print("算法", scope)

scope = highest_prices.max() - lowest_prices.min()
print("numpy", scope)

high_spread = np.ptp(highest_prices)
print("高价极差", high_spread)

# plt.show()
