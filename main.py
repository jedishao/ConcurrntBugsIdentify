import spacy

import Identify
import labelOfdata
from utils import IOutils


def ree(dataset):
    fp = []
    fn = []
    one = 0
    for k in dataset.keys():
        # matrix.append(k)
        if dataset[k] == 1:
            one += 1
        if dataset[k] != labelOfdata.grpc[k]:
            if dataset[k] == 1:
                fp.append(k)
            else:
                fn.append(k)
    return fp, fn


def main():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("results/projects/grpc_train.txt", encoding='utf-8')
    #  conSents = open("results/projects/test.txt", encoding='utf-8')
    # conSents = open("results/projects/redisson_pp.txt", encoding='utf-8')
    # only_one = open('results/only_one_cmi.txt')
    # write_pos = open("./results/pos_concurrent.txt", "w")
    # read_pos = open("./results/pos_concurrent.txt")
    # den_results = open("./results/den_concurrent.txt", "a")
    result = {}
    dataset = IOutils.getTestset(conSents)

    for key in dataset.keys():
        if Identify.identify(nlp, dataset[key], key):
            result[key] = 1
        else:
            result[key] = 0

    one = []
    zero = []
    #print(result)
    for re in result.keys():
        if result[re] == 1:
            one.append(re)
        else:
            zero.append(re)
    print(len(one))
    print(one)
    print(len(zero))
    print(zero)
    # file-->pos-->pattern1(SVO)-->targetFile(sents)-->dependence
    # data = getDataset2list(conSents)
    # data = IOutils.getDataset2list(conSents)
    # IOutils.getPos2file(nlp, data, write_pos)
    # write_pos.close()
    # test_results = pattern_1.testKW(nlp, data)
    # CVA_index, CVSY_index = pattern_1.getPtn1byPos(read_pos)
    # CVA_dataset = utils.getSentsByIndex(data, CVA_index)
    # CVSY_dataset = utils.getSentsByIndex(data, CVSY_index)
    # CVA_set = pattern_1.getPtn1byKw_CVA(nlp, CVA_dataset)
    # CVSY_set = pattern_1.getPtn1byKw_CVSY(nlp, CVSY_dataset)

    # for sent in CVAS_set:
    #     print(data[sent], end="")

    print('\n' + '==============================================')
    # print(CVSY_index)
    # for sent in C_set:
    #     print(sent)
    # print(data[sent], end="")
    fp, fn = ree(result)
    print(fp)
    print(fn)
    conSents.close()
    # only_one.close()

    # read_pos.close()


if __name__ == '__main__':
    main()
