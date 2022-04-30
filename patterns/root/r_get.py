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
# I got this problem when I trying to locking an object.


def check(nlp, line):
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
            return 57
        elif neg and obj:
            return 58
        elif obj:
            return 59
        elif exc:
            return 60
    if cmi:
        if exc:
            return 61
