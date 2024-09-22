import os
import numpy as np


closing_prices = np.loadtxt(os.path.dirname(__file__) + "/aapl.csv", 
                       delimiter=",", usecols=(6), unpack=True)

mean = np.mean(closing_prices)   # 平均值
devs = closing_prices - mean
variable = (devs**2).mean()
std_dev = np.sqrt(variable) 
print("算法", std_dev)

std_dev = np.std(closing_prices)
print("numpy", std_dev)

