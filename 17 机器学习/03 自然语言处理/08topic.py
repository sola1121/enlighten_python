import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)   # 忽略用户级警告

import nltk.tokenize as nltoken
import nltk.corpus as sc
import nltk.stem.snowball as snowball
import gensim.models.ldamodel as gm
import gensim.corpora as gc

doc = list()

with open(os.path.dirname(__file__) + "/data/topic.txt") as f:
    for line in f.readlines():
        doc.append(line)

tokenizer = nltoken.RegexpTokenizer(r"\w+")    # 见空白就拆开
stopwords = sc.stopwords.words("english")   # 停止词汇
stemmer = snowball.SnowballStemmer("english")
lines_tokens = list()

# 被拆开的句子是一个行列式, 一行表示一句, 一列表示一个单词
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = list()
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    line_tokens.append(line_tokens)

dic = gc.Dictionary(lines_tokens)   # 构建词典, 用于构建词袋

bow = list()
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)                 # 构建了词袋

print(bow)

TODO: 没有完成学习
