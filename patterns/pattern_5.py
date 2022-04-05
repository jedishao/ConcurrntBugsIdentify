# @Time    : 4/5/22 3:07 PM
# @Author  : Shuai S
# @File    : pattern_5.py
import corpus


def check(nlp, dataset):
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) in corpus.ISS:
                    for child in token.children:
                        if str(child) == 'CMI':
                            return True
                        elif str(child.dep_) == 'compound':
                            for grandchild in child.children:
                                if str(grandchild) == 'CMI':
                                    return True
    return False
