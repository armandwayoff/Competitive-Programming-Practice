# 6 / 22 (Your code did not execute within the time limits)

import itertools

def anotherMinimaxProblem(a):
    ans = []
    for p in itertools.permutations(a):
        arr = []
        for i in range(len(a) - 1):
            arr.append(p[i] ^ p[i + 1])
        ans.append(max(arr))
    return min(ans)
