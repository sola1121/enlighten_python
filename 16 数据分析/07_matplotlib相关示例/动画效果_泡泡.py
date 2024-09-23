import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

n_bubbles = 100   # 气泡个数

# 气泡的浮动涉及 位置, 大小, 增长, 颜色
bubbles = np.zeros(n_bubbles, dtype=[
    ("position", float, 2),   # n_bubbles行, 2列
    ("size", float, 1),
    ("growth", float, 1),
    ("color", float, 4)
    ]) 

bubbles["position"] = np.random.uniform(0, 1, size=(n_bubbles, 2))   # 维度, 100行两列
bubbles["size"] = np.random.uniform(50, 750, size=n_bubbles)   # 百行
bubbles["growth"] = np.random.uniform(30, 150, n_bubbles)   # 百行
bubbles["color"] = np.random.uniform(0, 1, (n_bubbles, 4))   # 百行四列

plt.figure("Bubbles", facecolor="lightgray")
plt.title("Bubbles", fontsize=12)
plt.xticks(())
plt.yticks(())

obj = plt.scatter(bubbles["position"][:, 0], bubbles["position"][:, 1], s=bubbles["size"], c=bubbles["color"])   # 使用点图

def update(number):
    bubbles["size"] += bubbles["growth"]
    burst = number % n_bubbles   # 让破裂的气泡数在n_bubbles所给数量中
    bubbles["position"][burst] = np.random.uniform(0, 1, size=2)   # 一维数组两列
    bubbles["size"][burst] = 0
    bubbles["growth"][burst] = np.random.uniform(30, 150)
    bubbles["color"][burst] = np.random.uniform(0, 1, 4)   # 一维数组四列
    obj.set_offsets(bubbles["position"])
    obj.set_sizes(bubbles["size"])    
    obj.set_facecolor(bubbles["color"])

update_func = anime.FuncAnimation(plt.gcf(), update, interval=10)   # 创建动画, 使用变量让其不被回收

plt.show()

