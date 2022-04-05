# @Time    : 4/3/22 1:43 PM
# @Author  : Shuai S
# @File    : pattern_3.py
import corpus


def check(nlp, dataset):
    for line in dataset:
        cmi, adv, neg1, neg2 = False, False, False, False
        doc = nlp(line)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) in ['work', 'unlock']:
                    for child in token.children:
                        # print(str(child)+'--->'+str(child.dep_))
                        if str(child) == 'CMI' and str(child.dep_) in corpus.S:
                            cmi = True
                        if str(child.lemma_) == 'not' and str(child.dep_) == 'neg':
                            neg1 = True
                else:
                    for child in token.children:
                        # print(str(child)+'--->'+str(child.dep_))
                        if str(child) == 'CMI' and str(child.dep_) in corpus.S:
                            cmi = True
                        if str(child.lemma_) == 'not' and str(child.dep_) == 'neg':
                            neg2 = True
                        if str(child.lemma_) in ['correctly', 'properly'] and str(child.dep_) in corpus.ADV:
                            adv = True
        if cmi:
            if neg1:
                return True
            if neg2 and adv:
                return True
    return False
