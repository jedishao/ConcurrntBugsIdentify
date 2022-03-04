import spacy

nlp = spacy.load("en_core_web_sm")
conSents = open("./results/concurrentSents.txt")
pos_results = open("./results/pos_concurrent.txt", "a")

sentsList = []
for line in conSents:
    sentsList.append(str(line))

# doc = nlp("I love dogs")
# for token in doc:
#     print(token.pos_)
for sent in sentsList:
    doc = nlp(sent)
    tmplist = []
    for token in doc:
        tmplist.append(str(token.pos_))
    pos_results.write(str(tmplist)+'\n')

conSents.close()
pos_results.close()
