import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

plt.figure("Signal", facecolor="lightgray")
plt.title("Signal", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Signal", fontsize=14)

ax = plt.gca()   # 设置轴
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)

plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
line_obj = plt.plot([], [], c="orangered")[0]
line_obj.set_data([], [])

def update(data):
    time_, value_ = data
    x, y = line_obj.get_data()
    x.append(time_)
    y.append(value_)
    x_min, x_max = ax.get_xlim()
    if time_ > x_max:
        ax.set_xlim(time_ - (x_max - x_min), time_)   # 避免超出范围
        ax.figure.canvas.draw()
    line_obj.set_data(x, y)

def gen_func():
    """模拟信号发生的生成器"""
    time_ = 0
    while True:
        value_ = np.sin(2 * np.pi * time_) * np.exp(np.sin(0.2 * np.pi * time_))
        yield time_, value_
        time_ += 0.05

update_func = anime.FuncAnimation(plt.gcf(), update, gen_func, interval=5)

plt.show()
