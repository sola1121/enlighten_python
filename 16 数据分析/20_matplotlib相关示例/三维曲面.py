import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

plt.figure('3D Wireframe')
ax = plt.gca(projection='3d')
plt.title('3D Wireframe', fontsize=20)

ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
plt.tick_params(labelsize=10)

ax.plot_wireframe(x, y, z, rstride=30, cstride=30, linewidth=0.5, color='orangered')
plt.show()