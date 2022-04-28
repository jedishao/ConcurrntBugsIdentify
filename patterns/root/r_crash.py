# @Time    : 4/28/22 2:59 PM
# @Author  : Shuai S
# @File    : r_crash.py
import spacy

import corpus

# I was crashed into a blocking issue when I was doing some configuration on my windows laptop.

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
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.BAD:
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.lemma_) in corpus.MEC:
                                    return 'P65'


for lii in lineList:
    s = check(lii)
    print(s)

