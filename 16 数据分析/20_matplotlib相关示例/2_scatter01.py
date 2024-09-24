import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

xo = np.pi * 3/4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)

plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(sin_y.min() * 1.1, sin_y.max() * 1.1)

# 设置x轴, y轴的值
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3/4, np.pi], 
           [r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$", r"$\frac{\pi}{2}$", r"$\frac{\pi}{4}$",r"$-\pi$"])
plt.yticks([-1, -0.5, 0.5, 1])

# 设置坐标轴到原点
axis = plt.gca()   # 获取当前坐标轴
axis.spines["left"].set_position(("data", 0))   # 设置左边的坐标轴到零点
axis.spines["bottom"].set_position(("data", 0))   # 设置低端的坐标轴到零点
axis.spines["top"].set_color(None)   # 设置上坐标轴无色
axis.spines["right"].set_color(None)   # 设置右坐标轴无色

plt.plot(x, cos_y, linestyle="--", linewidth=2.0, color="#66ccff", label="")
plt.plot(x, sin_y, linestyle=":",  linewidth=2.0, color="r")

plt.scatter([xo, xo], [yo_cos, yo_cos])

plt.legend(loc="lower left")

plt.show()
