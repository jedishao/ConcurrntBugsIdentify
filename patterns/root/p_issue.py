# @Time    : 4/25/22 5:19 PM
# @Author  : Shuai S
# @File    : p_issue.py
import spacy

import corpus

# Use issues---lock.
# Concurrency Issues.
# Issue in locking on key in concurrency.
# Rlock performance issue.
# RedissonRedLock issue.

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
                if str(child.dep_) == 'compound':
                    if str(child.lemma_).lower() in corpus.STE:
                        return 'P27'
                    elif str(child.lemma_) in corpus.MEC:
                        return 'P28'
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 'P29'
                elif str(child.dep_) == 'appos':
                    if str(child.lemma_).lower() in corpus.STE:
                        return 'P30'
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.comp:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P31'


for lii in lineList:
    s = check(lii)
    print(s)
