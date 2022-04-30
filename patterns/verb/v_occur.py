# @Time    : 4/28/22 1:59 PM
# @Author  : Shuai S
# @File    : v_occur.py
import spacy

import corpus

# The task can run on the same thread due to reentrant lock feature, but when the task runs on another thread a deadlock occurs.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'occur':
            for child in token.children:
                if str(child.dep_) in corpus.s:
                    if str(child.lemma_) == 'deadlock':
                        return 118
