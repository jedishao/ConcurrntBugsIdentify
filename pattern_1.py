import ast
import corpus


def getCoarse_Ptn1Index(sents_with_pos):
    """
    The first step for pattern 1, find all the sentences have [CMI][VERB][ADV]
    :param sents_with_pos: sentences with POS tag
    :return: the index of sentences that are identified as mode 1
    """
    sentsList = []
    for line in sents_with_pos:
        list_list = ast.literal_eval(line)
        sentsList.append(list_list)
    i = 0
    CVA_index = []
    CVSY_index = []

    for sens in sentsList:
        c, v, a, s = 0, 0, 0, 0  # 'VERB', 'ADV'
        for token in sens:
            if str(token) == 'CMI':
                c += 1
            elif str(token) == 'VERB':
                v += 1
            elif str(token) == 'ADV':
                a += 1
            elif str(token) == 'SYMP':
                s += 1
        if c == 1 and v > 0 and a > 0 and s == 0:
            CVA_index.append(i)
        if c == 1 and v > 0 and s > 0:
            CVSY_index.append(i)
        i += 1
    return CVA_index, CVSY_index


def getSentsOfPtn1_1(nlp, coarse):
    """
    The final step for pattern 1
    :param coarse:
    :param nlp:
    :return:
    """
    results = []
    for sent in coarse:
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

# def getSentsOfPtn1_1(nlp, coarse):
