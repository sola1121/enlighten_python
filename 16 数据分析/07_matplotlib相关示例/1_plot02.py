import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)   # 线性空间划分, 将-pi~pi之间划分1000份
cos_y = np.cos(x) / 2   # numpy的cos可以接收一个数组, 并也将结果返回数组
sin_y = np.sin(x)

# 填满轴
plt.xlim(x.min(), x.max())   # 取x轴的左右边界为x取值的最小最大值
plt.ylim(sin_y.min(), sin_y.max())   # 取y轴的上下边界为sin_y值的最大最小

plt.plot(x, cos_y, linestyle="--", linewidth=2.0, color="#66ccff")
plt.plot(x, sin_y, linestyle=":",  linewidth=2.0, color="r")
plt.show()
