# @Time    : 4/23/22 9:16 PM
# @Author  : Shuai S
# @File    : r_lock.py

import spacy
import corpus

# CMI locks up.
# Under heavy use on production, Redisson's locks get all locked up, and the application stalls.
# The other threads, that are waiting for a separate lock are locked even though there is no-one taking up such lock....
# when thread is interrupt...all Reference variables is locked!
# As i understand it shouldn't lock the calling thread, and return value (Future) as soon as possible.
# Indefinite lock lost during master failover.
# No matter which lock is locked first in thread t1, the Red Lock will always can be locked or cannot.
# In this case, the Red Lock should always be locked for most of the lock is available.
# redisson lock uncontrolled release.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        return 75
                elif str(child.dep_) in ['auxpass', 'advcl']:
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.s:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 76
                elif str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.MEC:
                        return 77
                    elif str(child.lemma_) in corpus.COP:
                        return 78
                    elif str(child.lemma_) in corpus.BAD:
                        return 79
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        return 80
