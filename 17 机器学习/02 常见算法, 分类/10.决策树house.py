import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm


housing = sd.load_boston()     # 波斯顿的房子
print(housing.feature_names)   # 影响房价的特征
print(housing.data.shape)      # 二维数据集形状
print(housing.target.shape)    # 数据条数(行)

x, y = su.shuffle(housing.data, housing.target, random_state=7)   # 进行洗牌, 让样本分布随机
train_size = int(len(x) * .8)                                     # 训练使用个数的80% 
# 训练用的输入train_x, 测试用的输入test_x, 训练用的输出train_y, 测试用的输出test_y
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 决策树
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)

pred_test_y = model.predict(test_x)       # 预测输出
print(sm.r2_score(test_y, pred_test_y))   # 预测效果与实际测试数据比对, 找出模型精度


# 基于决策树的正向激励
model = se.AdaBoostRegressor(st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
model.fit(train_x, train_y)

pred_test_y = model.predict(test_x)       # 预测输出
print(sm.r2_score(test_y, pred_test_y))   # 预测效果与实际测试数据比对, 找出模型精度

# 输出与测试数据的比对结果
for test, pred_test in zip(test_y, pred_test_y):
    print("实际测试数据", test, "预测数据", pred_test)