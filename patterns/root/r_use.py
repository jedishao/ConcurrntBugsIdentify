# @Time    : 4/28/22 3:13 PM
# @Author  : Shuai S
# @File    : r_use.py
import spacy

import corpus

#The take() method in RedissonBlockingQueue uses Future.getNow(), which returns null if an exception occurs.
# When I am using two threads to put values through redisson to different database with limited memory(maxmemory-policy :volatile-lru, maxmemory:4MB),  error like org.redisson.client.RedisOutOfMemoryException:
# Deadlock using RedissonMultiLock.
# While using RedissonMultiLock with 3 locks both clients blocks.
# I am using reddison Rlock with a cluster setup , and sometimes I see latency when trying to acquire the lock or unlock.
# Hi, we have been using RedissonSortedSet and just found that on certain cases the order can be broken and I assume RedissonSortedSet is supposedly thread safe.
# I'm using RLock and seeing memory leak via org.redisson.client.handler.CommandPubSubDecoder.
# I'm using RxJava and as a part of the sequence I use a RLock, at some point (in another process) I unlock it and if the thread to unlock is not the same as the one that blocked I get an exception (see below).
# when use lock, but throw some class cast exception.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, exc, sym = False, False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.obj:
                                if str(grandchild.lemma_) in corpus.BAD:
                                    exc = True
    if cmi and exc:
        return 'P68'


for lii in lineList:
    s = check(lii)
    print(s)

