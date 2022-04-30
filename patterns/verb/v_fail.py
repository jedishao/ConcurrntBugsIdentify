#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 6:20 PM
#@Author : Shao
#@File : v_fail.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    sym, cmi = False, False
    for token in doc:
        if str(token.lemma_) == 'fail':
            for child in token.children:
                if str(child.lemma_) in corpus.MEC:
                    return 111
