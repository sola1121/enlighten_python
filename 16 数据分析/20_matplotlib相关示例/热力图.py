import numpy as np
import matplotlib.pyplot as plt
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

plt.figure('Hot', facecolor='lightgray')
plt.title('Hot', fontsize=20)

plt.xlabel('x', fontsize=14)   # 设置x轴, y轴标签
plt.ylabel('y', fontsize=14)

plt.tick_params(labelsize=10)   # 设置
plt.grid(linestyle=':')

plt.imshow(z, cmap='jet', origin='low')   # 绘制热力图

plt.show()
