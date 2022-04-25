# @Time    : 4/23/22 9:13 PM
# @Author  : Shuai S
# @File    : p_race.py

import spacy

import corpus
# The same lock name was likely concurrently obtained and held by another thread possibly on another jvm.

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sam, mec = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'amod':
                    if str(child.lemma_) in corpus.MEC:
                        return 'P15'


for lii in lineList:
    s = check(lii)
    print(s)
