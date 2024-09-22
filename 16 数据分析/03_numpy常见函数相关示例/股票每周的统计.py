import os
import datetime as dt
import numpy as np


def  dmy2wday(dmy):
    dmy = str(dmy, encoding="U8")
    date = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    wday = date.weekday()
    return wday

wdays, opening_prices, highest_prices, lowest_prices, closing_prices = np.loadtxt(
os.path.dirname(__file__) + "/aapl.csv", delimiter=",", usecols=(1, 3, 4, 5, 6), unpack=True, converters={1: dmy2wday})

# 取15天的数据
wdays = wdays[:16]
opening_prices = opening_prices[:16]
highest_prices = highest_prices[:16]
lowest_prices = lowest_prices[:16]
closing_prices = closing_prices[:16]

# 第一个周一
first_monday = np.where(wdays == 0)[0][0]

# 最后一个周五
last_friday = np.where(wdays == 4)[0][-1]

indices = np.array(first_monday, last_friday + 1)
print(indices)

# 将所获得的15天均分为三份, 这样就可以表示每个星期了
indices = np.split(indices, 3)

def week_summary(indices):
    opening_price = opening_prices[indices[0]]
    highest_price = np.max(np.take(highest_prices, indices))
    lowest_price = np.min(np.take(lowest_prices, indices))
    closing_price = closing_prices[indices[-1]]
    return opening_price, highest_price, lowest_price, closing_price

summaries = np.apply_along_axis(week_summary, 1, indices)
print(summaries)

