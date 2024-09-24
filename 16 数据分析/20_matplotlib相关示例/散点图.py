import numpy as np
import matplotlib.pyplot as plt


n = 1000
x = np.random.normal(0, 1, n)   # n个符合标准正太的随机数
y = np.random.normal(0, 1, n)   # n个符合标准正太的随机数

distance = np.sqrt(pow(x, 2) + pow(y, 2))   # 与原点的距离

plt.figure("Scatter", facecolor="lightgray")
plt.title("Scatter", fontsize=20)

plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.scatter(x, y, s=60, c=distance, cmap="jet_r", alpha=.5, marker="*")

plt.show()