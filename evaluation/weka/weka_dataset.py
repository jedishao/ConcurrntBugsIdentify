# @Time    : 4/10/22 10:55 PM
# @Author  : Shuai S
# @File    : weka_dataset.py

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

import labelOfdata

np.set_printoptions(threshold=np.inf)

conSents = open("data/redisson.txt", encoding='utf-8')
ifidf = open("data/redisson_ifidf.txt", 'w', encoding='utf-8')

data = []

for line in conSents:
    data.append(line)

vector = TfidfVectorizer(stop_words='english')

X_train = vector.fit_transform((d for d in data))
print(len(vector.get_feature_names_out()))
# for v in vector.get_feature_names_out():
#     print("@attribute '"+v+"' real")
# print(X_train)
arr = X_train.toarray()
for w in arr:
    print(len(w))
    # wr = arr[w].tolist()
    # wr.append(labelOfdata.redisson_label[w])
    # ifidf.write(str(wr))
    # ifidf.write('\n')
# #print(len(arr))
# conSents.close()
# ifidf.close()
