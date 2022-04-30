#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 12:59 AM
#@Author : Shao
#@File : n_error.py
#@Software : PyCharm

import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) in corpus.MEC:
            return 12
