import nltk.tokenize as nltoken
import sklearn.feature_extraction.text as ft
import sklearn.preprocessing as sp

doc = "The brown dog is running. The black dog is in the black room. Running in the room is forbidden."

sentences = nltoken.sent_tokenize(doc)   # 返回指定语言的每句话
for i, sentence in enumerate(sentences):
    print(i + 1, sentence)

cv = ft.CountVectorizer()   # 计数矢量化器
words = cv.get_feature_names()
print("统计了哪些单词", words)
bow = cv.fit_transform(sentences).toarray()   # Learn the vocabulary dictionary and return term-document matrix.
print("每句中单词出现的次数\n", bow, end="\n\n")
words = cv.get_feature_names()
print("统计了哪些单词", words, end="\n\n")
tf = sp.normalize(bow, norm="l1")   # Scale input vectors individually to unit norm (vector length).
print("词频, 单词出现次数占句总数的比例\n", tf, end="\n\n")

