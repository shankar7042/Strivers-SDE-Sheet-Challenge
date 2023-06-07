# n = row, m = col
def rotateMatrix(mat: list[list[int]], n: int, m: int):
    row_start, col_start, row_end, col_end = 0, 0, n-1, m-1

    while row_start < row_end and col_start < col_end:
        print(row_start, col_start, row_end, col_end)
        last_ele = mat[row_start][col_end]
        for i in range(col_end, col_start, -1):
            mat[row_start][i] = mat[row_start][i-1]

        new_last_ele = mat[row_end][col_end]
        for i in range(row_end, row_start+1, -1):
            mat[i][col_end] = mat[i-1][col_end]
        mat[row_start+1][col_end] = last_ele

        last_ele = mat[row_end][col_start]
        for i in range(col_start, col_end - 1):
            mat[row_end][i] = mat[row_end][i+1]

        mat[row_end][col_end-1] = new_last_ele

        for i in range(row_start, row_end-1):
            mat[i][col_start] = mat[i+1][col_start]
        mat[row_end-1][col_start] = last_ele

        row_start, col_start, row_end, col_end = row_start + \
            1, col_start+1, row_end-1, col_end-1


def printMatrix(matrix):
    for row in matrix:
        print(row)


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotateMatrix(arr, len(arr), len(arr[0]))
printMatrix(arr)

# the above array should rotate clock wise ans output will be like below
# arr = [
#     [5, 1, 2, 3],
#     [9, 10, 6, 4],
#     [13, 11, 7, 8],
#     [14, 15, 16, 12]
# ]
