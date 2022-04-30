# @Time    : 4/28/22 2:47 PM
# @Author  : Shuai S
# @File    : r_execute.py

import spacy

import corpus

# redission ScheduledFuture can not be execute after definite time.


def check(nlp, line):
    doc = nlp(line)
    cmi, neg = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) == 'neg':
                    neg = True
    if cmi and neg:
        return 53
