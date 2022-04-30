# -*- codeing = utf-8 -*-
# @Time : 4/29/2022 2:52 PM
# @Author : Shao
# @File : r_condition.py
# @Software : PyCharm
import corpus


def check(nlp, line):
    doc = nlp(line)
    race, cmi = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                cmi = True
                            else:
                                for sgrandchild in grandchild.children:
                                    if str(sgrandchild.dep_) == 'compound':
                                        if str(sgrandchild.lemma_) in corpus.MEC:
                                            cmi = True
                elif str(child.dep_) == 'compound':
                    if str(child.lemma_) == 'race':
                        race = True
    if race:
        if cmi:
            return 39
        else:
            return 40
