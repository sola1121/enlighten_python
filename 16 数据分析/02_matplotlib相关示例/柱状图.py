import numpy as np
import matplotlib.pyplot as plt

n = 12
x = np.arange(n)
y1 = (1 - x / n) * np.random.uniform(0.5, 1.0, n)   # 生成均匀分布的样本
y2 = (1 - x / n) * np.random.uniform(0.5, 1.0, n)

plt.figure('Bar', facecolor='lightgray')   # 画布设置
plt.title('Bar', fontsize=20)

plt.ylim(-1.25, 1.25)   # y轴范围限制

plt.xlabel('x', fontsize=14)   # x, y轴标签
plt.ylabel('y', fontsize=14)

plt.xticks(x, x + 1)   # 设置刻度 (刻度位置, 刻度文本)
plt.tick_params(labelsize=10)

plt.grid(axis='y', linestyle=':')   # 轴y格栅

plt.bar(x, y1, ec='white', fc='dodgerblue', label='Sample 1')   # 柱状图样本1
for _x, _y in zip(x, y1):
    plt.text(_x, _y, '%.2f' % _y, ha='center', va='bottom', size=8)

plt.bar(x, -y2, ec='white', fc='dodgerblue', alpha=0.5, label='Sample 2')   # 柱状图样本2
for _x, _y in zip(x, y2):
    plt.text(_x, -_y - 0.015, '%.2f' % _y, ha='center', va='top', size=8)

plt.legend()   # 显示说明标签label

plt.show()