#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 1:47 AM
#@Author : Shao
#@File : n_dump.py
#@Software : PyCharm

import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'dump':
            for child in token.children:
                if str(child.dep_) == 'compound':
                    if str(child.lemma_) == 'thread':
                        return 11
