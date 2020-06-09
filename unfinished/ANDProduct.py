# 50% (Your code did not execute within the time limits)

def andProduct(a, b):
    ans = a
    for i in range(a + 1, b + 1):
        ans &= i
    return ans
