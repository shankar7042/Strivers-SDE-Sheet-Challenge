def missingAndRepeating(arr: list[int], n: int) -> list[int, int]:
    sum1 = (n * (n+1)) // 2
    sum2 = (n * (n + 1) * (2*n + 1)) // 6
    real_sum = 0
    real_sum2 = 0
    for i in range(n):
        real_sum += arr[i]
        real_sum2 += arr[i] * arr[i]

    val1 = sum1 - real_sum
    val2 = (sum2 - real_sum2) // val1
    missing_num = (val1 + val2) // 2
    repeating_num = val2 - missing_num
    return [missing_num, repeating_num]


arr = [6, 4, 3, 5, 5, 1]
print(missingAndRepeating(arr, len(arr)))
