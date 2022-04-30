# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 5:54 PM
# @Author : Shao
# @File : infinite.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_).lower() == 'infinite':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) in corpus.MEC:
                        return 2
