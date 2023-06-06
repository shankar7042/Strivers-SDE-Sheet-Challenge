def maxSubarraySum(arr, n):
    max_so_far = 0
    curr_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum < 0:
            curr_sum = 0
        max_so_far = max(max_so_far, curr_sum)
    return max_so_far


arr = [1, 2, 7, -4, 3, 2, -10, 9, 1]
print(maxSubarraySum(arr, len(arr)))
