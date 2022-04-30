#-*- codeing = utf-8 -*-
#@Time : 4/28/2022 10:53 PM
#@Author : Shao
#@File : r_stuck.py
#@Software : PyCharm
import corpus

# CMI stuck.
# If more than 3 locks are supplied to RedissonRedLock or RedissonMultiLock instance then lock method could stuck.

def check(nlp, line):
    doc = nlp(line)
    neg, mec = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        return 89
