from __future__ import print_function
import os.path
import json


__all__ = ['ROOT', 'contexts_filename', 'get_contexts', 'get_agreement']


ROOT = os.path.abspath(os.path.dirname(__file__))


def contexts_filename(pos, corpus, word):
    ''' Return absolute path to file with contexts for given part of speech
    (pos), corpuss and word.
    Current valid pos values are "nouns" and "verbs", and valid corpus values
    are "RuTenTen" and "RNC".
    '''
    return os.path.join(ROOT, pos, corpus, '{}.txt'.format(word))


def get_contexts(filename, with_skipped=False):
    ''' Read results from file with labeled data.
    Skip undefined or "other" senses.
    If there are two annotators, return only contexts
    where both annotators agree on the meaning and it is defined.
    Returns senses, a dictionary of {sense_id: sense definition},
    and a list of contests, each context as ((left, word, right), sense_id).
    '''
    if filename.endswith('.json'):
        assert not with_skipped
        with open(filename, 'rt') as f:
            senses, w_d = json.load(f)
            other = max(senses, key=int)
            w_d = [(ctx, s) for ctx, s in w_d if s not in {'0', other}]
            return senses, w_d
    w_d = []
    with open(filename, 'r') as f:
        senses = {}
        other = None
        skipped = []
        for i, line in enumerate(f, 1):
            row = list(filter(None, line.strip().split('\t')))
            try:
                if line.startswith('\t'):
                    if len(row) == 3:
                        meaning, ans, ans2 = row
                        assert ans == ans2
                    else:
                        meaning, ans = row
                    if ans != '0':
                        senses[ans] = meaning
                else:
                    if other is None:
                        other = str(len(senses))
                        del senses[other]
                    if len(row) == 5:
                        before, word, after, ans1, ans2 = row
                        if ans1 == ans2:
                            ans = ans1
                        else:
                            skipped.append(
                                ((before, word, after), (ans1, ans2)))
                            continue
                    else:
                        before, word, after, ans = row
                    if ans != '0' and ans != other:
                        w_d.append(((before, word, after), ans))
                    else:
                        skipped.append(((before, word, after), ans))
            except ValueError:
                print('error on line', i, file=sys.stderr)
                raise
    return (senses, w_d, skipped) if with_skipped else (senses, w_d)


def get_agreement(filename):
    ''' Return ratio of senses where both annotators gave either the
    same concrete sense, or both skipped the senses.
    ("do not understand (0)" and "other" are considered equal).
    '''
    senses, w_d, skipped = get_contexts(filename, with_skipped=True)
    other = str(len(senses) + 1)
    n_agree = len(w_d)
    n_disagree = 0
    for _, ans in skipped:
        if isinstance(ans, tuple):
            ans1, ans2 = ans
            if ans1 == ans2 or all(a in ['0', other] for a in [ans1, ans2]):
                n_agree += 1
            else:
                n_disagree += 1
    return n_agree / (n_agree + n_disagree)
