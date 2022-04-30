# @Time    : 4/25/22 8:29 PM
# @Author  : Shuai S
# @File    : v_hold.py

import spacy
import corpus

# This is prone to issues where it never gets destroyed and a lock is held forever.
# RedissonRedLock trylock success while another thread already hold the lock in specific conditions.


def check(nlp, line):
    doc = nlp(line)
    cmi, tmp = False, False
    for token in doc:
        if str(token.pos_) == 'VERB':
            if str(token.lemma_) == 'hold':
                for child in token.children:
                    if str(child.dep_) in corpus.s:
                        if str(child.lemma_) in corpus.MEC:
                            cmi = True
                    elif str(child.dep_) in corpus.adv:
                        if str(child.lemma_) in corpus.TMP:
                            tmp = True
    if cmi and tmp:
        return 115
