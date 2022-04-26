# @Time    : 4/3/22 9:25 PM
# @Author  : Shuai S
# @File    : pattern_4.py


# [CMI][COP]([TMP]+[SYMP])
import re

import corpus


# when thread is interrupt all Reference variables is locked
def check(nlp, dataset):
    ste, sym, kw = False, False, False
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            # constraint (asy)
            if str(token.lemma_) in corpus.STE:
                kw = True
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) in corpus.SYMP or str(token) == 'locked':
                    # [CMI][COP]([TMP]+[SYMP])
                    flag, ste = pattern4_1(token)
                    if flag:
                        return True
                elif str(token.lemma_) in corpus.OTHER:
                    if pattern4_2(token):
                        return True
        if ste and kw:
            return True
    return False


def pattern4_1(token):
    flag, ste, sym = False, False, False
    for child in token.children:
        # subject
        if str(child.dep_) in corpus.S:
            # [CMI]-->
            if str(child) == 'CMI':
                flag = True
                return flag, ste
            elif str(child.lemma_) in corpus.STE:
                sym = True
            else:
                for grandchild in child.children:
                    if str(grandchild) == 'CMI':
                        flag = True
                        return flag, ste
        elif str(child.dep_) in corpus.adv:  # adv
            # [STE][COP][TMP]
            if str(child.lemma_) in corpus.TMP:
                ste = True
        elif str(child.dep_) == 'conj':  # conjunction
            if str(child.lemma_) in corpus.SYMP:
                flag = True
                return flag, ste
    if sym and ste:
        flag = True
        return flag, ste
    return flag, ste


# CMI makes the thread waiting forever
def pattern4_2(token):
    # make
    cmi, th, adv = False, False, False
    for child in token.children:
        if str(child) == 'CMI':
            cmi = True
            # if str(child.dep_) == 'comp'
        if re.search('comp', str(child.dep_)):  # complement
            if str(child.lemma_) in corpus.COP:
                for grandchild in child.children:
                    if str(grandchild.lemma_) in corpus.TMP and str(grandchild.dep_) in corpus.adv:
                        adv = True
                    elif str(grandchild.lemma_) in corpus.STE and str(grandchild.dep_) in corpus.S:
                        th = True
                    elif str(grandchild.lemma_) in corpus.COP and re.search('comp', str(child.dep_)):  # 101
                        return True
    if cmi and adv and th:
        return True
    return False
