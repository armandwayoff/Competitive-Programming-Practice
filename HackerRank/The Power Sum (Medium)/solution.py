# Solution from https://nerdprogrammer.com/hackerrank-the-power-sum-solution/

def powerSum(X, N, current=1):
    pw = pow(current, N)
    if pw > X:
        return 0
    elif pw == X:
        return 1
    else:
        return powerSum(X, N, current + 1) + powerSum(X - pw, N, current + 1)
