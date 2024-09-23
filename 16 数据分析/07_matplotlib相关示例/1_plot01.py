import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)   # 线性空间划分, 将-pi~pi之间划分1000份
cos_y = np.cos(x) / 2   # numpy的cos可以接收一个数组, 并也将结果返回数组
sin_y = np.sin(x)

plt.plot(x, cos_y)
plt.plot(x, sin_y)
plt.show()
