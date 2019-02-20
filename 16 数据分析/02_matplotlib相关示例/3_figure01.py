import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

plt.figure("Figure Object 1", figsize=(5, 4), dpi=120, facecolor="lightgray")   # 设置图形画布
plt.title("Figure Object 1", fontsize=18)   # 图例标题
plt.figure("Figure Object 2", figsize=(5, 4), dpi=120, facecolor="lightgreen")

plt.xlabel("x", fontsize=12)   # x轴坐标标签
plt.ylabel("y", fontsize=12)   # y轴坐标标签

plt.tick_params(labelsize=10)   # 轴上标签字体的大小

plt.grid(linestyle=":")   # 网格线

plt.plot(x, cos_y, label=r"$y=\frac{1}{2}cos(x)$")
plt.legend()

plt.show()