def printPascal1(n: int) -> list[list[int]]:
    ans = [[1]]

    for i in range(1, n):
        curr = [1]
        for j in range(1, i):
            curr.append(ans[i-1][j] + ans[i-1][j-1])
        curr.append(1)
        ans.append(curr)
    return ans


def generateRow(row: int) -> list[int]:
    ans = 1
    ansRow = list()
    ansRow.append(ans)

    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        ansRow.append(ans)
    return ansRow


def printPascal2(n: int) -> list[list[int]]:
    triangle = list()
    for i in range(1, n+1):
        triangle.append(generateRow(i))
    return triangle


def printPascalTriangle(pascalMatrix: list[int]):
    for i in range(len(pascalMatrix)):
        print(pascalMatrix[i])


printPascalTriangle(printPascal2(10))
# print(generateRow(10))
