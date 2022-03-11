from textblob import TextBlob
from spacy.lang.en import English
from xml.dom.minidom import Document

blob = TextBlob("I love your dog")
print(blob.tags)

nlp = English()
# #
# apples = nlp(u"refuel")
# orange = nlp(u"good")

# print(apples.similarity(orange))

fileObject = open('../results/bugreports.txt')

lineList = []

for line in fileObject:
    lineList.append(str(line))
for sentence in lineList:
    print(nlp(sentence).sents)
    # for sent in nlp(sentence).sents:
    #     print(sent)

