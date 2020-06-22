def matrixRotation(matrix, r):
    cycles = []
    for i in range(math.floor(len(matrix) / 2)):
        newCycle = []
        for p in range(i, len(matrix[0]) - i):
            newCycle.append(matrix[i][p])
        for p in range(i + 1, len(matrix) - 1 - i):
            newCycle.append(matrix[p][len(matrix[0]) - 1 - i])
        for p in range(len(matrix[0]) - i - 1, i - 1, -1):
            newCycle.append(matrix[len(matrix) - 1 - i][p])
        for p in range(len(matrix) - 2 - i, i, -1):
            newCycle.append(matrix[p][i])
        cycles.append(newCycle)
    
    for i in range(len(cycles)):
        rot = r % len(cycles[i])
        cycles[i] = cycles[i][rot:] + cycles[i][:rot]
    
    newMatrix = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(cycles)):
        indice = 0
        for p in range(i, len(matrix[0]) - i):
            newMatrix[i][p] = cycles[i][indice]
            indice += 1
        for p in range(i + 1, len(matrix) - 1 - i):
            newMatrix[p][len(matrix[0]) - 1 - i] = cycles[i][indice]
            indice += 1
        for p in range(len(matrix[0]) - i - 1, i - 1, -1):
            newMatrix[len(matrix) - 1 - i][p] = cycles[i][indice]
            indice += 1
        for p in range(len(matrix) - 2 - i, i, -1):
            newMatrix[p][i] = cycles[i][indice]
            indice += 1
    
    for i in range(len(newMatrix)):
        print(*newMatrix[i])
