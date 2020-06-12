def maxMin(k, arr):
    comb = combinations(arr, k)
    minmax = []
    for i in list(comb):
        minmax.append(max(i) - min(i))
    return min(minmax)
