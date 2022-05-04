# -*- codeing = utf-8 -*-
# @Time : 5/3/2022 10:08 PM
# @Author : Shao
# @File : kw_search.py
# @Software : PyCharm
import spacy

nlp = spacy.load("en_core_web_sm")
conSents = open("dataset/dataset1/hsqldb/hsqldb_format.txt", encoding='utf-8')
data = []
for line in conSents:
    data.append(line)
# ['thread', 'blocked', 'locked', 'race', 'dead-lock', 'deadlock', 'concurrent',
#                                  'concurrency', 'atomic', 'synchronize', 'syn-chronous', 'synchronization',
#                                  'starvation', 'suspension', 'order', 'violation',
#                                  'atomicity', 'livelock', 'live-lock',
#                                  'multi-threaded', 'multithreading', 'multi-thread.']:
count = 0
for rl in data:
    doc = nlp(rl)
    b, lock = 0, 0
    for token in doc:
        if str(token.lemma_) in ['thread', 'blocked', 'locked', 'race', 'dead-lock', 'deadlock', 'concurrent',
                                         'concurrency', 'atomic', 'synchronize', 'syn-chronous', 'synchronization',
                                         'starvation', 'suspension', 'order', 'violation',
                                         'atomicity', 'livelock', 'live-lock',
                                         'multi-threaded', 'multithreading', 'multi-thread.']:
            count += 1
            break
        # if str(token.lemma_) in ['compete', 'atomic', 'concurrency', 'synchronization', 'race', 'deadlock',
        #                          'concurrent', 'mutex']:
        #     count += 1
        #     break
        # elif str(token.lemma_) in ['read', 'write', 'acquire', 'wrong', 'miss']:
        #     b += 1
        # elif str(token.lemma_) == 'lock':
        #     lock += 1
        # if b and lock:
        #     count += 1
        #     break

print(count)
