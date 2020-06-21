def missingNumbers(arr, brr):
    missing = []
    for a in brr:
        if a not in arr:
            missing.append(a)
            brr.remove(a)
    countA = []
    countB = []
    for i in list(dict.fromkeys(arr)):
        countA.append(arr.count(i))
        countB.append(brr.count(i))
    ans = []
    for i in range(len(countA)):
        if countA[i] != countB[i]:
            ans.append(list(dict.fromkeys(arr))[i])
    ans += missing
    return sorted(ans)
