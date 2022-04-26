# from textblob import TextBlob
import numpy as np
import requests
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
import labelOfdata
#
# fileObject = open('../dataset/dataset1/redisson_train.txt', 'r')
# lineList = []
# for line in fileObject:
#     lin = line.replace('\n', '').replace('\r', '')
#     lineList.append(lin)
#     # if str(line) == '5':
#     # print(len(str(line)))
# dataset = {}
# ls = 0
# number = 0
# for l in lineList:
#     if l.isnumeric():
#         if number != 0:
#             dataset[number] = ls
#         number = int(l)
#
# print(dataset)
#
# for kk in dataset.keys():
#     if kk not in labelOfdata.redisson.keys():
#         print('---'+kk)
#
# lab = []
# for la in labelOfdata.redisson.keys():
#     if labelOfdata.redisson[la] == 1:
#         lab.append(la)
# print(len(labelOfdata.redisson))
#
# for line in fileObject:
#     lineList.append(str(line))
# for sentence in lineList:
#     print(nlp(sentence).sents)
#     # for sent in nlp(sentence).sents:
#     #     print(sent)

# data = ["Any plan to add TTL to a Lock operation? Don't confuse with tryLock with TIME.",
#            'I refer to a situation where a thread is dead and leave a resource locked (deadlock).', '']
# nlp = spacy.load("en_core_web_sm")
# for sents in data:
#     cop, adv = False, False
#     doc = nlp(sents)
#     for token in doc:
#         if str(token.lemma_) in corpus.COB:
#             print(token)
# ll = []
# for key in labelOfdata.redisson.keys():
#     ll.append(labelOfdata.redisson[key])
# print(ll)

# url = 'https://github.com/redisson/redisson/issues/' + '3416'
# print(url)
# response = requests.get(url)
# if response.url.find('pull') == -1:
#     print('ss')

# for i in range(10):
#     print(i)