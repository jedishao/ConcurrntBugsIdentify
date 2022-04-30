# @Time    : 4/28/22 4:02 PM
# @Author  : Shuai S
# @File    : v_break.py
import spacy

import corpus

# Hi, we have been using RedissonSortedSet and just found that on certain cases the order can be broken and I assume RedissonSortedSet is supposedly thread safe.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'break':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) == 'order':
                        return 110
