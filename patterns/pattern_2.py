# @Time    : 4/3/22 1:42 PM
# @Author  : Shuai S
# @File    : pattern_2.py
import corpus


def check(nlp, dataset):
    for line in dataset:
        doc = nlp(line)
        for token in doc:
            # constraint (race condition)
            if str(token.lemma_) == 'race':
                if str(token.head) == 'condition':
                    return True
            if str(token.lemma_) == 'deadlock':
                return True
    return False


def constraint(doc):
    print()

