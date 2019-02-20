# 根据语言中某些特定的单词来判断情感

import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu


positive_datas = list()
negtive_datas = list()

# 正面评价
fileids = nc.movie_reviews.fileids("pos")
for fileid in fileids:
    feature = dict()
    words = nc.movie_reviews.words(fileid)   # 拿出nltk_data中的数据
    for word in words:
        feature[word] = True
    positive_datas.append((feature, "POSITIVE"))

# 负面评价
fileids = nc.movie_reviews.fileids("neg")
for fileid in fileids:
    feature = dict()
    words = nc.movie_reviews.words(fileid)   # 拿出nltk_data中的数据
    for word in words:
        feature[word] = False
    negtive_datas.append((feature, "NEGTIVE"))

# 各取80%的数据用于训练
positive_num, negtive_num = int(len(positive_datas)*0.8), int(len(negtive_datas)*0.8)

train_data = positive_datas[:positive_num] + negtive_datas[:negtive_num]
test_data = positive_datas[positive_num:] + negtive_datas[negtive_num:]

model = cf.NaiveBayesClassifier.train(train_data)   # 朴素叶贝斯分类

ac = cu.accuracy(model, test_data)
print("准确度", ac)

tops = model.most_informative_features()
print(len(tops))
print(tops[:10])


# 自己写点来测试
reviews = [
    "It's not a good movie, nothing worth to watch.",
    "amazing, I never see a movie like this.",
]

sents, probs = list(), list()
for review in reviews:
    feature = dict()
    words = review.split()
    for word in words:
        feature[word] = True
        pcls = model.prob_classify(feature)
        sent = pcls.max()
        prob = pcls.prob(sent)
        sents.append(sent)
        probs.append(prob)

for review, sent, prob in zip(reviews, sents, probs):
    print(review, "->", sent, round(prob, 4))
