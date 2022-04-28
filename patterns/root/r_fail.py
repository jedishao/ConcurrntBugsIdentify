# @Time    : 4/28/22 4:44 PM
# @Author  : Shuai S
# @File    : r_fail.py

import spacy

import corpus

# The second thread failed to acquire lock but the lock is released during 2 seconds...please tell me, thanks


te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.COP:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.obj:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 'P76'


for lii in lineList:
    s = check(lii)
    print(s)

