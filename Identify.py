# @Time    : 4/28/22 4:58 PM
# @Author  : Shuai S
# @File    : Identify.py
import patterns.root as root
import patterns.verb as verb
import patterns.noun as noun


def identify(nlp, dataset, key):
    for sentence in dataset:
        doc = nlp(sentence)
        for token in doc:
            if str(token.dep_) == 'ROOT':
                if str(token.lemma_).lower() == 'be':
                    return root.r_be.check(doc)
                elif str(token.lemma_).lower() == 'block':
                    return root.r_block.check(doc)
                elif str(token.lemma_).lower() == 'cause':
                    return root.r_cause.check(doc)
                elif str(token.lemma_).lower() == 'crash':
                    return root.r_crash.check(doc)
                elif str(token.lemma_).lower() == 'deadlock':
                    return root.r_deadlock.check(doc)
                elif str(token.lemma_).lower() == 'exception':
                    return root.r_exception.check(doc)
                elif str(token.lemma_).lower() == 'execute':
                    return root.r_execute.check(doc)
                elif str(token.lemma_).lower() == 'fail':
                    return root.r_fail.check(doc)
                elif str(token.lemma_).lower() == 'get':
                    return root.r_get.check(doc)
                elif str(token.lemma_).lower() == 'hang':
                    return root.r_hang.check(doc)
                elif str(token.lemma_).lower() == 'have':
                    return root.r_have.check(doc)
                elif str(token.lemma_).lower() == 'issue':
                    return root.r_issue.check(doc)
                elif str(token.lemma_).lower() == 'lock':
                    return root.r_lock.check(doc)
                elif str(token.lemma_).lower() == 'obtain':
                    return root.r_obtain.check(doc)
                elif str(token.lemma_).lower() == 'problem':
                    return root.r_problem.check(doc)
                elif str(token.lemma_).lower() == 'race':
                    return root.r_race.check(doc)
                elif str(token.lemma_).lower() == 'release':
                    return root.r_release.check(doc)
                elif str(token.lemma_).lower() == 'throw':
                    return root.r_throw.check(doc)
                elif str(token.lemma_).lower() == 'try':
                    return root.r_try.check(doc)
                elif str(token.lemma_).lower() == 'use':
                    return root.r_use.check(doc)
                elif str(token.lemma_).lower() == 'work':
                    return root.r_work.check(doc)
            elif str(token.dep_) == 'VERB':
                if str(token.lemma_).lower() == 'await':
                    return verb.v_await.check(doc)
                elif str(token.lemma_).lower() == 'block':
                    return verb.v_block.check(doc)
                elif str(token.lemma_).lower() == 'break':
                    return verb.v_break.check(doc)
                elif str(token.lemma_).lower() == 'hang':
                    return verb.v_hang.check(doc)
                elif str(token.lemma_).lower() == 'have':
                    return verb.v_have.check(doc)
                elif str(token.lemma_).lower() == 'hold':
                    return verb.v_hold.check(doc)
                elif str(token.lemma_).lower() == 'occur':
                    return verb.v_occur.check(doc)
                elif str(token.lemma_).lower() == 'receive':
                    return verb.v_receive.check(doc)
                elif str(token.lemma_).lower() == 'unlock':
                    return verb.v_unlock.check(doc)
                elif str(token.lemma_).lower() == 'wait':
                    return verb.v_wait.check(doc)
            elif str(token.dep_) == 'NOUN':
                if str(token.lemma_).lower() == 'bug':
                    return noun.n_bug.check(doc)
                elif str(token.lemma_).lower() == 'deadlock':
                    return noun.n_deadlock.check(doc)
                elif str(token.lemma_).lower() == 'lock':
                    return noun.n_lock.check(doc)
                elif str(token.lemma_).lower() == 'problem':
                    return noun.n_problem.check(doc)
