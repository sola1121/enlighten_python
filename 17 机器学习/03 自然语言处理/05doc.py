import os
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb   # 使用朴素贝叶斯分类器


train = sd.load_files(os.path.dirname(__file__) + "/data/20news",       # 获取文件中数据, 会按照文件夹进行分类
                      encoding="latin1", shuffle=True, random_state=7)  # 设置随机排序
train_data = train.data
print(len(train_data))   # 样本个数

train_y = train.target
categories = train.target_names
print(categories)   # 分类的方式, 按照文件夹名来的

cv = ft.CountVectorizer()
train_bow = cv.fit_transform(train_data)
print(train_bow.shape)   # (行, 列), 行代表样本个数, 列代表样本属性

tt = ft.TfidfTransformer()
train_x = tt.fit_transform(train_bow)

# 建立模型
model = nb.MultinomialNB()   # 多项分布
model.fit(train_x, train_y)

# 测试数据
test_data = [
    "Nothing to say, just the data to test the result of learning."
]

test_bow = cv.transform(test_data)   # 将文档转换成文档-术语矩阵。
test_x = tt.transform(test_bow)   # 将一个计数矩阵转换为tf或tf-idf表示法
pred_test_y = model.predict(test_x)
print("预测分类的编号", pred_test_y)

# 测试数据与预测数据
for sentence, index in zip(test_data, pred_test_y):
    print(sentence, "->", categories[index])
