# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 5:45 PM
# @Author : Shao
# @File : v_lock.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    cmi, exc, sym = False, False, False
    for token in doc:
        if str(token.lemma_) == 'lock':
            cmi = True
            for child in token.children:
                if str(child.dep) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
        elif str(token.lemma_) in corpus.BAD:
            exc = True
    if cmi:
        if exc:
            return 116
        elif sym:
            return 117
