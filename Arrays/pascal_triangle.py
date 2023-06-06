def printPascal(n: int):
    ans = [[1]]

    for i in range(1, n):
        curr = [1]
        for j in range(1, i):
            curr.append(ans[i-1][j] + ans[i-1][j-1])
        curr.append(1)
        ans.append(curr)
    return ans


def printPascalTriangle(pascalMatrix: list[int]):
    for i in range(len(pascalMatrix)):
        print(pascalMatrix[i])


printPascalTriangle(printPascal(10))
