import ast

import spacy

import corpus


def getPos2file(nlp, dataset, results):
    """

    :param dataset:
    :param nlp:
    :param results: results file
    :return: results
    """
    for sent in dataset:
        doc = nlp(sent)
        tmplist = []
        for token in doc:
            if str(token) == 'CMI':
                tmplist.append("CMI")
            elif str(token.lemma_) == 'deadlock':
                tmplist.append("SYMP")
            else:
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


def dependence(nlp, sent):
    doc = nlp(sent)
    tmplist = []
    for token in doc:
        if str(token.dep_) == 'ROOT':
            for to in token.childern:
                if str(to.dep_) == 'nsubj':
                    print(str(to))


def getPattern1Index(sents_with_pos):
    """
    :param sents_with_pos: sentences with POS tag
    :return: the index of sentences that are identified as mode 1
    """

    sentsList = []
    for line in sents_with_pos:
        list_list = ast.literal_eval(line)
        sentsList.append(list_list)
    i = 0
    index = []
    # pattern 1
    for sens in sentsList:
        t, v, a = 0, 0, 0  # 'VERB', 'ADV'
        for token in sens:
            if str(token) == 'CMI':
                t += 1
            elif str(token) == 'VERB' and t > 0:
                v += 1
            elif str(token) == 'ADV' and v > 0:
                a += 1
        if a > 0:
            index.append(i)
        i += 1
    return index


def getSentsByIndex(dataset, index):
    results = []
    for i in index:
        results.append(dataset[i])
    return results


def getDataset2list(targetFile):
    sentsList = []
    for line in targetFile:
        sentsList.append(line)
    return sentsList


def getSentsOfPtn1(nlp, targetFile):
    results = []
    for sent in targetFile:
        doc = nlp(sent)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_) in corpus.COP:
                    cmi = False
                    symp = False
                    for child in token.children:
                        if str(child.dep_) in corpus.S:
                            if str(child) == 'CMI':
                                cmi = True
                        elif str(child.dep_) in corpus.ADV:
                            if str(child) in corpus.TMP:
                                symp = True
                    if cmi and symp:
                        results.append(sent)
    return results


def main():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("results/deadlockSents_NER.txt")
    write_pos = open("./results/pos_concurrent.txt", "w")
    read_pos = open("./results/pos_concurrent.txt", "r")
    # den_results = open("./results/den_concurrent.txt", "a")

    # file-->pos-->pattern1(SVO)-->targetFile(sents)-->dependence
    dataset = getDataset2list(conSents)
    getPos2file(nlp, dataset, write_pos)
    index = getPattern1Index(read_pos)
    pattern_1_set = getSentsByIndex(dataset, index)
    ptn1_sents = getSentsOfPtn1(nlp, pattern_1_set)

    print(ptn1_sents)

    conSents.close()
    write_pos.close()
    read_pos.close()


if __name__ == '__main__':
    main()
