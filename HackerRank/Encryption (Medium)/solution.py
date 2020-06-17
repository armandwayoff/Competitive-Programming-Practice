def encryption(s):
    columns = math.ceil(math.sqrt(len(s)))
    rows = math.ceil(len(s) / columns)

    matrix = []
    for i in range(rows):
        matrix.append([])

    index = 0
    for i in range(len(s)):
        if i % columns == 0:
            sub = s[i:i + columns]
            for j in sub:
                matrix[index].append(j)
            index += 1
    for i in range((rows * columns - len(s))):
        matrix[-1].append('X')

    words = []
    trans = map(list, zip(*matrix))
    for r in trans:
        words.append(''.join(r).replace('X', ''))
    return ' '.join(words)
