import spacy

import pattern_1
from utils import IOutils
from utils import utils


def main():
    nlp = spacy.load("en_core_web_sm")
    # conSents = open("results/deadlockSents_NER.txt")
    only_one = open('results/only_one_cmi.txt')
    write_pos = open("./results/pos_concurrent.txt", "w")
    read_pos = open("./results/pos_concurrent.txt")
    # den_results = open("./results/den_concurrent.txt", "a")

    # file-->pos-->pattern1(SVO)-->targetFile(sents)-->dependence
    # dataset = getDataset2list(conSents)
    dataset = IOutils.getDataset2list(only_one)
    IOutils.getPos2file(nlp, dataset, write_pos)
    write_pos.close()
    index = pattern_1.getCoarse_Ptn1Index()
    pattern_1_set = utils.getSentsByIndex(dataset, index)
    ptn1_results = pattern_1.getSentsOfPtn1(nlp)

    for sent in ptn1_results:
        print(sent, end="")

    # conSents.close()
    only_one.close()

    read_pos.close()


if __name__ == '__main__':
    main()
