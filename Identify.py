# @Time    : 4/28/22 4:58 PM
# @Author  : Shuai S
# @File    : Identify.py
import patterns.root as root
import patterns.verb as verb
import patterns.noun as noun
from patterns import p_keywords
from patterns.CMI import cmi, unlock, lock, infinite
from patterns.noun import n_bug, n_deadlock, n_lock, n_problem, n_exception, n_fail, n_error, n_issue, n_dump, n_block, \
    n_hung, n_condition
from patterns.root import r_fail, r_release, r_race, r_problem, r_hang, r_have, r_issue, r_throw, r_try, r_use, r_work, \
    r_be, r_block, r_cause, r_crash, r_deadlock, r_exception, r_execute, r_get, r_lock, r_obtain, r_stuck, root, \
    r_condition, r_park, r_acquire
from patterns.verb import v_await, v_block, v_break, v_hang, v_have, v_hold, v_unlock, v_occur, v_receive, v_wait, \
    v_stuck, v_lock, verb, v_fail, v_release


def identify(nlp, dataset):
    # for sentence in dataset:
    result = None
    doc = nlp(dataset)
    for token in doc:
        if str(token.lemma_).lower() in ['question', 'suggestion', 'implement', 'optimization', 'feature']:
            return 9999
    for token in doc:
        if str(token.dep_) == 'ROOT':
            if str(token.lemma_).lower() == 'acquire':
                result = r_acquire.check(nlp, doc)
            elif str(token.lemma_).lower() == 'be':
                result = r_be.check(nlp, doc)
            elif str(token.lemma_).lower() == 'block':
                result = r_block.check(nlp, doc)
            elif str(token.lemma_).lower() == 'cause':
                result = r_cause.check(nlp, doc)
            elif str(token.lemma_).lower() == 'crash':
                result = r_crash.check(nlp, doc)
            elif str(token.lemma_).lower() == 'condition':
                result = r_condition.check(nlp, doc)
            elif str(token.lemma_).lower() == 'deadlock':
                result = r_deadlock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'exception':
                result = r_exception.check(nlp, doc)
            elif str(token.lemma_).lower() == 'execute':
                result = r_execute.check(nlp, doc)
            elif str(token.lemma_).lower() == 'fail':
                result = r_fail.check(nlp, doc)
            elif str(token.lemma_).lower() == 'get':
                result = r_get.check(nlp, doc)
            elif str(token.lemma_).lower() == 'hang':
                result = r_hang.check(nlp, doc)
            elif str(token.lemma_).lower() == 'have':
                result = r_have.check(nlp, doc)
            elif str(token.lemma_).lower() == 'issue':
                result = r_issue.check(nlp, doc)
            elif str(token.lemma_).lower() == 'lock':
                result = r_lock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'obtain':
                result = r_obtain.check(nlp, doc)
            elif str(token.lemma_).lower() == 'park':
                result = r_park.check(nlp, doc)
            elif str(token.lemma_).lower() == 'problem':
                result = r_problem.check(nlp, doc)
            elif str(token.lemma_).lower() == 'race':
                result = r_race.check(nlp, doc)
            elif str(token.lemma_).lower() == 'release':
                result = r_release.check(nlp, doc)
            elif str(token.lemma_).lower() == 'throw':
                result = r_throw.check(nlp, doc)
            elif str(token.lemma_).lower() == 'try':
                result = r_try.check(nlp, doc)
            elif str(token.lemma_).lower() == 'use':
                result = r_use.check(nlp, doc)
            elif str(token.lemma_).lower() == 'work':
                result = r_work.check(nlp, doc)
            elif str(token.lemma_).lower() in ['stuck', 'stick']:
                result = r_stuck.check(nlp, doc)
            else:
                result = root.check(nlp, doc)
        if result is not None:
            return result
    for token in doc:
        if str(token.pos_) == 'VERB':
            if str(token.lemma_).lower() == 'await':
                result = v_await.check(nlp, doc)
            elif str(token.lemma_).lower() == 'block':
                result = v_block.check(nlp, doc)
            elif str(token.lemma_).lower() == 'break':
                result = v_break.check(nlp, doc)
            elif str(token.lemma_).lower() == 'hang':
                result = v_hang.check(nlp, doc)
            elif str(token.lemma_).lower() == 'have':
                result = v_have.check(nlp, doc)
            elif str(token.lemma_).lower() == 'hold':
                result = v_hold.check(nlp, doc)
            elif str(token.lemma_).lower() == 'occur':
                result = v_occur.check(nlp, doc)
            elif str(token.lemma_).lower() == 'receive':
                result = v_receive.check(nlp, doc)
            elif str(token.lemma_).lower() == 'release':
                result = v_release.check(nlp, doc)
            elif str(token.lemma_).lower() == 'fail':
                result = v_fail.check(nlp, doc)
            elif str(token.lemma_).lower() == 'lock':
                result = v_lock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'unlock':
                result = v_unlock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'wait':
                result = v_wait.check(nlp, doc)
            elif str(token.lemma_).lower() in ['stuck', 'stick']:
                result = v_stuck.check(nlp, doc)
            else:
                result = verb.check(nlp, doc)
        if result is not None:
            return result
    for token in doc:
        if str(token.pos_) in ['NOUN', 'PROPN']:
            if str(token.lemma_).lower() == 'bug':
                result = n_bug.check(nlp, doc)
            elif str(token.lemma_).lower() == 'block':
                result = n_block.check(nlp, doc)
            elif str(token.lemma_).lower() == 'condition':
                result = n_condition.check(nlp, doc)
            elif str(token.lemma_).lower() == 'deadlock':
                result = n_deadlock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'lock':
                result = n_lock.check(nlp, doc)
            elif str(token.lemma_).lower() == 'hung':
                result = n_hung.check(nlp, doc)
            elif str(token.lemma_).lower() == 'problem':
                result = n_problem.check(nlp, doc)
            elif str(token.lemma_).lower() == 'exception':
                result = n_exception.check(nlp, doc)
            elif str(token.lemma_).lower() == 'fail':
                result = n_fail.check(nlp, doc)
            elif str(token.lemma_).lower() == 'error':
                result = n_error.check(nlp, doc)
            elif str(token.lemma_).lower() == 'issue':
                result = n_issue.check(nlp, doc)
            elif str(token.lemma_).lower() == 'dump':
                result = n_dump.check(nlp, doc)
        if result is not None:
            return result
    for token in doc:
        if str(token) == 'CMI':
            result = cmi.check(nlp, doc)
        elif str(token.lemma_).lower() == 'unlock':
            result = unlock.check(nlp, doc)
        elif str(token.lemma_).lower() == 'lock':
            result = lock.check(nlp, doc)
        elif str(token.lemma_).lower() == 'infinite':
            result = infinite.check(nlp, doc)
        if result is not None:
            return result
    result = p_keywords.check(nlp, doc)
    return result
