# @Time    : 4/23/22 4:55 PM
# @Author  : Shuai S
# @File    : p_try.py
import spacy

# I am trying to use redisson for distributed locks.
# I'm trying to use Lock and Unlock on Jersey Resource.
import corpus

te = open('test.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for li in te:
    lineList.append(li)


def check(line):
    doc = nlp(line)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for child in token.children:
                if str(child.pos_) == 'VERB':
                    for grandchild in child.children:
                        if str(grandchild.dep_) in corpus.OBJ:
                            if str(grandchild.lemma_) in corpus.MEC:
                                return 'P1'
                        elif str(grandchild.dep_) == 'prep':
                            for sgrandchild in grandchild.children:
                                if str(sgrandchild.lemma_) in corpus.MEC:
                                    return 'P2'


for lii in lineList:
    s = check(lii)
    print(s)
