def mergeSortedArray(arr1: list[int], arr2: list[int], m: int, n: int):
    # k = 0
    # for i in range(m-n, m):
    #     arr1[i] = arr2[k]
    #     k += 1
    # arr1.sort()
    # return arr1
    left, right = m-1, 0
    while left >= 0 and right < n:
        if arr1[left] >= arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()


arr1 = [1, 2, 3, 0, 0]
arr2 = [4, 5]
mergeSortedArray(arr1, arr2, len(arr1), len(arr2))
print(arr1, arr2)
