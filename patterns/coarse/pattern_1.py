import ast
import corpus
import spacy
p = open('../train_patterns.txt')
lineList = []
nlp = spacy.load("en_core_web_sm")
for line in p:
    lineList.append(line)
i = 1
for data in lineList:
    doc = nlp(data)
    print(str(i), '---------')
    for token in doc:
        if str(token.dep_) == 'ROOT':
            print(token)
    i += 1

# def check(nlp, dataset):
#     for line in dataset:
#         doc = nlp(line)
#         for token in doc:
#             if str(token.lemma_) == 'asynchronous':
#                 return False
#         for token in doc:
#             if str(token.lemma_) in corpus.STE:
#                 # constraint (stm is noun (lock screen, etc.))
#                 if str(token.pos_) == 'NOUN':
#                     return True
#                 elif str(token.pos_) == 'VERB':
#                     if constraint(doc):
#                         return True
#     return False
#
#
# def constraint(doc):
#     for token in doc:
#         if str(token.dep_) == 'ROOT':
#             if str(token.lemma_) in corpus.STE:
#                 for child in token.children:
#                     if str(child.lemma_) in corpus.CST:
#                         return False
#             else:
#                 for child in token.children:
#                     if str(token.lemma_) in corpus.STE:
#                         if str(child.lemma_) in corpus.CST:
#                             return False
#     return True
