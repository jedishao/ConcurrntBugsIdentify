# from textblob import TextBlob
import spacy
from spacy.lang.en import English
from xml.dom.minidom import Document

# blob = TextBlob("I love your dog")
# print(blob.tags)
import corpus

# nlp = English()
# #
# apples = nlp(u"refuel")
# orange = nlp(u"good")

# print(apples.similarity(orange))

fileObject = open('../results/projects/redisson_train.txt', 'r')
lineList = []
for line in fileObject:
    lin = line.replace('\n', '').replace('\r', '')
    lineList.append(lin)
    # if str(line) == '5':
    # print(len(str(line)))
results = {}
ls = 0
number = 0
for l in lineList:
    if l.isnumeric():
        if number != 0:
            results[number] = ls
        number = int(l)

print(results)


#
# for line in fileObject:
#     lineList.append(str(line))
# for sentence in lineList:
#     print(nlp(sentence).sents)
#     # for sent in nlp(sentence).sents:
#     #     print(sent)

# dataset = ["Any plan to add TTL to a Lock operation? Don't confuse with tryLock with TIME.",
#            'I refer to a situation where a thread is dead and leave a resource locked (deadlock).', '']
# nlp = spacy.load("en_core_web_sm")
# for sents in dataset:
#     cop, adv = False, False
#     doc = nlp(sents)
#     for token in doc:
#         if str(token.lemma_) in corpus.COB:
#             print(token)
