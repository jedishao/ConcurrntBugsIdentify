# @Time    : 4/23/22 7:36 PM
# @Author  : Shuai S
# @File    : r_get.py
import spacy

import corpus

# threads are getting stuck.
# two thread get the same lock by trylock?
# multiple threads get the lock at the same time.
# sometime lock.tryLock() can not get lock.
# Thread gets stuck when trying to acquire lock via tryLock().
# Some threads get stuck at the Waiting state at tryLock.
# we get errors when unlocking.
# After that I get exception and unlock only after expiration in 30 sec.
# When I try to get lock using the following code, i get an error saying that i can't write to a Slave.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sbj, symp, obj, neg, exc, cmi = False, False, False, False, False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        sbj = True
                elif str(child.dep_) == 'acomp':
                    if str(child.lemma_) in corpus.SYMP:
                        symp = True
                elif str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.MEC:
                        obj = True
                    elif str(child.lemma_) in corpus.BAD:
                        exc = True
                elif str(child.dep_) == 'neg':
                    neg = True
        elif str(token.lemma_) in corpus.ULO:
            sbj = True
        elif str(token.lemma_) in corpus.MEC:
            cmi = True

    if sbj:
        if symp:
            return 'P11'
        elif neg and obj:
            return 'P12'
        elif obj:
            return 'P13'
        elif exc:
            return 'P74'
    if cmi:
        if exc:
            return 'P75'


for lii in lineList:
    s = check(lii)
    print(s)
