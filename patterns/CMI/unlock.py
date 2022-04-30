#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 3:18 PM
#@Author : Shao
#@File : unlock.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_).lower() == 'unlock':
            for child in token.children:
                if str(child.dep_) == 'neg':
                    return 4
