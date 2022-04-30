# @Time    : 4/27/22 2:50 PM
# @Author  : Shuai S
# @File    : v_block.py
import spacy

import corpus

# This is causing calling thread to block forever in MasterSlaveConnectionManager.get() method.


def check(nlp, line):
    doc = nlp(line)
    sym, cmi = False, False
    for token in doc:
        if str(token.lemma_) == 'block':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            print(grandchild)
                            if str(grandchild.lemma_) in corpus.MEC:
                                cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
    if cmi:
        if sym:
            return 107
        else:
            return 108
    if sym:
        return 109
