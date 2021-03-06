# @Time    : 4/23/22 5:39 PM
# @Author  : Shuai S
# @File    : r_work.py
import spacy

# but when i make these MEC from different Threads it does not works.
# RLock did not work.
# ReadLock not working correctly.
# ReadWriteLock not working.
# `redissonClient.getRedLock` does not work well with Read-Write block in a multi-JVM environment.
# ElasticacheCluster not working correctly with DistributedLocks.
# The RedissonMultiLock works fine if all the redis nodes are alive.
# ReadWriteLock timeout does not work as expected.
# Same scenario works as expected when there is no exception or error inside the try block.


import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'neg':
                    for child1 in token.children:
                        if str(child1.dep_) == 'advcl':
                            for grandchild in child1.children:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 96
                        elif str(child1.dep_) in corpus.s:
                            if str(child1.lemma_) in corpus.MEC:
                                return 97
                            else:
                                for grandchild in child1.children:
                                    if str(grandchild.lemma_) in corpus.MEC:
                                        return 98
                        elif str(child1.dep_) == 'prep':
                            for grandchild in child1.children:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 99
