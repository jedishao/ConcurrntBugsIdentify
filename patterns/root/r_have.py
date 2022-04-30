# @Time    : 4/25/22 4:33 PM
# @Author  : Shuai S
# @File    : r_have.py
import spacy
import corpus

# RedissonRedLock.tryLock(l) still have something wrong.
# I have 1 thread locked trying to release a lock.
# I have about 30 other threads locked awaiting for a lock (a different one from the one used by the previous thread).
# Hi,I have a thread stuck in the CommandAsyncService#get() indefinitely waiting for the CountdownLatch.
# CMI still have something wrong.
# In our use case, we can have hundreds of unique fair locks being acquired many times, usually for short periods of time (~1-2 seconds).
# RedissonSessionRepository topic listeners initialization has race condition.


def check(nlp, line):
    doc = nlp(line)
    wrong, cmi = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) == 'condition':
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) == 'race':
                                    return 64
                    if str(child.lemma_) in corpus.MEC:
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'acl':
                                if str(grandchild.lemma_) in corpus.SYMP:
                                    return 65
                        return 66
                    elif str(child.lemma_) in corpus.BAD:
                        wrong = True
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.adv:
                                if str(grandchild.lemma_) in corpus.BAD:
                                    wrong = True
                            elif str(grandchild.dep_) == 'prep':
                                for sgrandchild in grandchild.children:
                                    if str(sgrandchild.dep_) in corpus.obj:
                                        if str(sgrandchild.lemma_) in corpus.MEC:
                                            return 67
                elif str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.MEC:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.comp:
                                if str(grandchild.lemma_) in corpus.CONDI:
                                    return 68
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
    if cmi and wrong:
        return 69
