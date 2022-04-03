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
    for line in lineList:
        if line.isnumeric():
            number = int(line)
            results[number] = ls
            ls = []
        else:
            ls.append(line)
    return results
