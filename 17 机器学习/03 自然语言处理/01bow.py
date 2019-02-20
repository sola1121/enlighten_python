import nltk.tokenize as nltoken
import sklearn.feature_extraction.text as ft

doc = "The brown dog is running. The black dog is in the black room. Running in the room is forbidden."

sentences = nltoken.sent_tokenize(doc)   # 返回指定语言的每句话
for i, sentence in enumerate(sentences):
    print(i + 1, sentence)

cv = ft.CountVectorizer()   # 计数矢量化器

bow = cv.fit_transform(sentences).toarray()   # Learn the vocabulary dictionary and return term-document matrix.
print("每句中单词出现的次数", bow)
