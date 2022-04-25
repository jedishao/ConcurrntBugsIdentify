# @Time    : 4/23/22 8:58 PM
# @Author  : Shuai S
# @File    : p_obtain.py
import spacy

import corpus
# The same lock name was likely concurrently obtained and held by another thread possibly on another jvm.

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sam, mec = False, False
    for token in doc:
        if str(token.lemma_) == 'same':
            sam = True
        elif str(token.lemma_) in corpus.MEC:
            mec = True
    if sam and mec:
        return 'P14'


for lii in lineList:
    s = check(lii)
    print(s)
