import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdt

def dmy2ymd(dmy):
    """
    日期格式转换预处理器
    日月年 -> 年月日
    """
    dmy = str(dmy, encoding="utf-8")
    date = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    ymd = date.strftime("%Y-%m-%d")
    return ymd

dates, opening_prices, highest_prices, lowest_prices, closing_prices = \
np.loadtxt("E:/达内学习文件/16 数据分析/03_numpy通用函数相关示例/aapl.csv", 
delimiter=",", usecols=(1,3,4,5,6), unpack=True, dtype="M8[D], f8, f8, f8, f8", converters={1: dmy2ymd})

# print(dates)

plt.figure("Candlestick", facecolor="lightgray")
plt.title("Candlestick", fontsize=14)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price", fontsize=12)

plt.tick_params(labelsize=10)
plt.grid(linestyle=":")

# TODO: 干点啥

dates = dates.astype(mdt.datetime.datetime)

rise = closing_prices - opening_prices >= .01
fall = opening_prices - closing_prices >= .01

fc = np.zeros(dates.size, dtype="3f4")   # 每个元素都是由3个float32组成
ec = np.zeros(dates.size, dtype="3f4")

fc[rise], fc[fall] = (1, 1, 1), (0, .5, 0)   # 设置涨与跌的颜色
ec[rise], ec[fall] = (1, 0, 0), (0, .5, 0)

plt.bar(dates, highest_prices - lowest_prices, 0, lowest_prices, color=fc, edgecolor=ec)
plt.bar(dates, closing_prices - opening_prices, .8, opening_prices, color=fc, edgecolor=ec)

plt.gcf().auto_xdate()   # 美化x轴日期, 加斜

plt.show()
