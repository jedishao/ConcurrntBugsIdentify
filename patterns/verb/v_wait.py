# @Time    : 4/27/22 2:38 PM
# @Author  : Shuai S
# @File    : v_wait.py

import spacy

import corpus

# There is no timeout when waiting for the lock.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sbj, sym, unlock, fea, neg = False, False, False, False, False
    for token in doc:
        if str(token.lemma_) == 'wait':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            return 'P41'


for lii in lineList:
    s = check(lii)
    print(s)
