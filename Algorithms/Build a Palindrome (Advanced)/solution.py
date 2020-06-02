def buildPalindrome(a, b):
    global extremite_a, extremite_b
    list_a, list_b = list(a), list(b)

    count = 0
    for i in range(len(list_a)):
        if list_a[i] not in list_b:
            count += 1
    if count == len(list_a):
        return -1

    sorted_list_a, sorted_list_b = list_a.copy(), list_b.copy()
    sorted_list_a.sort()
    sorted_list_b.sort()
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if sorted_list_a[i] == sorted_list_b[j]:
                extremite_a = list_a.index(sorted_list_a[i])
                extremite_b = list_b.index(sorted_list_b[j])
                break
        else:
            continue
        break

    sub_a = list_a[extremite_a]
    sub_b = list_b[extremite_b]
    index = 1
    while extremite_a + index < len(list_a) and extremite_b - index >= 0:
        if list_a[extremite_a + index] == list_b[extremite_b - index]:
            sub_a += list_a[extremite_a + index]
            sub_b = list_b[extremite_b - index] + sub_b
            index += 1
        else:
            break
    index -= 1

    print(sub_a, sub_b)

    if extremite_a + index == len(list_a) - 1 and extremite_b - index == 0:
        return sub_a + sub_b
    if extremite_a + index < len(list_a) - 1 and extremite_b - index == 0:
        return sub_a + list_a[extremite_a + index + 1] + sub_b
    if extremite_a + index == len(list_a) - 1 and extremite_b - index > 0:
        return sub_a + list_b[extremite_b - index - 1] + sub_b
    if extremite_a + index < len(list_a) - 1 and extremite_b - index > 0:
        new_extrem = [list_a[extremite_a + index + 1], list_b[extremite_b - index - 1]]
        new_extrem.sort()
        return sub_a + new_extrem[0] + sub_b
