# @Time    : 4/28/22 2:25 PM
# @Author  : Shuai S
# @File    : n_bug.py
import spacy

import corpus


# I've found something that I believe is a bug in Redisson's CMI implementation where multiple ReadLocks seemed to become or at least behaved like WriteLock when it tried to lock on a lockpoint that another WriteLock has already acquired a lock, then released.


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.lemma_) == 'bug':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 6
                            else:
                                for sgrandchild in grandchild.children:
                                    if str(sgrandchild.lemma_) in corpus.MEC:
                                        return 6
