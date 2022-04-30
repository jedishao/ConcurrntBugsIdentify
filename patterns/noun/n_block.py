#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 3:05 PM
#@Author : Shao
#@File : n_block.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'block':
            for child in token.children:
                if str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        return 5
