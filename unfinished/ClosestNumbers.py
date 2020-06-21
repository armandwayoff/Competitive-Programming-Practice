def closestNumbers(arr):
    arr.sort()
    if arr == range(min(arr), max(arr) + 1):
        ans = []
        for i in range(len(arr) - 1):
            ans.extend((arr[i], arr[i + 1]))
        return ans
    else:
        dif = []
        for i in range(len(arr) - 1):
            dif.append(abs(arr[i] - arr[i + 1]))
        ans = []
        for i in range(len(dif)):
            if dif[i] == min(dif):
                ans.extend((arr[i], arr[i + 1]))
        return ans
