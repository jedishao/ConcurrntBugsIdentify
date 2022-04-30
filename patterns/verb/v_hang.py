# @Time    : 4/28/22 2:10 PM
# @Author  : Shuai S
# @File    : v_hang.py
import spacy

import corpus

# Bug found that can cause MasterSlaveConnectionManager to hang forever on get() call if exception is thrown anywhere in CommandHandler.


def check(nlp, line):
    doc = nlp(line)
    sym, cmi = False, False
    for token in doc:
        if str(token.lemma_) == 'hang':
            for child in token.children:
                if str(child.lemma_) in corpus.MEC:
                    cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
    if cmi:
        if sym:
            return 112
        else:
            return 113
