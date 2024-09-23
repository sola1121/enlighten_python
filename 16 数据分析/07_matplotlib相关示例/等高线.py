import numpy as np
import matplotlib.pyplot as plt

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))   # 返回坐标, linspace
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

plt.figure('Contour', facecolor='lightgray')
plt.title('Contour', fontsize=20)

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

plt.tick_params(labelsize=10)

plt.grid(linestyle=':')   # 格栅

plt.contourf(x, y, z, 8, cmap='jet')

cntr = plt.contour(x, y, z, 8, colors='black', linewidths=0.5)
plt.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)

plt.show()
