def superDigit(n, k):
    m = k * count(n)
    return count(m)


def count(n):
    if len(str(n)) > 1:
        somme = sum([int(i) for i in list(str(n))])
        return count(somme)
    else:
        return n
