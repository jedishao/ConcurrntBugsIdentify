# @Time    : 4/5/22 3:11 PM
# @Author  : Shuai S
# @File    : pattern_6.py
import corpus


def check(nlp, dataset):
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            if str(token.lemma_) in corpus.LOG:
                if str(token.pos_) == 'NOUN':
                    return True
    return False
