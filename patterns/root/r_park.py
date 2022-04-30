#-*- codeing = utf-8 -*-
#@Time : 4/29/2022 3:30 PM
#@Author : Shao
#@File : r_park.py
#@Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    cmi, symp = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        symp = True
    if cmi:
        if symp:
            return 82
        else:
            return 83
