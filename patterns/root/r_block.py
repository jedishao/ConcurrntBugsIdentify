#-*- codeing = utf-8 -*-
#@Time : 4/27/2022 9:09 PM
#@Author : Shao
#@File : r_block.py
#@Software : PyCharm

# RLock trylock blocks forever.
# When tryLock is called with 0 wait time, the thread blocks forever.
# CommandAsyncService blocks indefinitely.
# But if for any reason connection is not established yet the calling thread will be blocked.
# loop lock blocked when master-slave failover.
# all application threads are blocked with stack trace.
# threads blocked waiting on CountDownLatch.
# When you try to fetch that object by using RedissonMap.get() call, deserialization of object will fail in MapOutput because of missing appropriate constructor and thread calling RedissonMap.get() will block forever.
# RedissonAtomicLong.get blocks indefinitely.
# RMapCache get operation will be blocked.
# RedissonFairLock blocks indefinitely after threadWaitTimeExpiry.
# And if redis server is not available at all it will be blocked for very long period of time.
# The program will be blocked with the callstack I pasted.
# org.redisson.RedissonTopic.removeAllListeners got blocked on CountDownLatch.await.
# CommandAsyncService gets blocked at high concurrency.
# but it blocks indefinitely instead of the remaining time until a new permit becomes available.
# CommandAsyncService blocks indefinitely [without OutOfMemoryError].
# RMapCache get operation will be blocked.

import spacy

import corpus

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    sym, cmi = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.S:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
                elif str(child.dep_) == 'auxpass':
                    return 'P44'
                elif str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.adv:
                            if str(grandchild.lemma_) in corpus.TMP:
                                sym = True
    if cmi:
        if sym:
            return 'P41'
        else:
            return 'P42'
    if sym:
        return 'P43'


for lii in lineList:
    s = check(lii)
    print(s)
