import ast
import corpus


# [CMI][COP]([TMP]+[SYMP])


def getPtn1byPos(sents_with_pos):
    """
    The first step for pattern 1, find all the sentences have [CMI][VERB][ADV]
    :param sents_with_pos: sentences with POS tag
    :return: the index of sentences that are identified as mode 1
    """
    sentsList = []
    for line in sents_with_pos:
        list_list = ast.literal_eval(line)
        sentsList.append(list_list)
    # for the readability of .txt file
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
            elif str(token) == 'NOUN':
                s += 1
        if c == 1 and v > 0:
            if a > 0:  # and s == 0
                CVA_index.append(i)
            elif s > 0:
                CVSY_index.append(i)
        i += 1
    return CVA_index, CVSY_index


def getPtn1byKw_CVA(nlp, dataset):
    CVA_set = []
    for sents in dataset:
        flag = True
        cmi, cop, tmp, symp = 0, 0, 0, 0
        doc = nlp(sents)
        for token in doc:
            if str(token) == 'CMI':
                cmi += 1
            elif str(token.lemma_) in corpus.COP:
                cop += 1
            elif str(token.lemma_) in corpus.TMP:
                tmp += 1
        if cmi == 1:
            if cop > 0 and tmp > 0:
                CVA_set.append(sents)
    return CVA_set


def getPtn1byKw_CVSY(nlp, dataset):
    CVSY_set = []
    for sents in dataset:
        cmi, cop, symp = 0, 0, 0
        doc = nlp(sents)
        for token in doc:
            if str(token) == 'CMI':
                cmi += 1
            elif str(token.lemma_) in corpus.COP:
                cop += 1
            elif str(token.lemma_) in corpus.SYMP:
                symp += 1
        if cmi == 1:
            if cop > 0 and symp > 0:
                CVSY_set.append(sents)
    return CVSY_set


def getSentsOfPtn1(nlp, coarse):
    """
    CMI is the subject
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
                    flag = True
                    cmi, adv, symp = False, False, False
                    for child in token.children:
                        if str(child.dep_) in corpus.S:
                            if str(child) == 'CMI':
                                cmi = True
                        elif str(child.dep_) in corpus.ADV:
                            if str(child.lemma_) in corpus.TMP:
                                adv = True
                        elif str(child.dep_) in corpus.OBJ:
                            if str(child.lemma_) in corpus.SYMP:
                                symp = True
                    if cmi and adv:
                        results.append(sent)
                        flag = False
                    if cmi and symp and flag:
                        results.append(sent)
                elif str(token.lemma_) in corpus.OTHER:
                    flag = True
                    cmi, cop, symp = False, False, False
                    for child in token.children:
                        if str(child.dep_) in corpus.S:
                            if str(child) == 'CMI':
                                cmi = True
                        elif str(child.dep_) == 'attr':
                            for ch in child.children:
                                if str(ch.dep_) in corpus.ADV:
                                    if str(ch.lemma_) in corpus.COP:
                                        cop = True
                    if cmi and cop:
                        results.append(sent)
    return results


def getSentsOfPtn1_2(nlp, coarse):
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
                        elif str(child.dep_) == 'dobj':
                            symp = True
                if str(token.lemma_) in corpus.OTHER:
                    if str(child.dep_) in corpus.OBJ:
                        # if str(child) in corpus.TMP:
                        symp = True
                if cmi and symp:
                    results.append(sent)
    return results


def testKW(nlp, dataset):
    results = []
    index = 1
    for sents in dataset:
        count = 0
        doc = nlp(sents)
        for token in doc:
            if str(token.lemma_) in corpus.SYMP or str(token.lemma_) in corpus.TMP:
                count += 1
        if count >= 1:
            results.append(index)
        index += 1
    return results


def finalversion(nlp, dataset):
    cob, cop, adv, symp = 0, 0, 0, 0
    for sents in dataset:
        doc = nlp(sents)
        for token in doc:
            if str(token.lemma_) in corpus.COB:
                cob += 1
            elif str(token.lemma_) in corpus.COP:
                cop += 1
            elif str(token.lemma_) in corpus.SYMP:
                symp += 1
            elif str(token.lemma_) in corpus.TMP:
                adv += 1
    count = cop + symp + adv
    if cob > 0:
        return True
    elif count > 1:
        return True
    else:
        return False
