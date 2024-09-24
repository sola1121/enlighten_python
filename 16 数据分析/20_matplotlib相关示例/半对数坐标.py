import numpy as np
import matplotlib.pyplot as plt


y = np.array([1, 10, 100, 1000, 100, 10, 1])
plt.figure('Normal & Log', facecolor='lightgray')

plt.subplot(211)
plt.title('Normal', fontsize=16)

plt.ylabel('y', fontsize=12)

ax = plt.gca()
ax.xaxis.set_major_locator( plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))

plt.tick_params(labelsize=10)

plt.grid(which='major', axis='both', linewidth=0.75, linestyle='-', color='lightgray')
plt.grid(which='minor', axis='both', linewidth=0.25, linestyle='-', color='lightgray')

plt.plot(y, 'o-', c='dodgerblue', label='plot')
plt.legend()

# ========使用半对数坐标的子图=========

plt.subplot(212)   # 在当前画布创建子图
plt.title('Log', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

ax = plt.gca()   # 获取当前子图坐标轴
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))

plt.tick_params(labelsize=10)
plt.grid(which='major', axis='both', linewidth=0.75, linestyle='-', color='lightgray')
plt.grid(which='minor', axis='both', linewidth=0.25, linestyle='-', color='lightgray')

plt.semilogy(y, 'o-', c='orangered', label='semilog')   # 创建半对数坐标

plt.legend()
plt.tight_layout()   # 紧密

plt.show()
