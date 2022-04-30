# @Time    : 4/25/22 8:45 PM
# @Author  : Shuai S
# @File    : cmi.py
import spacy

import corpus

# there is a lock name CMI which doesn't release.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token) == 'CMI':
            for child in token.children:
                if str(child.lemma_) == 'release':
                    for grandchild in child.children:
                        if str(grandchild.dep_) == 'neg':
                            return 0
                elif str(child.dep_) == 'compound':
                    if str(child.lemma_).lower() in corpus.NEG:
                        return 1
