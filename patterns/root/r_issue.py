# @Time    : 4/25/22 5:19 PM
# @Author  : Shuai S
# @File    : r_issue.py
import spacy

import corpus

# Use issues---lock.
# Concurrency Issues.
# Issue in locking on key in concurrency.
# Rlock performance issue.
# RedissonRedLock issue.
# CMI deadlock issue.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'compound':
                    if str(child.lemma_).lower() in corpus.STE:
                        return 70
                    elif str(child.lemma_) in corpus.MEC:
                        return 71
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 72
                elif str(child.dep_) == 'appos':
                    if str(child.lemma_).lower() in corpus.STE:
                        return 73
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.comp:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 74

