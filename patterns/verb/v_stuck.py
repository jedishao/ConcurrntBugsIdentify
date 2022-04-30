# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 5:34 PM
# @Author : Shao
# @File : v_stuck.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_).lower() in ['stuck', 'stick']:
            for child in token.children:
                if str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        return 121
