# @Time    : 4/28/22 4:20 PM
# @Author  : Shuai S
# @File    : r_release.py
import spacy

import corpus
# unlock not releasing lock to waiting threads.


def check(nlp, line):
    doc = nlp(line)
    neg, mec = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'neg':
                    neg = True
                elif str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.MEC:
                        mec = True
    if neg and mec:
        return 88
