def surfaceArea(A):
    surface = H * W * 2

    left_side, right_side = A[0], A[-1]
    front_side = []
    for i in range(len(A)):
        front_side.append(A[i][0])
    back_side = []
    for i in range(len(A)):
        back_side.append(A[i][-1])
    s1, s2 = [], []
    s1.extend([left_side, right_side])
    s2.extend([front_side, back_side])

    for i in range(2):
        for j in range(W):
            surface += s1[i][j]

    for i in range(2):
        for j in range(H):
            surface += s2[i][j]

    for i in range(H):
        for j in range(W - 1):
            surface += abs(A[i][j + 1] - A[i][j])
    for i in range(W):
        for j in range(H - 1):
            surface += abs(A[j + 1][i] - A[j][i])
            
    return surface
