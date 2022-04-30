# @Time    : 4/23/22 8:58 PM
# @Author  : Shuai S
# @File    : r_obtain.py
import spacy

import corpus
# The same lock name was likely concurrently obtained and held by another thread possibly on another jvm.


def check(nlp, line):
    doc = nlp(line)
    sam, mec = False, False
    for token in doc:
        if str(token.lemma_) == 'same':
            sam = True
        elif str(token.lemma_) in corpus.MEC:
            mec = True
    if sam and mec:
        return 81

