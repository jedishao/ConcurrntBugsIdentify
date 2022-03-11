import ast
import spacy


def pattern1():
    nlp = spacy.load("en_core_web_sm")
    # conSents = open("../results/deadlockSents_NER_copy.txt")
    conSents = open("../results/test.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    # doc = nlp("TUC should not cause deadlocks")
    i = 0
    j = 1
    indx = []
    for sens in sentsList:
        doc = nlp(sens)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                children = list(token.children)
                if str(children).__contains__('TUC'):
                    print(str(token) + "--->" + str(children))
                    i += 1
                    indx.append(j)
        j += 1
    print(indx)
    print(i)


def pattern2():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("../results/deadlockSents_NER_copy.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    # doc = nlp("TUC should not cause deadlocks")
    i = 0
    j = 1
    indx = []
    for sens in sentsList:
        doc = nlp(sens)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                for child in token.children:
                    if str(child.dep_) == 'prep':
                        if str(list(child.rights)).__contains__('TUC'):
                            # print(str(token) + "--->" + str(children))
                            i += 1
                            indx.append(j)
        j += 1
    print(indx)
    print(i)


def pattern3():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("../results/deadlockSents_NER_copy.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    i = 0
    j = 1
    indx = []
    for sens in sentsList:
        doc = nlp(sens)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                for child in token.children:
                    if str(child.pos_) == 'VERB':
                        if str(list(child.lefts)).__contains__('TUC'):
                            # print(str(token) + "--->" + str(children))
                            i += 1
                            indx.append(j)
        j += 1
    print(indx)
    print(i)


def pattern4():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("../results/deadlockSents_NER_copy.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    i = 0
    j = 1
    indx = []
    for sens in sentsList:
        doc = nlp(sens)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                for child in token.children:
                    # if str(child.pos_) == 'NOUN':
                    if str(list(child.lefts)).__contains__('TUC') or str(list(child.rights)).__contains__('TUC'):
                        # print(str(token) + "--->" + str(children))
                        i += 1
                        indx.append(j)
        j += 1
    print(indx)
    print(i)


def pattern5():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("../results/deadlockSents_NER_copy.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    i = 0
    j = 1
    indx = []
    for sens in sentsList:
        doc = nlp(sens)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                for child in token.children:
                    if str(list(child.lefts)).__contains__('TUC') or str(list(child.rights)).__contains__('TUC'):
                        # print(str(token) + "--->" + str(children))
                        i += 1
                        indx.append(j)
                    elif len(list(child.rights)) != 0:
                        for ch in child.rights:
                            if str(list(ch.lefts)).__contains__('TUC') or str(list(ch.rights)).__contains__(
                                    'TUC'):
                                i += 1
                                indx.append(j)
                    elif len(list(child.lefts)) != 0:
                        for ch in child.lefts:
                            if str(list(ch.lefts)).__contains__('TUC') or str(list(ch.rights)).__contains__(
                                    'TUC'):
                                i += 1
                                indx.append(j)

        j += 1
    print(indx)
    print(i)


def testDep_():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('Circular dependency between TUC and TUC causes thread deadlock')
    tmp = []
    for token in doc:
        tmp.append(str(token.dep_))
    print(tmp)


def testRoot():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('There are two TUC involved in this deadlock.')
    for token in doc:
        if str(token.dep_) == 'ROOT':
            print(token.text)
            print(list(token.children))


def testHead():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('Circular dependency between TUC and TUC causes thread deadlock')
    for token in doc:
        print(str(token) + '--->' + str([right for right in token.rights]))


def getPos():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp('There are two TUC involved in this deadlock.')
    indx = []
    for token in doc:
        if str(token) == 'TUC':
            indx.append('TUC')
        else:
            indx.append(str(token.pos_))
    print(indx)


def getPos4file():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("../results/test.txt")
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    for sens in sentsList:
        indx = []
        doc = nlp(sens)
        for token in doc:
            if str(token) == 'TUC':
                indx.append('TUC')
            else:
                indx.append(str(token.pos_))
        print(indx)


def getPosPattern():
    conSents = open("../results/test.txt")
    sentsList = []
    for line in conSents:
        list_list = ast.literal_eval(line)
        sentsList.append(list_list)
    i = 0
    tmp = []
    for sens in sentsList:
        t, v, a = 0, 0, 0  # 'VERB', 'ADV'
        for token in sens:
            if str(token) == 'TUC':
                t += 1
            elif str(token) == 'VERB' and t > 0:
                v += 1
            elif str(token) == 'ADV' and v > 0:
                a += 1
        if a > 0:
            tmp.append(i)
        i += 1
    print(tmp)


def writeTofile():
    conSents = open("../results/test.txt")
    target = open("../results/testdel.txt", 'a')
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    index = [3, 6, 10, 16, 41, 51, 53, 61, 67, 69, 70, 72, 74, 76, 85, 86, 88, 94, 95, 99]
    for i in index:
        target.write(str(sentsList[i]) + '\n')


# testRoot()
print(spacy.explain("acl"))

# print(1 and 3 in [1, 3, 3])

# print([child for child in token.children])

# for token in doc:
#     if str(token.dep_) == 'ROOT':
#         for to in token.children:
#             if str(to.dep_) == 'nsubj':
#                 print('TUC:'+str(to))
#             elif str(to.dep_) == 'dobj':
#                 print(str(to))

# Load English tokenizer, tagger, parser and NER
# nlp = spacy.load("en_core_web_sm")

# Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")
# doc = nlp(text)

# Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
#
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# for token in doc:
#     print(token.text, token.dep_, token.head.text, token.head.pos_,
#           [child for child in token.children])
# conSents = open("../results/test.txt")
# sentsList = []
# for line in conSents:
#     sentsList.append(str(line))
# for sent in sentsList:
#     doc = nlp(sent)
#     tmplist = []
#     for token in doc:
#         print(token.text, token, token.head.text, [child for child in token.children])
# conSents.close()

# doc = nlp("TUC is recursively invoked twice")
# tmplist = []
# for token in doc:
#     tmplist.append(str(token.dep_))
# print(tmplist)

# print(token.text, [right for right in token.subtree], token.head.text, [child for child in token.children])
