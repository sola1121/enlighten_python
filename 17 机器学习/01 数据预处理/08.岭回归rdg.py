import os
import numpy as np
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

model_ln = lm.LinearRegression()   # 构建一个线性回归器
model_ln.fit(x, y)
pred_y_ln = model_ln.predict(x)   # 预测结果

print("平均值误差", sm.mean_absolute_error(y, pred_y_ln))
print("平均值平方误差", sm.mean_squared_error(y, pred_y_ln))
print("中位数误差", sm.median_absolute_error(y, pred_y_ln))


model_rd = lm.Ridge(150, fit_intercept=True, max_iter=10000)
model_rd.fit(x, y)
pred_y_rd = model_rd.predict(x)

plt.figure("Linear Regression", facecolor="lightgray")
plt.title("Linear Regression", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.scatter(x, y, c="dodgerblue", alpha=0.75, s=60, label='Sample')

sorted_indices = x.T[0].argsort()

plt.plot(x[sorted_indices], pred_y_ln[sorted_indices], 'o-', c='orangered', label='Regression')
plt.plot(x[sorted_indices], pred_y_rd[sorted_indices], 'o-', c='limegreen', label='Ridge')

plt.legend()
plt.show()
