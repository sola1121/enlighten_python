# 通过名字判断用户的性别

import random
import numpy as np
import nltk.corpus as nc
import nltk.classify as cf

# 训练样本
male_names = nc.names.words("male.txt")
female_names = nc.names.words("female.txt")

models, acs = [], []
for n_letters in range(1, 6):
    data = []
    for male_name in male_names:
        feature = {"feature": male_name[-n_letters:].lower()}
        data.append((feature, "male"))
    for female_name in female_names:
        feature = {"featrue": female_name[-n_letters:].lower()}

# 将数据顺序打乱
    random.seed(7)
    random.shuffle(data)

# 各取一半数据仅用于训练和测试
    train_data = data[:int(len(data)/2)]
    test_data = data[int(len(data)/2):]

# 使用nltk中的朴素贝叶斯分类方法, 直接返回训练好的
    model = cf.NaiveBayesClassifier.train(train_data)

    ac = cf.accuracy(model, test_data)   # 准确度
    models.append(model)
    acs.append(ac)

# 选择其中最好的模型
best_index = np.array(ac).argmax()
best_letters = best_index + 1
best_model = models[best_index]
best_ac = acs[best_index]
print(best_letters, best_ac)


# 测试
names = ["leveo", "ben", "sam"]

genders = []
for name in names:
    feature = {"feature": name[-best_letters:].lower()}
    gender = best_model.classify(name)
    genders.append(gender)

for name, gender in zip(names, genders):
    print(name, gender)

