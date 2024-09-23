import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

grid = gs.GridSpec(3 , 3)   # 一个3*3 的格栅

plt.subplot(grid[0, :2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "1", ha="center", va="center", size=36, alpha=.5)
plt.tight_layout()   # 紧密布局

plt.subplot(grid[2:, :3])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, "2", ha="center", va="center", size=36, alpha=.5)
plt.tight_layout()   # 紧密布局



plt.show()
