#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 1:22 AM
#@Author : Shao
#@File : n_issue.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_).lower() in corpus.STE:
            return 16
