# hash method
def findDuplicate(arr: list, n: int):
    hash_list = [False] * (n)
    for i in range(n):
        if hash_list[int(arr[i])]:
            return int(arr[i])
        else:
            hash_list[int(arr[i])] = True
    return 0

# slow and fast pointer method


def findDuplicate2(arr: list[int], n: int):
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


arr = [5, 4, 2, 4, 1]
print(findDuplicate2(arr, len(arr)))
