import os
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as plt


x, y = [], []
with open(os.path.dirname(__file__) + "/single.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])

x = np.array(x)
y = np.array(y)
model = pl.make_pipeline(sp.PolynomialFeatures(10), lm.LinearRegression())   # 与多项式(1)管道连接
model.fit(x, y)
pred_y = model.predict(x)

print("平均值误差", sm.mean_absolute_error(y, pred_y))
print("平均值平方误差", sm.mean_squared_error(y, pred_y))
print("中位数误差", sm.median_absolute_error(y, pred_y))

test_x = np.linspace(x.min(), x.max(), 1000)[:, np.newaxis]
test_y = model.predict(test_x)

plt.figure("Polynomial Regression", facecolor="lightgray")
plt.title("Polynomial Regression", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.scatter(x, y, c="dodgerblue", alpha=0.75, s=60, label='Sample')

sorted_indices = x.T[0].argsort()

plt.plot(test_x, test_y, c='orangered', label='Regression')

plt.legend()
plt.show()
