# @Time    : 4/5/22 8:22 PM
# @Author  : Shuai S
# @File    : pattern_7.py


def check(nlp, dataset):
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            if str(token.lemma_) == 'break':
                return True
    return False
