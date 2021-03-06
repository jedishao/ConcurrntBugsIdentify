# @Time    : 4/10/22 10:55 PM
# @Author  : Shuai S
# @File    : weka_dataset.py

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

import labelOfdata

np.set_printoptions(threshold=np.inf)

conSents = open("../../dataset/dataset1/redisson/pos.txt", encoding='utf-8')
ifidf = open("C:/Users/Shao/Desktop/s.md", 'w', encoding='utf-8')
#ifidf = open("../../dataset/dataset1/redisson/idif.txt", 'w', encoding='utf-8')
data = []

for line in conSents:
    data.append(line)

#vector = TfidfVectorizer(stop_words='english')
vector = CountVectorizer(stop_words='english')
X_train = vector.fit_transform((d for d in data))
#X_train = vector.fit_transform((d for d in data))
#print(len(vector.get_feature_names()))
for v in vector.get_feature_names():
    print("@attribute '"+v+"' real")
# print(X_train)
arr = X_train.toarray()
# print(len(arr))
i = 1
for w in arr:
    #print(len(w))
    wr = w.tolist()
    if i < 3488:
        wr.append(0)
    else:
        wr.append(1)
    ifidf.write(str(wr))
    ifidf.write('\n')
    i += 1
# #print(len(arr))
# conSents.close()
# ifidf.close()
