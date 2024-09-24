import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2 * np.pi, 1001)
r_spiral = 0.8 * t
r_rose = 5 * np.sin(6 * t)

plt.figure('Polar', facecolor='lightgray')
plt.gca(projection='polar')   # 使用极面坐标
plt.title('Polar', fontsize=20)

plt.xlabel(r'$\theta$', fontsize=14)   # 设置x, y轴标签
plt.ylabel(r'$\rho$', fontsize=14)

plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

plt.plot(t, r_spiral, c='dodgerblue', label=r'$\rho=0.8\theta$')   # 在其中绘制螺旋图形
plt.plot(t, r_rose, c='orangered', label=r'$\rho=5sin(6\theta)$')   # 在其中绘制sin的图

plt.legend()

plt.show()
