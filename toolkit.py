# list1 = [3, 6, 10, 16, 41, 51, 53, 61, 67, 69, 70, 72, 74, 76, 85, 86, 88, 94, 95, 99]
# list1_copy = [3, 6, 10, 16, 41, 51, 53, 61, 67, 69, 70, 72, 74, 76, 85, 86, 88, 94, 95, 99]
# list2 = [3, 6, 51, 53, 61, 67, 69, 70, 72, 74, 76, 85, 86, 88, 94, 95, 99]
#
# for i in list1:
#     if list2.__contains__(i):
#         list1_copy.remove(i)
#
# k = 0
# for j in list2:
#     list2[k] = j + 1
#     k += 1
# print(list2)
import ast
import spacy

import corpus

target = open("results/only_one_cmi.txt", 'r')
# con = open("results/deadlockSents_NER.txt", 'r')
# results = open("results/only_one_cmi.txt", 'w')

index = []
sents = []
re = []
# for lines in con:
#     re.append(str(lines))
nlp = spacy.load("en_core_web_sm")
for line in target:
    sents.append(line)

# for sen in sents:
#     flag = False
#     doc = nlp(sen)
#     for token in doc:
#         if str(token) == 'CMI':
#             print(str(token.dep_))
#             if str(token.dep_) == 'nsubj' or str(token.dep_) == 'nsubjpass':
#                 flag = True
#     if flag:
#         index.append(sen)

for sen in sents:
    doc = nlp(sen)
    for token in doc:
        if str(token.dep_) == 'ROOT':
            print(str(token))

print('===============================================================================')
# for s in index:
#     print(s, end='')

sentences = ['CMI is currently a blocking operation.']
CVAS_set = []
# for sents in sentences:
#     flag = True
#     cmi, cop, tmp, symp = 0, 0, 0, 0
#     doc = nlp(sents)
#     for token in doc:
#         print(token.lemma_)
#         if str(token) == 'CMI':
#             print('a')
#             cmi += 1
#         elif str(token.lemma_) in corpus.COP:
#             print('b')
#             cop += 1
#         elif str(token.lemma_) in corpus.TMP:
#             print('c')
#             tmp += 1
#         elif str(token.lemma_) in corpus.SYMP:
#             print('d')
#             symp += 1
#     if cmi == 1 and cop > 0 and tmp > 0:
#         CVAS_set.append(sents)
#         flag = False
#     if cmi == 1 and cop > 0 and symp > 0 and flag:
#         CVAS_set.append(sents)

for sents in sentences:
    doc = nlp(sents)
    for d in doc:
        if str(d.dep_) == 'ROOT':
            for c in d.children:
                if str(c.dep_) == 'attr':
                    print(c)

for c in CVAS_set:
    print(c)
