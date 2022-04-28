# @Time    : 4/28/22 3:26 PM
# @Author  : Shuai S
# @File    : n_deadlock.py
import spacy

import corpus

# Deadlock using RedissonMultiLock.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'deadlock':
            for child in token.children:
                if str(child.dep_) == 'acl':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P69'


for lii in lineList:
    s = check(lii)
    print(s)
