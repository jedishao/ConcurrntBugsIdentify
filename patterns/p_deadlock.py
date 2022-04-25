# @Time    : 4/23/22 6:04 PM
# @Author  : Shuai S
# @File    : p_deadlock.py
import spacy

import corpus

# Deadlock while obtaining lock.
# Deadlock on lock() and not only.
# Deadlock with RedissonLock used by JCache.
# Deadlock while obtaining lock.
# Deadlock after Redis timeout.
# The deadlock of RedissonMultiLock.
# RedissonFairLock deadlock.
# RedissonFairLock deadlock.
# Thread deadlock when using distributed lock on 1.2.1.

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'advcl':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            return 'p7'
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            return 'p8'
                        elif str(grandchild.dep_) == 'pobj':
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild) in corpus.MEC:
                                    return 'p9'
                elif str(child.dep_) == 'compound':
                    if str(child) in corpus.MEC:
                        return 'p10'


for lii in lineList:
    s = check(lii)
    print(s)

