def perm1(arr: list[int]):
    ans = []
    curr = []
    map = [False] * (len(arr))

    def h(curr: list[int], map: list[bool]):
        if len(curr) == len(arr):
            ans.append(curr.copy())
            return

        for i in range(len(arr)):
            if not map[i]:
                curr.append(arr[i])
                map[i] = True
                h(curr, map)
                curr.pop()
                map[i] = False
    h(curr, map)
    return ans


def perm2(arr: list[int]) -> list[list[int]]:
    ans: list[list[int]] = []

    def helper(ind: int = 0):
        if ind == len(arr):
            ans.append(arr.copy())
            return
        for i in range(ind, len(arr)):
            arr[i], arr[ind] = arr[ind], arr[i]
            helper(ind+1)
            arr[i], arr[ind] = arr[ind], arr[i]

    helper()
    return ans


def next_permutation(arr: list[int]):
    n = len(arr)
    i = n-2
    while i > -1 and arr[i] >= arr[i+1]:
        i -= 1

    j = n-1
    while i > -1 and arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    reverse(arr, i+1, n-1)
    return arr


def reverse(arr, low, high):
    while low <= high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


arr = [4, 3, 2, 1]
print(next_permutation(arr))
