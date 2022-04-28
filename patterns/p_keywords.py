# @Time    : 4/23/22 8:12 PM
# @Author  : Shuai S
# @File    : p_keywords.py
import spacy

import corpus

# But while running a apache ab-test tool for concurrency, following exception occurs.

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    mec, ste, exc = False, False, False
    for token in doc:
        if str(token.lemma_) in corpus.MEC:
            mec = True
        elif str(token) == 'exception':
            exc = True
        elif str(token.lemma_) in corpus.STE:
            ste = True
    if exc:
        if mec:
            return 'p100'
        elif ste:
            return 'P101'


for lii in lineList:
    s = check(lii)
    print(s)
