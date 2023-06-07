def maximumProfit(prices):
    ans = 0
    min_so_far = prices[0]
    n = len(prices)

    for i in range(1, n):
        min_so_far = min(min_so_far, prices[i])
        ans = max(ans, prices[i] - min_so_far)
    return ans


# prices = [1, 2, 3, 4]
# prices = [98, 101, 66, 72]
prices = [2, 2, 2, 2]
print(maximumProfit(prices))
