# @Time    : 4/28/22 2:35 PM
# @Author  : Shuai S
# @File    : v_await.py
import spacy

import corpus

# In more details, this is happening because get() method awaits forever on Future object, which is released when Command.complete() is called.
te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, sym = False, False
    for token in doc:
        if str(token.lemma_) == 'await':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
    if cmi:
        if sym:
            return 'P63'


for lii in lineList:
    s = check(lii)
    print(s)
