
def rowZero(matrix: list[list[int]], row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def colZero(matrix: list[list[int]], col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def setZeros(matrix: list[list[int]]) -> None:
    rowSet = set()
    colSet = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rowSet.add(i)
                colSet.add(j)

    for row in rowSet:
        rowZero(matrix, row)

    for col in colSet:
        colZero(matrix, col)


matrix = [[7, 19, 3], [4, 21, 0]]
print(matrix)
setZeros(matrix)
print(matrix)
