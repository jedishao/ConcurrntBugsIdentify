# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 6:27 PM
# @Author : Shao
# @File : v_release.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_).lower() == 'release':
            for child in token.children:
                if str(child.dep_) == 'neg':
                    return 120
