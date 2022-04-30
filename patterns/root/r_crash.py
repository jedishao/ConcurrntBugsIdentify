# @Time    : 4/28/22 2:59 PM
# @Author  : Shuai S
# @File    : r_crash.py
import spacy

import corpus

# I was crashed into a blocking issue when I was doing some configuration on my windows laptop.
# JVM crashes when using 1000 concurrent redisson threads.
# Cluster nodes synchronization crashes (never scheduled again) with IllegalArgumentException while processing slave nodes.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.BAD:
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.lemma_) in corpus.MEC:
                                    return 41
                elif str(child.dep_) == 'advcl':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            return 42
                elif str(child.dep_) == 'compound':
                    if str(child.lemma_) in corpus.STE:
                        return 43
