#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 12:30 AM
#@Author : Shao
#@File : n_fail.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) in corpus.COP:
            return 14
