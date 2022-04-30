# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 6:09 PM
# @Author : Shao
# @File : verb.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    neg, pos, no, cmi, sym, orde, brok, thsa = False, False, False, False, False, False, False, False
    for token in doc:
        if str(token.pos_) == 'VERB':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                    elif str(child.lemma_) in corpus.ULO:
                        cmi = True
                    elif str(child.lemma_) == 'order':
                        orde = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.POS:
                        pos = True
                    elif str(child.lemma_) in corpus.NEG:
                        neg = True
                    elif str(child.lemma_) in corpus.TMP:
                        sym = True
                elif str(child.dep_) == 'neg':
                    no = True
                elif str(child.dep_) == 'oprd':
                    brok = True
                elif str(child.dep_) in corpus.comp:
                    for grandchild in child.children:
                        if str(grandchild.dep_) == 'neg':
                            no = True
                        elif str(grandchild.dep_) == 'attr':
                            if str(grandchild.lemma_) in corpus.TER:
                                thsa = True
                elif str(child.dep_) in corpus.obj:
                    for grandchild in child.children:
                        if str(grandchild.lemma_) in corpus.MEC:
                            cmi = True
            if cmi:
                if neg:
                    return 125
                elif pos and no:
                    return 126
                elif pos:
                    return 127
                elif sym:
                    return 128
            if orde and brok:
                return 129
            if no and thsa:
                return 130
