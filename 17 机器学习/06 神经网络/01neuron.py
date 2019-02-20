import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt


x = np.array([
    [.3, .2],
    [.1, .4],
    [.4, .6],
    [.9, .5]
])

y = np.array([0, 0, 0, 1])   # 期望的效果

# 建立单神经感知器模型
model = nl.net.newp([[0, 1], [0, 1]], 1)   # (对应输入的范围, 有几个输出)

# 训练并获取误差
error = model.train(x, y, epochs=50, show=1, lr=0.01)   # epochs做多少次, show显示批次, lr学习率

plt.figure("Neuron", facecolor="lightgray")
plt.title("Neuron", fontsize=12)
plt.xlabel("x", fontsize=10)
plt.ylabel("y", fontsize=10)
plt.tick_params(labelsize=10)
plt.grid(":")
plt.scatter(x[:0], y[:1], c=y.ravel(), cmap="brg", label="Training")

plt.legend()
plt.show()

