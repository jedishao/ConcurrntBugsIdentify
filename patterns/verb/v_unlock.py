# @Time    : 4/28/22 4:12 PM
# @Author  : Shuai S
# @File    : v_unlock.py

import spacy

import corpus

# I'm using RxJava and as a part of the sequence I use a RLock, at some point (in another process) I unlock it and if the thread to unlock is not the same as the one that blocked I get an exception (see below).

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, exc = False, False
    for token in doc:
        if str(token.lemma_) == 'unlock':
            cmi = True
        elif str(token.lemma_) in corpus.BAD:
            exc = True
    if cmi:
        if exc:
            return 'P72'

for lii in lineList:
    s = check(lii)
    print(s)
