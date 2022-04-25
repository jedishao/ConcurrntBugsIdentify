# @Time    : 4/23/22 7:36 PM
# @Author  : Shuai S
# @File    : p_get.py
import spacy

import corpus

# threads are getting stuck.
# two thread get the same lock by trylock?
# multiple threads get the lock at the same time.
# sometime lock.tryLock() can not get lock.
# Thread gets stuck when trying to acquire lock via tryLock().
# Some threads get stuck at the Waiting state at tryLock.

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sbj, symp, obj, neg = False, False, False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.S:
                    if str(child.lemma_) in corpus.MEC:
                        sbj = True
                elif str(child.dep_) == 'acomp':
                    if str(child.lemma_) in corpus.SYMP:
                        symp = True
                elif str(child.dep_) in corpus.OBJ:
                    if str(child.lemma_) in corpus.MEC:
                        obj = True
                elif str(child.dep_) == 'neg':
                    neg = True

    if sbj:
        if symp:
            return 'p11'
        elif neg and obj:
            return 'p12'
        elif obj:
            return 'p13'


for lii in lineList:
    s = check(lii)
    print(s)
