# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 3:46 PM
# @Author : Shao
# @File : r_acquire.py
# @Software : PyCharm
import spacy

import corpus


def check(nlp, line):
    doc = nlp(line)
    obj, cmi = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_).lower() in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.obj:
                    if str(child.lemma_).lower() in corpus.MEC:
                        obj = True
                elif str(child.dep_) == 'agent':
                    for grandchild in child.children:
                        if str(grandchild.lemma_).lower() in corpus.MEC:
                            obj = True
    if obj:
        return 20
    if cmi:
        return 21
