# @Time    : 4/23/22 4:55 PM
# @Author  : Shuai S
# @File    : r_try.py
import spacy

# I am trying to use redisson for distributed locks.
# I'm trying to use Lock and Unlock on Jersey Resource.
import corpus


def check(nlp, line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.pos_) == 'VERB':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 91
                        elif str(grandchild.dep_) == 'prep':
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.lemma_) in corpus.MEC:
                                    return 92
