# @Time    : 4/28/22 1:20 PM
# @Author  : Shuai S
# @File    : r_cause.py

# Following scenario causes infinite recursion and StackOverflowException when someone tries to create new URL:URLBuilder.replaceURLFactory() - URLBuilder.
# This causes deadlock of all other threads trying to grab the lock and can ultimately bring down an application as threads build up.
# redission AtomicObject in debug + breakpoint mode cause a different result.
# LockWatchdogTimeout will cause the IllegalMonitorStateException.
# In particular, Scheduler threads cause serious problems.
# Spring Data Redis connection in multi mode may cause thread hang.

import spacy

import corpus

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, exc = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.SYMP:
                        return 'P54'
                    elif str(child.lemma_) == 'recursion':
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.adv:
                                if str(grandchild.lemma_) in corpus.TMP:
                                    return 'p55'
                    elif str(child.lemma_) in corpus.BAD:
                        exc = True
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.SYMP:
                        for grandchild in child.children:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P57'
    if cmi:
        if exc:
            return 'P56'

for lii in lineList:
    s = check(lii)
    print(s)
