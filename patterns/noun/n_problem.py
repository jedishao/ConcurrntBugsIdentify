# @Time    : 4/28/22 1:55 PM
# @Author  : Shuai S
# @File    : n_problem.py
import spacy

import corpus

# I run into a thread deadlock problem when using distributed lock on 1.2.1.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'problem':
            for child in token.children:
                if str(child.dep_) == 'compound':
                    if str(child.lemma_) in corpus.STE:
                        return 'P58'


for lii in lineList:
    s = check(lii)
    print(s)
