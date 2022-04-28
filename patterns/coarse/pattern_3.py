# @Time    : 4/3/22 1:43 PM
# @Author  : Shuai S
# @File    : pattern_3.py
import re

import corpus


def check(nlp, dataset):
    for line in dataset:
        cmi, adv, neg1, neg2, neg3, ter, cop = False, False, False, False, False, False, False
        doc = nlp(line)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) in ['work', 'unlock']:
                    for child in token.children:
                        if str(child) == 'CMI' and str(child.dep_) in corpus.s:
                            cmi = True
                        if str(child.lemma_) == 'not' and str(child.dep_) == 'neg':
                            neg1 = True
                else:
                    # CMI is not reentrant.
                    # CMI cannot be correctly unlocked.
                    for child in token.children:
                        if str(child) == 'CMI' and str(child.dep_) in corpus.s:
                            cmi = True
                        if str(child.lemma_) == 'not' and str(child.dep_) == 'neg':
                            neg2 = True
                        if str(child.lemma_) in ['correctly', 'properly']:
                            if str(child.dep_) in corpus.adv:
                                adv = True
                        if re.search('comp', str(child.dep_)):
                            if str(child.lemma_).lower() in corpus.COP:
                                cop = True
                            else:
                                for grandchild in child.children:
                                    if str(grandchild.lemma_) == 'not' and str(grandchild.dep_) == 'neg':
                                        neg3 = True
                                    elif str(grandchild.lemma_) in corpus.TER and str(grandchild.dep_) == 'attr':
                                        ter = True
        if cmi:
            if neg1:
                return True
            if neg2:
                if ter or adv:
                    return True
                if cop:
                    return True
        if neg3 and ter:
            return True
    return False
