# @Time    : 4/23/22 9:13 PM
# @Author  : Shuai S
# @File    : r_race.py

import spacy

import corpus
# The same lock name was likely concurrently obtained and held by another thread possibly on another jvm.


def check(nlp, line):
    doc = nlp(line)
    sam, mec = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'amod':
                    if str(child.lemma_) in corpus.MEC:
                        return 87
