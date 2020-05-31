def flippingMatrix(matrix):
    somme = 0
    for i in range(n):
        for j in range(n):
            somme += max(matrix[i][j], matrix[2 * n - 1 - i][j], matrix[2 * n - 1 - i][2 * n - 1 - j], matrix[i][2 * n - 1 - j])
    return somme
