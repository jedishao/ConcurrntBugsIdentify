# @Time    : 4/28/22 1:59 PM
# @Author  : Shuai S
# @File    : v_occur.py
import spacy

import corpus

# The task can run on the same thread due to reentrant lock feature, but when the task runs on another thread a deadlock occurs.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'occur':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) == 'deadlock':
                        return 'P59'


for lii in lineList:
    s = check(lii)
    print(s)
