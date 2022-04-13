# @Time    : 4/3/22 1:02 PM
# @Author  : Shuai S
# @File    : Identify.py
import corpus
from patterns import pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6, pattern_7


def identify(nlp, dataset, key):
    exc, cob, cop, adv, symp, ste, neg, cmi, log, iss, kw, ter = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # keywords with exception
    for sents in dataset:
        doc = nlp(sents)
        for token in doc:
            if str(token.lemma_).lower() in corpus.COB:
                cob += 1
            elif str(token.lemma_).lower() in corpus.COP:
                cop += 1
            elif str(token.lemma_).lower() in corpus.SYMP:
                symp += 1
            elif str(token.lemma_).lower() in ['not']:
                neg += 1
            elif str(token.lemma_).lower() in corpus.TMP:
                adv += 1
            elif str(token.lemma_).lower() in corpus.EXC:
                exc += 1
            elif str(token) == 'CMI':
                cmi += 1
            elif str(token.lemma_).lower() in corpus.LOG:
                log += 1
            elif str(token.lemma_).lower() in corpus.ISS:
                iss += 1
            if str(token.lemma_).lower() in corpus.STE:
                ste += 1
            if str(token.lemma_).lower() in corpus.KW:
                kw += 1
            if str(token.lemma_).lower() in corpus.TER:
                ter += 1
    count = cop + adv + symp
    if exc and kw:
        print('exc--->' + str(key))
        if cmi > 0:
            return True
        elif ste > 0:
            if pattern_1.check(nlp, dataset):
                return True

    if cob:
        print('cob--->' + str(key))
        if cmi > 0:
            return True
        if pattern_2.check(nlp, dataset):
            return True

    if neg and kw + ter:
        print('neg--->' + str(key))
        if pattern_3.check(nlp, dataset):
            return True

    if count:
        print('count--->' + str(key))
        if pattern_4.check(nlp, dataset):
            return True

    if iss and kw:
        print('iss--->' + str(key))
        if pattern_5.check(nlp, dataset):
            return True

    if log and kw:
        print('log--->' + str(key))
        if pattern_6.check(nlp, dataset):
            return True

    if ter and kw:
        print('ter--->' + str(key))
        if pattern_7.check(nlp, dataset):
            return True
        # [39, 106, 118, 155, 156, 169, 171, 199, 216, 254, 386, 409, 421, 465, 503, 533, 573, 581, 738, 780]
    return False
