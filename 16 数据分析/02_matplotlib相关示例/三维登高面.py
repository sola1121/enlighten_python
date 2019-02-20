import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))   # x, y 轴数据
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)   # z轴数据

plt.figure('3D Surface')
plt.title('3D Surface', fontsize=20)

ax = plt.gca(projection='3d')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)

plt.tick_params(labelsize=10)

ax.plot_surface(x, y, z, rstride=30, cstride=30, cmap='jet')   # x, y, z, rstride=行距,cstride=列距, cmap=颜色映射

plt.show()
