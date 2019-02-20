import matplotlib.pyplot as plt

plt.figure(facecolor='lightgray')

plt.axes([0.03, 0.038, 0.94, 0.924])   # 新增轴线
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, '1', ha='center', va='center', size=36, alpha=0.5)

plt.axes([0.63, 0.076, 0.31, 0.308])   # 新增轴线
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, '2', ha='center', va='center', size=36, alpha=0.5)
plt.show()