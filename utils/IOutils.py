# @Time    : 3/11/22 8:31 PM
# @Author  : Shuai S
# @File    : IOutils.py

def getDataset2list(targetFile):
    sentsList = []
    for line in targetFile:
        sentsList.append(line)
    return sentsList


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
            # elif str(token.lemma_) == 'deadlock':
            #     tmplist.append('SYMP')
            else:
                tmplist.append(str(token.pos_))
        results.write(str(tmplist) + '\n')


def getTestset(dataset):
    lineList = []
    for data in dataset:
        line = data.replace('\n', '').replace('\r', '')
        lineList.append(line)
        # if str(line) == '5':
        # print(len(str(line)))
    results = {}
    ls = []
    index = 0
    while index < len(lineList):
        if lineList[index].isnumeric():
            number = int(lineList[index])
            index += 1
            while index < len(lineList) and not lineList[index].isnumeric():
                ls.append(lineList[index])
                index += 1
            index -= 1
            results[number] = ls
            ls = []
        index += 1
    return results
