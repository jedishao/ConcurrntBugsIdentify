# @Time    : 4/28/22 1:12 PM
# @Author  : Shuai S
# @File    : v_receive.py
import spacy

import corpus

# sometimes when a thread(that acquired it) tries to release the lock the thread receives Exception.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, exc = False, False
    for token in doc:
        if str(token.lemma_) == 'receive':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) == 'Exception':
                        exc = True
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
    if cmi:
        if exc:
            return 'P52'


for lii in lineList:
    s = check(lii)
    print(s)
