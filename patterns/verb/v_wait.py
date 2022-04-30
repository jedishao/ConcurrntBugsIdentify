# @Time    : 4/27/22 2:38 PM
# @Author  : Shuai S
# @File    : v_wait.py

import spacy

import corpus

# There is no timeout when waiting for the lock.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'wait':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            return 124
