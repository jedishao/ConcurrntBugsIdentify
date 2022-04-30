# @Time    : 4/28/22 3:26 PM
# @Author  : Shuai S
# @File    : n_deadlock.py
import spacy

import corpus

# Deadlock using RedissonMultiLock.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'deadlock':
            for child in token.children:
                if str(child.dep_) == 'acl':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 8
                elif str(child.dep_) == 'prep':
                    return 9
    for token in doc:
        if str(token.lemma_) in corpus.MEC:
            return 10
