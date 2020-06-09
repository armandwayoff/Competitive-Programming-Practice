def biggerIsGreater(w):
    p = itertools.permutations(w)
    l = []
    for i in p:
        if ''.join(i) > w:
            l.append(''.join(i))
    l.sort()
    if len(l) > 0:
        return l[0]
    else:
        return 'no answer'
