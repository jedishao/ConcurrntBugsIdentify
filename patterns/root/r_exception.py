#-*- codeing = utf-8 -*-
#@Time : 4/27/2022 11:20 PM
#@Author : Shao
#@File : r_exception.py
#@Software : PyCharm

# Exception when I use RLock with SerializationCodec.
# Rlock Exception in cluster mode.
# Exception in using RedissonMultiLock.
# RedisConnectionException in High Concurrence.
# StackOverflowException in URLBuilder.
# Unexpected exception while processing command while taking a lock on a key.
# RedisResponseTimeoutException at getLockedLock for read operation in "replicatedServersConfig".
# Exception when use RedissonRedLock + RedissonMultiLock.

import spacy

import corpus


def check(nlp, line):
    doc = nlp(line)
    cmi, exc = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'advcl':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 48
                        elif str(grandchild.dep_) == 'advcl':
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.dep_) in corpus.obj:
                                    if str(sgrandchild.lemma_) in corpus.MEC:
                                        return 48
                elif str(child.dep_) == 'compound':
                    if str(child.lemma_) in corpus.MEC:
                        return 49
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 50
                            elif str(grandchild.lemma_).lower() in corpus.STE:
                                return 51
                        elif str(grandchild.dep_) in corpus.comp:
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.dep_) in corpus.obj:
                                    if str(sgrandchild.lemma_) in corpus.MEC:
                                        return 52
