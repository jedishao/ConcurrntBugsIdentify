# @Time    : 4/25/22 5:38 PM
# @Author  : Shuai S
# @File    : r_be.py
import spacy

import corpus

# some threads will be deadlock.
# Read Write lock cannot be correctly unlocked.
# the Read and Write lock cannot be correctly unlocked.
# There is a race condition where Redisson may throw RedisTimeoutException after retryInterval has exceeded but before timeout has exceeded.
# RReadWriteLock is not reentrant.
# RReadWriteLock is incompatible with reentry r&w op.
# URIBuilder is not thsa.
# Race-condition during ack checking is possible.

def check(nlp, line):
    doc = nlp(line)
    sbj, sym, unlock, fea, neg = False, False, False, False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        sbj = True
                    elif str(child.lemma_) == 'condition':
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) == 'race':
                                    return 22
                elif str(child.dep_) == 'attr':
                    if str(child.lemma_) in corpus.SYMP:
                        sym = True
                    elif str(child.lemma_) == 'condition':
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) == 'race':
                                    return 23
                    elif str(child.lemma_) == 'dump':
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_).lower() == 'thread':
                                    return 24
                    elif str(child.lemma_) in ['thsa']:
                        fea = True
                    elif str(child.lemma_) in corpus.BAD:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'prep':
                                for sgrandchild in grandchild.children:
                                    if str(sgrandchild.dep_) in corpus.obj:
                                        if str(sgrandchild.lemma_) in corpus.STE:
                                            return 25
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'prep':
                                for sgrandchild in grandchild.children:
                                    if str(sgrandchild.dep_) in corpus.obj:
                                        if str(sgrandchild.lemma_) == 'condition':
                                            for ssgrandchild in sgrandchild.children:
                                                if str(ssgrandchild.lemma_) == 'race':
                                                    return 26

                elif str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.ULO:
                        unlock = True
                    elif str(child.lemma_) in ['reentrant', 'incompatible']:
                        fea = True
                    elif str(child.lemma_) in corpus.SYMP:
                        sym = True
                elif str(child.dep_) == 'advcl':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.s:
                            if str(grandchild.lemma_) in corpus.MEC:
                                sbj = True
                elif str(child.dep_) == 'neg':
                    neg = True
    if sbj:
        if sym:
            return 27
        elif unlock:
            return 28
    if fea:
        if neg:
            return 29
        elif sbj:
            return 30
