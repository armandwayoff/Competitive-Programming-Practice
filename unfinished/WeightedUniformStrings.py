def weightedUniformStrings(s, queries):
    alphabet = list(' abcdefghijklmnopqrstuvwxyz')
    ans = ['No'] * len(queries)
    for i in range(len(s)):
        j = i
        while j < len(s) and s[i] == s[j]:
            j += 1
        weight = alphabet.index(s[i]) * (j - i)
        if weight in queries:
            ans[queries.index(weight)] = 'Yes'
    return ans
    
