# @Time    : 4/28/22 2:13 PM
# @Author  : Shuai S
# @File    : n_lock.py
import spacy

import corpus

# I've found my indefinitely held locks will sometimes disappear after a master/slave failover.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'lock':
            for child in token.children:
                if str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.SYMP:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.adv:
                                if str(grandchild.lemma_) in corpus.TMP:
                                    return 17
                    elif str(child.lemma_) in corpus.TMP:
                        return 18