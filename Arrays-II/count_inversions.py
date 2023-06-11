def merge(arr: list[int], low: int, mid: int, high: int):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    n, m = len(left), len(right)
    i, j, k = 0, 0, low
    count = 0
    while i < n and j < m:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            count += n - i
        k += 1

    while i < n:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < m:
        arr[k] = right[j]
        j += 1
        k += 1
    return count


def mergeSort(arr: list[int], low: int, high: int):
    count = 0
    if low < high:
        mid = low + (high - low) // 2
        count += mergeSort(arr, low, mid)
        count += mergeSort(arr, mid+1, high)
        count += merge(arr, low, mid, high)
    return count


arr = [5, 4, 3, 2, 1]
print(mergeSort(arr, 0, len(arr) - 1))
print(arr)
