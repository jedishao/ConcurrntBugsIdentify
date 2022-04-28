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

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    cmi, exc = False, False
    # for token in doc:
    #     if str(token.dep_) == 'ROOT':
    #         for child in token.children:
    #             if str(child.dep_) == 'advcl':
    #                 for grandchild in child.children:
    #
for lii in lineList:
    s = check(lii)
    print(s)
