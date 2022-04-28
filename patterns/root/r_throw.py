#-*- codeing = utf-8 -*-
#@Time : 4/27/2022 10:21 PM
#@Author : Shao
#@File : r_throw.py
#@Software : PyCharm

# RLock.tryLock() thows Exception.org.redisson.client.RedisException:
# RLock throws java.lang.IllegalMonitorStateException in the thread where got the lock twice.
# If I shutdown one of the redis nodes, it will throw RedisConnectionException.
# tryLock method throw Exception.
# RedissonList iterator as it tries to keep "up to date" with data has a race condition in which if between the .hasNext() and the .next() call the set is emptied the list will throw NoSuchElementException.
# The unlock part throws the following exception even though they're all read locks.
# An exception is thrown and the lock is not unlocked.
# when aquire redisson lock, that throw redis response timeout sometimes.
# RBlockingQueue.take doesn't throw InterruptedException.
# RLock unlock always throw an exception what like 'not lock by current thread'.
# RedissonAtomicLong#getAndSet throws NullPointerException when value does not exist yet.
# Redisson throws RedisTimeoutException before timeout has exceeded.
# Redisson throws RedisTimeoutException after timeout has exceeded.


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
                if str(child.dep_) in corpus.S:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                    elif str(child) == 'Exception':
                        exc = True
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) in corpus.MEC:
                                    cmi = True
                elif str(child.dep_) in corpus.obj:
                    if str(child) in ['Exception', 'timeout']:
                        exc = True
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.S:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    cmi = True
    if cmi:
        if exc:
            return 'P44'


for lii in lineList:
    s = check(lii)
    print(s)
