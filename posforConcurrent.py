import spacy


def getTag(nlp, conSents, results):
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    for sent in sentsList:
        doc = nlp(sent)
        tmplist = []
        for token in doc:
            tmplist.append(str(token.pos_))
        results.write(str(tmplist) + '\n')


def getDen(nlp, conSents, results):
    sentsList = []
    for line in conSents:
        sentsList.append(str(line))
    for sent in sentsList:
        doc = nlp(sent)
        tmplist = []
        for token in doc:
            tmplist.append(str(token.dep_))
        results.write(str(tmplist) + '\n')


def main():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("results/deadlockSents.txt")
    pos_results = open("./results/pos_concurrent.txt", "a")
    den_results = open("./results/den_concurrent.txt", "a")

    getTag(nlp, conSents, pos_results)
    # getDen(nlp, conSents, den_results)


    conSents.close()
    pos_results.close()
    den_results.close()


if __name__ == '__main__':
    main()
