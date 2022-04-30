# -*- codeing = utf-8 -*-
# @Time : 4/28/2022 11:28 PM
# @Author : Shao
# @File : n_exception.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) in corpus.MEC:
            return 13
