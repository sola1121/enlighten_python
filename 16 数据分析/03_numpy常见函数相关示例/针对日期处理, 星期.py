import os
import datetime as dt
import numpy as np

# 获取对应星期的数据值

def dmy2wday(dmy):
    dmy = str(dmy, encoding="U8")
    date = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    wday = date.weekday()   # datetime对象中提取星期, 将使用0~6依次表示星期 
    return wday


wdays, closing_prices = np.loadtxt(os.path.dirname(__file__) + "/aapl.csv", 
                       delimiter=",", usecols=(1, 6), unpack=True, converters={1: dmy2wday})

ave_closing_prices = np.zeros(5)

for wday in range(ave_closing_prices.size):
    # ave_closing_prices[wday] = closing_prices[wdays == wday].mean()   # 使用掩码的方式
    ave_closing_prices[wday] = closing_prices[np.where(wdays == wday)].mean()

for wday, ave_closing_prices in zip(["Mon", "Tue", "Wed", "Thu", "Fri"], ave_closing_prices):
    print(wday, np.round(ave_closing_prices, 2))
