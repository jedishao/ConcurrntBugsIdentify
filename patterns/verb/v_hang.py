# @Time    : 4/28/22 2:10 PM
# @Author  : Shuai S
# @File    : v_hang.py
import spacy

import corpus

# Bug found that can cause MasterSlaveConnectionManager to hang forever on get() call if exception is thrown anywhere in CommandHandler.

te = open('../test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
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
            return 'P60'
        # else:
        #     return 'P53'


for lii in lineList:
    s = check(lii)
    print(s)
