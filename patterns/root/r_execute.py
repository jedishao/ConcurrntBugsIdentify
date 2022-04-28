# @Time    : 4/28/22 2:47 PM
# @Author  : Shuai S
# @File    : r_execute.py

import spacy

import corpus

# redission ScheduledFuture can not be execute after definite time.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, neg = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) == 'neg':
                    neg = True
    if cmi and neg:
        return 'P64'


for lii in lineList:
    s = check(lii)
    print(s)
