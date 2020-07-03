def cavityMap(grid):
    g = []
    for i in grid:
        g.append(list(i[0]))
    ans = g.copy()
    for i in range(1, len(g) - 1):
        for j in range(1, len(g[0]) - 1):
            if int(g[i][j]) > int(g[i - 1][j]) and int(g[i][j]) > int(g[i + 1][j]) and int(g[i][j]) > int(g[i][j - 1]) and int(g[i][j]) > int(g[i][j + 1]):
                ans[i][j] = -1
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] == -1:
                ans[i][j] = 'X'
    res = []
    for i in ans:
        res.append(''.join(i))
    return res
