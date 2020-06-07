def connectedCell(matrix):
    region = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                region.append([i, j])

    starting_cell = region[0]
    count = 1
    for i in range(1, len(region)):
        if abs(starting_cell[0] - region[i][0]) <= 1 and abs(starting_cell[1] - region[i][1]) <= 1:
            starting_cell = region[i]
            count += 1
    return count
