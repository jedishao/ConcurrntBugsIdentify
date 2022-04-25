# @Time    : 4/23/22 9:16 PM
# @Author  : Shuai S
# @File    : p_lock.py

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
                if str(child.dep_) in corpus.S:
                    if str(child.lemma_) in corpus.MEC:
                        return 'P16'
                elif str(child.dep_) in ['auxpass', 'advcl']:
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.S:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P17'
                elif str(child.dep_) in corpus.OBJ:
                    if str(child.lemma_) in corpus.MEC:
                        return 'P18'
                    elif str(child.lemma_) in corpus.COP:
                        return 'P19'
                elif str(child.dep_) in corpus.ADV:
                    if str(child.lemma_) in corpus.TMP:
                        return 'P20'


for lii in lineList:
    s = check(lii)
    print(s)
