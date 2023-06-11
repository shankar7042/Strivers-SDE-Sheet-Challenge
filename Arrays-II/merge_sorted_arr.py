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


def swap_if_greater(arr1: list[int], arr2: list[int], ind1: int, ind2: int):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]


# gap method / shell sort method


def mergeSortedArray2(arr1: list[int], arr2: list[int], m: int, n: int):
    totalLen = m + n
    gap = (totalLen // 2) + (totalLen % 2)
    while gap > 0:
        left = 0
        right = left + gap
        while right < totalLen:
            # left -> arr1 and right -> arr2
            if left < m and right >= m:
                swap_if_greater(arr1, arr2, left, right - m)
            # left -> arr2 and right -> arr2
            elif left >= m:
                swap_if_greater(arr2, arr2, left - m, right - m)
            # left -> arr1 and right -> arr1
            elif right < m:
                swap_if_greater(arr1, arr1, left, right)
            left += 1
            right += 1

        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)


arr1 = [10, 20, 30, 40, 50]
arr2 = [5, 15, 25, 35, 45, 55, 65]
mergeSortedArray2(arr1, arr2, len(arr1), len(arr2))
print(arr1, arr2)
