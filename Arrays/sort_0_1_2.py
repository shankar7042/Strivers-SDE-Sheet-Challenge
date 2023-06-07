def sort012(arr: list[int], n: int):

    # Rules
    # 0 -> low - 1 => all contains 0 only
    # low -> mid-1 => all contains 1 only
    # high + 1 -> n-1 => all contains 2 only
    # mid -> high => unsorted arr

    #           low         mid       high
    # 0 0 0 0 0  1  1 1 1 1 .............  2 2 2 2 2 2

    low, mid, high = 0, 0, n-1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
print(arr)
sort012(arr, len(arr))
print(arr)
