# @Time    : 3/11/22 7:37 PM
# @Author  : Shuai S
# @File    : utils.py


def getSentsByIndex(dataset, index):
    """
    :param dataset: target file
    :param index: index list
    :return: the sentence follow by the index list
    """
    results = []
    for i in index:
        results.append(dataset[i])
    return results


