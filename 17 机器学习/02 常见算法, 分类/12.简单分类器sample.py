import numpy as np
import matplotlib.pyplot as plt
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))

flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = np.zeros(len(flat_x), dtype=int)
flat_y[flat_x[:, 0] < flat_x[:, 1]] = 1
grid_y = flat_y.reshape(grid_x[0].shape)

plt.figure('Simple Classification', facecolor='lightgray')
plt.title('Simple Classification', fontsize=20)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')

plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=60)

plt.show()