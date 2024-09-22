import os
import datetime as dt
import numpy as np

def dmy2days(dmy):
    dmy = str(dmy, encoding="U8")
    date = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    days = (date - dt.date.min).days   # 计算出天数
    return days

twap, tsum = 0, 0

days, closing_prices = np.loadtxt(os.path.dirname(__file__) + "/aapl.csv", 
                       delimiter=",", usecols=(1, 6), unpack=True, converters={1: dmy2days})


for day, closing_price in zip(days, closing_prices):
    twap += closing_price * day
    tsum += day
twap /= tsum
print("算法:", twap, end=",  ")

twap = np.average(closing_prices, weights=days)
print("numpy:", twap)

# plt.show()
