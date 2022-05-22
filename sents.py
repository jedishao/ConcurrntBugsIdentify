# -*- codeing = utf-8 -*-
# @Time : 5/4/2022 5:54 PM
# @Author : Shao
# @File : sents.py
# @Software : PyCharm
import spacy

import Identify

linelist = []
li = []
nlp = spacy.load("en_core_web_sm")
# conSents = open("dataset/dataset1/redisson/redisson_pos.txt", encoding='utf-8')
# conSents = open("dataset/dataset1/redisson/redisson_pos.txt", encoding='utf-8')
# conSents = open("dataset/dataset1/redisson/redisson_pos.txt", encoding='utf-8')
conSents = open("dataset/dataset1/pos.txt", encoding='utf-8')
for lil in conSents:
    linelist.append(lil)

j = 0
for re in linelist:
    doc = nlp(re)
    for sent in doc.sents:
        li.append(str(sent))
print(len(li))

lsls = []
for ll in li:
    doc = nlp(ll)
    for token in doc:
        if str(token.pos_) == 'NOUN':
            if not lsls.__contains__(str(token.lemma_)):
                lsls.append(str(token.lemma_))
print(len(lsls))
print(lsls)
# ji = 0
# for token in li:
#     doc = nlp(token)
#     for t in doc:
#         # 'lock', 'transcation', 'race', 'concurrence', 'concurrency', 'concurrent', 'cmi',
#         # 'order', 'race', 'deadlock', 'livelock' 'unlock', 'block', 'hang'
#         if str(t.lemma_) in ['thread']:
#             ji += 1
#             break
# print(ji)
# k = 0
# l1 = {}
# l2 = {}
# l3 = {}
# l4 = {}
# l5 = {}
# for lll in li:
#     if k < 234:
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 460:
#         if k == 234:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 690:
#         if k == 460:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 900:
#         if k == 690:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 1100:
#         if k == 900:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 1400:
#         if k == 1100:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 1700:
#         if k == 1400:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     elif k < 2000:
#         if k == 1700:
#             print(len(l1))
#             print(l1)
#         rew = Identify.identify(nlp, lll)
#         l1[rew] = 0
#     k += 1
# print(len(l1))
# print(l1)
# l1
# print(j)
