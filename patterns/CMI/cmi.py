# @Time    : 4/25/22 8:45 PM
# @Author  : Shuai S
# @File    : cmi.py
import spacy

import corpus

# there is a lock name CMI which doesn't release.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token) == 'CMI':
            for child in token.children:
                if str(child.lemma_) == 'release':
                    for grandchild in child.children:
                        if str(grandchild.dep_) == 'neg':
                            return 'P41'


for lii in lineList:
    s = check(lii)
    print(s)


