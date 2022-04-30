#-*- codeing = utf-8 -*-
#@Time : 4/28/2022 12:17 AM
#@Author : Shao
#@File : r_hang.py
#@Software : PyCharm

# PyCharmConnectionManager call hangs forever if exception is thrown during Command processing.
# Redisson shutdown hangs if redis server was down.
# Redisson hang on RBatch.execute().
# Read thread finishes executing properly, write thread hangs forever.
# Write thread hangs until the read thread finishes and then locks and finishes.
# Many threads are hanging indefinitely in the CommandAsyncService.get() method.
# Thread hangs indefinitely at the request.
# tryLock() method is hanging forever.
# RLock.isLocked() get hung when I disable/enable my local network.
# RLock.isLocked() got hung forever with callstack as following
# CMI and CMI of CMI object get hang.

import spacy

import corpus


def check(nlp, line):
    doc = nlp(line)
    cmi, sym = False, False
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.dep_) == 'prep':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.obj:
                            if str(grandchild.lemma_) in corpus.MEC:
                                cmi = True
                elif str(child.dep_) in corpus.s:
                    if str(child.lemma_) in corpus.MEC:
                        cmi = True
                    else:
                        for grandchild in child.children:
                            if str(grandchild.dep_) in corpus.obj:
                                if str(grandchild.lemma_) in corpus.MEC:
                                    cmi = True
                elif str(child.dep_) in corpus.adv:
                    if str(child.lemma_) in corpus.TMP:
                        sym = True
                elif str(child.dep_) == 'aux':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.s:
                            if str(grandchild.lemma_) in corpus.MEC:
                                cmi = True
    if cmi:
        if sym:
            return 62
        else:
            return 63
