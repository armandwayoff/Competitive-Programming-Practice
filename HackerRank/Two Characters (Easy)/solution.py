def alternate(s):
    letters = list(dict.fromkeys(s))

    lengths = []
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            newS = ''.join([x for x in s if x == letters[i] or x == letters[j]])
            if test(newS):
                lengths.append(len(newS))
    if len(lengths) == 0:
        return 0
    else:
        return max(lengths)

def test(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True
