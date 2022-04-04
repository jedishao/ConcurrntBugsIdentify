# @Time    : 4/3/22 1:43 PM
# @Author  : Shuai S
# @File    : pattern_3.py
import corpus


def check(nlp, dataset):
    for line in dataset:
        cmi, neg = False, False
        doc = nlp(line)
        for token in doc:
            # constraint (race condition)
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) == 'work':
                    for child in token.children:
                        # print(str(child)+'--->'+str(child.dep_))
                        # if str(child) == 'CMI' and str(child.dep_) in corpus.S:
                        #     cmi = True
                        if str(child.lemma_) == 'not' and str(child.dep_) == 'neg':
                            neg = True
        if neg and cmi:
            return True
    return False
