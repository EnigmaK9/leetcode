def maximumProfit(prices):
    if not prices:
        return 0

    total_profit = 0

    for index in range(1, len(prices)):
        if prices[index] > prices[index - 1]:
            total_profit += prices[index] - prices[ index - 1]

    return total_profit

