import spacy

import labelOfdata
import pattern_1
from utils import IOutils
from utils import utils


def main():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("results/projects/redisson_train.txt")
    # only_one = open('results/only_one_cmi.txt')
    # write_pos = open("./results/pos_concurrent.txt", "w")
    # read_pos = open("./results/pos_concurrent.txt")
    # den_results = open("./results/den_concurrent.txt", "a")
    results = {}
    dataset = IOutils.getTestset(conSents)

    for key in dataset.keys():
        # print(dataset[key])
        if pattern_1.finalversion(nlp, dataset[key]):
            results[key] = 1
        else:
            results[key] = 0
    print(results)
    fp = []
    fn = []
    one = 0
    for k in dataset.keys():
        # matrix.append(k)
        if results[k] == 1:
            one += 1
        if results[k] != labelOfdata.redisson_label[k]:
            if results[k] == 1:
                fp.append(k)
            else:
                fn.append(k)

    print(fp)
    print(len(fp))
    print(fn)
    print(len(fn))
    # file-->pos-->pattern1(SVO)-->targetFile(sents)-->dependence
    # dataset = getDataset2list(conSents)
    # dataset = IOutils.getDataset2list(conSents)
    # IOutils.getPos2file(nlp, dataset, write_pos)
    # write_pos.close()
    # test_results = pattern_1.testKW(nlp, dataset)
    # CVA_index, CVSY_index = pattern_1.getPtn1byPos(read_pos)
    # CVA_dataset = utils.getSentsByIndex(dataset, CVA_index)
    # CVSY_dataset = utils.getSentsByIndex(dataset, CVSY_index)
    # CVA_set = pattern_1.getPtn1byKw_CVA(nlp, CVA_dataset)
    # CVSY_set = pattern_1.getPtn1byKw_CVSY(nlp, CVSY_dataset)

    # for sent in CVAS_set:
    #     print(dataset[sent], end="")

    print('\n' + '==============================================')
    # print(CVSY_index)
    # for sent in C_set:
    #     print(sent)
    # print(dataset[sent], end="")

    conSents.close()
    # only_one.close()

    # read_pos.close()


if __name__ == '__main__':
    main()
