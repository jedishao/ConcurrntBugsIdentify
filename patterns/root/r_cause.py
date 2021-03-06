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


def check(nlp, line):
    doc = nlp(line)
    cmi, exc = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.SYMP:
                        return 35
                    elif str(child.lemma_) == 'recursion':
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.adv:
                                if str(grandchild.lemma_) in corpus.TMP:
                                    return 36
                    elif str(child.lemma_) in corpus.BAD:
                        exc = True
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.SYMP:
                        for grandchild in child.children:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 37
    if cmi:
        if exc:
            return 38

