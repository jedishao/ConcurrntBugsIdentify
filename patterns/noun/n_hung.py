#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 7:56 PM
#@Author : Shao
#@File : n_hung.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'hung':
            for child in token.children:
                if str(child.lemma_) in corpus.TMP:
                    return 15
