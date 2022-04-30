#-*- codeing = utf-8 -*-
#@Time : 4/27/2022 10:29 PM
#@Author : Shao
#@File : v_have.py
#@Software : PyCharm
import spacy

import corpus

# RedissonList iterator as it tries to keep "up to date" with data has a race condition in which if between the .hasNext() and the .next() call the set is emptied the list will throw NoSuchElementException.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'have':
            for child in token.children:
                if str(child.dep_) in corpus.obj:
                    if str(child.lemma_) == 'condition':
                        for grandchild in child.children:
                            if str(grandchild.dep_) == 'compound':
                                if str(grandchild.lemma_) == 'race':
                                    return 114
