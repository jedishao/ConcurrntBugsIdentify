# @Time    : 4/28/22 4:44 PM
# @Author  : Shuai S
# @File    : r_fail.py

import spacy

import corpus

# The second thread failed to acquire lock but the lock is released during 2 seconds...please tell me, thanks
# redisson failed to acquire lock and keep sending acquire lock request.
# But if we block node1's network then it fails with the below error.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) in corpus.comp:
                    if str(child.lemma_) in corpus.COP:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.obj:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    return 54
                elif str(child.dep_) == 'advcl':
                    if str(child.lemma_) in corpus.COP:
                        return 55
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.COP:
                        return 56

