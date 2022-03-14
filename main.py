import spacy

import pattern_1
from utils import IOutils
from utils import utils


def main():
    nlp = spacy.load("en_core_web_sm")
    conSents = open("results/deadlockSents_NER.txt")
    # only_one = open('results/only_one_cmi.txt')
    write_pos = open("./results/pos_concurrent.txt", "w")
    read_pos = open("./results/pos_concurrent.txt")
    # den_results = open("./results/den_concurrent.txt", "a")

    # file-->pos-->pattern1(SVO)-->targetFile(sents)-->dependence
    # dataset = getDataset2list(conSents)
    dataset = IOutils.getDataset2list(conSents)
    # IOutils.getPos2file(nlp, dataset, write_pos)
    # write_pos.close()
    CVAS_set, C_set = pattern_1.getPtn1byKw(nlp, dataset)
    # sent_cva_set = utils.getSentsByIndex(dataset, CVA_index)
    # sent_cvsy_set = utils.getSentsByIndex(dataset, CVSY_index)
    # for s in sent_cvsy_set:
    #     print(s, end="")
    ptn1_results = pattern_1.getSentsOfPtn1(nlp, CVAS_set)
    # listd = ['CMI should not cause deadlock.']
    ptn12_results = pattern_1.getSentsOfPtn1_2(nlp, CVAS_set)
    print(len(CVAS_set))
    print(len(C_set))
    # for sent in CVAS_set:
    #     print(sent, end="")

    print('\n'+'==============================================')

    for sent in C_set:
        print(sent, end="")

    conSents.close()
    # only_one.close()

    read_pos.close()


if __name__ == '__main__':
    main()
