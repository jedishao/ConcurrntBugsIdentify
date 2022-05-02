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
    conSents = open("dataset/dataset1/grpc/grpc_pos.txt", encoding='utf-8')
    wre = open("dataset/dataset1/grpc/weja_neg.txt", 'w')
    #  conSents = open("dataset/dataset1/test.txt", encoding='utf-8')
    # conSents = open("dataset/dataset1/redisson_pp.txt", encoding='utf-8')
    # only_one = open('dataset/only_one_cmi.txt')
    # write_pos = open("./dataset/pos_concurrent.txt", "w")
    # read_pos = open("./dataset/pos_concurrent.txt")
    # den_results = open("./dataset/den_concurrent.txt", "a")
    result = []
    rer = []
    # dataset = IOutils.getTestset(conSents)
    lineList = []
    for li in conSents:
        lineList.append(li)

    j = 1
    for re in lineList:
        print('ss')
        doc = nlp(re)
        lsss = []
        rer = []
        for i in range(138):
            rer.append(0)
        for sent in doc.sents:
            lsss.append(str(sent))
        for s in lsss:
            rew = Identify.identify(nlp, s)
            if rew == 9999:
                break
            if rew is not None:
                # print(j, "--->", rew)
                rer[rew] = 1
        result.append(rer)
        j += 1

    print('=======================')
    k = 1
    bai = []
    for r in result:
        r.append(1)
        wre.write(str(r))
        wre.write('\n')
        # key = 0
        # for oo in r:
        #     if oo == 1:
        #         key = 1
        # if key == 0:
        #     bai.append(k)
        # k += 1

    print(len(bai))
    print(bai)
    # for key in dataset.keys():
    #     if Identify.identify(nlp, dataset[key], key):
    #         result[key] = 1
    #     else:
    #         result[key] = 0

    # one = []
    # zero = []
    # #print(result)
    # for re in result.keys():
    #     if result[re] == 1:
    #         one.append(re)
    #     else:
    #         zero.append(re)
    # print(len(one))
    # print(one)
    # print(len(zero))
    # print(zero)
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
    # fp, fn = ree(result)
    # print(fp)
    # print(fn)
    conSents.close()
    # only_one.close()

    # read_pos.close()


if __name__ == '__main__':
    main()
