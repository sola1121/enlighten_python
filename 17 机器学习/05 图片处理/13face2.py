import sklearn.datasets as sd
import sklearn.model_selection as sks
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as plt


faces = sd.fetch_olivetti_faces("../data")

y = faces.data
x = faces.target

train_x, test_x, train_y, test_y = sks.train_test_split(x, y, test_size=0.2, random_state=7)
model = svm.SVC(class_weight="balance")
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / len(pred_test_y))   # 查看精度
print(sm.classification_report(test_y, pred_test_y))