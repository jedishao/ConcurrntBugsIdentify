# from textblob import TextBlob
from spacy.lang.en import English
from xml.dom.minidom import Document

# blob = TextBlob("I love your dog")
# print(blob.tags)

nlp = English()
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
ls = []
number = 0
for l in lineList:
    if l.isnumeric():
        if number != 0:
            results[number] = ls
        number = int(l)
        ls = []
    else:
        ls.append(l)

print(results)


#
# for line in fileObject:
#     lineList.append(str(line))
# for sentence in lineList:
#     print(nlp(sentence).sents)
#     # for sent in nlp(sentence).sents:
#     #     print(sent)
