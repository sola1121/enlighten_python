import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt


data = np.loadtxt("mono.txt")

train_x, train_y = data[:, :2], data[:, 2:]

train_labels = list()   # 标签

for train_row in train_y:
    train_row.astype(int).astype(str)
    train_labels.append(".".join(train_row))
label_set = np.unique(train_labels)   # 去重

train_codes = list()
for train_label in train_labels:
    np.where(label_set == train_label)[0][0]
    train_codes.append(train_code)
train_codes = np.array(train_codes)

# x = np.array([
#     [.3, .2],
#     [.1, .4],
#     [.4, .6],
#     [.9, .5]
# ])

# y = np.array([0, 0, 0, 1])   # 期望的效果

# # 建立单神经感知器模型
# model = nl.net.newp([[0, 1], [0, 1]], 1)   # (对应输入的范围, 有几个输出)

# # 训练并获取误差
# error = model.train(x, y, epochs=10, show=1, lr=0.01)   # epochs做多少次, show显示批次, lr学习率

# plt.figure("Neuron", facecolor="lightgray")
# plt.title("Neuron", fontsize=12)
# plt.xlabel("x", fontsize=10)
# plt.ylabel("y", fontsize=10)
# plt.tick_params(labelsize=10)
# plt.grid(":")
# plt.scatter(x[:0], y[:1], c=y.ravel(), cmap="brg", label="Training")

# plt.legend()
# plt.show()

