# @Time    : 4/28/22 12:51 PM
# @Author  : Shuai S
# @File    : r_problem.py

# Similar problem I have when I use CountDown.
# Problem with Rlock - unlock not releasing lock to waiting threads.
# RTransaction Unusual Locking Problem.
# Distlock Mutual exclusion problem?
# The problem: sometimes when a thread(that acquired it) tries to release the lock the thread receives IllegalMonitorStateException , which means that this lock is already released.

import spacy

import corpus

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, sym = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'relcl':
                    for grandchild in child.children:
                        if str(grandchild.dep_) == 'advcl':
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.lemma_) in corpus.MEC:
                                    return 'P49'
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P50'
                elif str(child.dep_) == 'compound':
                    if str(child.lemma_) in corpus.MEC:
                        return 'P51'


for lii in lineList:
    s = check(lii)
    print(s)
