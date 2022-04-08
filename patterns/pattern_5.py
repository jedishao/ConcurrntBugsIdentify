# @Time    : 4/5/22 3:07 PM
# @Author  : Shuai S
# @File    : pattern_5.py
import re

import corpus


def check(nlp, dataset):
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_).lower() in corpus.ISS:
                    for child in token.children:
                        if str(child) == 'CMI':
                            return True
                        elif str(child.dep_) == 'compound':
                            for grandchild in child.children:
                                if str(grandchild) == 'CMI':
                                    return True
                        elif str(child.dep_) == 'prep':
                            for grandchild in child.children:
                                if str(grandchild) == 'CMI':
                                    return True
                else:
                    for child in token.children:
                        if str(child) == 'CMI':
                            return True
                        elif str(child.lemma_).lower() in corpus.ISS:
                            for grandchild in child.children:
                                if str(grandchild.lemma_).lower() in corpus.COB:
                                    return True
                        elif str(child.dep_) == 'compound':
                            if str(child) == 'CMI':
                                for grandchild in child.children:
                                    if str(grandchild.lemma_).lower() in corpus.ISS:
                                        return True
    return False
