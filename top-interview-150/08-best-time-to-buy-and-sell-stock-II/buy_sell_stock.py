def maximum_profit(prices):
    if not prices:
        return 0

    total_profit = 0

    for index in range(1, len(prices)):
        if prices[index] > prices[index - 1]:
            total_profit += prices[index] - prices[ index - 1]

    return total_profit

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

print(maximum_profit(prices1))
print(maximum_profit(prices2))
print(maximum_profit(prices3))
