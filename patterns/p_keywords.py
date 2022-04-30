# @Time    : 4/23/22 8:12 PM
# @Author  : Shuai S
# @File    : p_keywords.py
import spacy

import corpus

# But while running a apache ab-test tool for concurrency, following exception occurs.


def check(nlp, line):
    doc = nlp(line)
    mec, ste, exc, ulo, cop, sym, tmp, thsa, non = False, False, False, False, False, False, False, False, False
    for token in doc:
        if str(token.lemma_) in corpus.MEC:
            mec = True
        if str(token.lemma_) in corpus.BAD:
            exc = True
        if str(token.lemma_).lower() in corpus.STE:
            ste = True
        if str(token.lemma_) in corpus.ULO:
            ulo = True
        if str(token.lemma_) in corpus.COP:
            cop = True
        if str(token.lemma_) in corpus.SYMP:
            sym = True
        if str(token.lemma_) in corpus.TMP:
            tmp = True
        if str(token.lemma_) == 'thsa':
            thsa = True
        if str(token.dep_) == 'neg':
            non = True
    if exc:
        if mec:
            return 131
        elif ste:
            return 132
        elif ulo:
            return 133
        if cop:
            return 134
    if sym:
        if tmp:
            return 135
        elif mec:
            return 136

    if thsa and non:
        return 137
