#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 8:29 PM
#@Author : Shao
#@File : n_condition.py
#@Software : PyCharm


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'condition':
            for child in token.children:
                if str(child.dep_) == 'compound':
                    if str(child.lemma_) == 'race':
                        return 7
