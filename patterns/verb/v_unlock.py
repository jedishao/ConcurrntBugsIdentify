# @Time    : 4/28/22 4:12 PM
# @Author  : Shuai S
# @File    : v_unlock.py

import spacy

import corpus

# I'm using RxJava and as a part of the sequence I use a RLock, at some point (in another process) I unlock it and if the thread to unlock is not the same as the one that blocked I get an exception (see below).


def check(nlp, line):
    doc = nlp(line)
    cmi, exc, sym = False, False, False
    for token in doc:
        if str(token.lemma_) == 'unlock':
            cmi = True
            for child in token.children:
                if str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
        elif str(token.lemma_) in corpus.BAD:
            exc = True
    if cmi:
        if exc:
            return 122
        elif sym:
            return 123
