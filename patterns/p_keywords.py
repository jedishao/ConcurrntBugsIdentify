# @Time    : 4/23/22 8:12 PM
# @Author  : Shuai S
# @File    : p_keywords.py
import spacy

import corpus

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    mec, symp, exc = False, False, False
    for token in doc:
        if str(token) in corpus.MEC:
            mec = True
        elif str(token) == 'exception':
            exc = True
    if mec and exc:
        return 'p100'
