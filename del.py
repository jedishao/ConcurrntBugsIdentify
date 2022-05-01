# @Time    : 4/2/22 8:23 PM
# @Author  : Shuai S
# @File    : del.py
# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# fil = open('dataset/dataset1/redisson/redisson_neg.txt', encoding='utf-8')
#
# li = []
# for line in fil:
#     li.append(line)
# lp = []
# j = 0
# for l in li:
#     doc = nlp(l)
#     for d in doc.sents:
#         lp.append(str(d))
#     for lll in lp:
#         doc = nlp(lll)
#         key = 0
#         for token in doc:
#             if str(token.lemma_) in ['compete', 'atomic', 'concurrency', 'synchronization', 'race', 'deadlock',
#                                      'deadlocked', 'concurrent',
#                                      'mutex', 'lock']:
#                 key = 1
#     if key == 1:
#         j += 1
#     lp = []
#
#
# print(j)

for i in range(5):
    print(i)