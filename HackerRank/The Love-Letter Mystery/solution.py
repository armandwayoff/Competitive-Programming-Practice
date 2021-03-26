def theLoveLetterMystery(s):
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2 + 1:][::-1] if len(s) % 2 == 1 else s[len(s) // 2:][::-1]
    if s1 == s2:
        return 0
    else:
        alpha = list(' abcdefghijklmnopqrstuvwxyz')
        count = 0
        for i in range(len(s1)):
            sym = s2[i]
            if s1[i] != sym:
                count += abs(alpha.index(s1[i]) - alpha.index(sym))
        return count
   
