import os.path


__all__ = ['ROOT', 'contexts_filename', 'get_labeled_contexts']


ROOT = os.path.abspath(os.path.dirname(__file__))


def contexts_filename(pos, corpus, word):
    ''' Return absolute path to file with contexts for given part of speech
    (pos), corpuss and word.
    Current valid pos values are "nouns" and "verbs", and valid corpus values
    are "RuTenTen" and "RNC".
    '''
    return os.path.join(ROOT, pos, corpus, '{}.txt'.format(word))


def get_labeled_contexts(filename):
    ''' Read results from file with labeled data.
    Skip undefined or "other" senses.
    If there are two annotators, return only contexts
    where both annotators agree on the meaning and it is defined.
    Returns senses, a dictionary of {sense_id: sense definition},
    and a list of contests, each context as ((left, word, right), sense_id).
    '''
    w_d = []
    with open(filename, 'r') as f:
        senses = {}
        other = None
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
                            continue
                    else:
                        before, word, after, ans = row
                    if ans != '0' and ans != other:
                        w_d.append(((before, word, after), ans))
            except ValueError:
                print('error on line', i, file=sys.stderr)
                raise
    return senses, w_d
