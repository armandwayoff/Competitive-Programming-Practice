def palindromeIndex(s):
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2 + 1:][::-1] if len(s) % 2 == 1 else s[len(s) // 2:][::-1]
    if s1 == s2:
        return -1
    else:
        for i in range(len(s1)):
            sym = s2[i]
            if s1[i] != sym:
                S = s1[:i] + s1[i + 1:]
                s3 = s[:len(S) // 2]
                s4 = s[len(S) // 2 + 1:][::-1] if len(S) % 2 == 1 else S[len(S) // 2:][::-1]
                if s3 == s4:
                    return i
                else:
                    return len(s1) + 1 - i
                    
