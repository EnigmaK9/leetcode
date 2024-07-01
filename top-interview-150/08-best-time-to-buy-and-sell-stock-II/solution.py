class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        total_profit = 0

        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                total_profit += prices[index] - prices[index - 1]

        return total_profit

# Casos de prueba
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

sol = Solution()
print(sol.maxProfit(prices1))  # Output: 7
print(sol.maxProfit(prices2))  # Output: 4
print(sol.maxProfit(prices3))  # Output: 0

