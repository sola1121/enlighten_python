import os
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open(os.path.dirname(__file__) + '/multiple2.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=5)

# 传参列表
params = [
    {"kernel": ["linear"], "C": [1, 10, 100]},
    {"kernel": ["poly"], "C": [1], "degree": [2, 3]},
    {"kernel": ["rbf"], "C": [1, 10, 100, 1000], "gamma": [1, .1, .01, .001]},   # 径向基函数
]
TODO:
model = ms.GridSearchCV(svm.SVC(probability=True), params, cv=5)
model.fit(train_x, train_y)
model.cv_results_["params"]
model.cv_results_["mean_test_score"]

l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

prob_x = np.array([
    [2,   1.5],
    [8,   9],
    [4.8, 5.2],
    [4,   4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])

print(prob_x)
pred_prob_y = model.predict(prob_x)
print(pred_prob_y)
probs = model.predict_proba(prob_x)
print(probs)
mp.figure('The Best Hyperparameter', facecolor='lightgray')
mp.title('The Best Hyperparameter', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
C0, C1 = y == 0, y == 1
mp.scatter(x[C0][:, 0], x[C0][:, 1], c='orangered', s=60)
mp.scatter(x[C1][:, 0], x[C1][:, 1], c='limegreen', s=60)
C0, C1 = pred_prob_y == 0, pred_prob_y == 1
mp.scatter(prob_x[C0][:, 0], prob_x[C0][:, 1], marker='D', c='dodgerblue', s=60)
mp.scatter(prob_x[C1][:, 0], prob_x[C1][:, 1], marker='D', c='deeppink', s=60)

for i in range(len(probs[C0])):
    mp.annotate('{}% {}%'.format(
        round(probs[C0][:, 0][i] * 100, 2),
        round(probs[C0][:, 1][i] * 100, 2)),
        xy=(prob_x[C0][:, 0][i],
            prob_x[C0][:, 1][i]),
        xytext=(12, -12), textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'deepskyblue', 'alpha': 0.8})

for i in range(len(probs[C1])):
    mp.annotate('{}% {}%'.format(
        round(probs[C1][:, 0][i] * 100, 2),
        round(probs[C1][:, 1][i] * 100, 2)),
        xy=(prob_x[C1][:, 0][i],
            prob_x[C1][:, 1][i]),
        xytext=(12, -12), textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'violet', 'alpha': 0.8})

mp.show()
