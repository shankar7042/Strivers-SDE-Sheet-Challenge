def binarySearch(arr: list[int], target: int):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1


def searchMatrix(mat: list[list[int]], target: int) -> bool:
    for row in mat:
        if binarySearch(row, target) != -1:
            return True
    return False


def searchMatrixEfficient(mat: list[list[int]], target: int) -> bool:
    low = 0
    n = len(mat)
    m = len(mat[0])
    high = (n * m) - 1
    print(n, m)
    while low <= high:
        mid = low + ((high-low)//2)
        if mat[mid // m][mid % m] == target:
            return True
        elif mat[mid // m][mid % m] > target:
            high = mid-1
        else:
            low = mid + 1
    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(searchMatrixEfficient(matrix, 8))
