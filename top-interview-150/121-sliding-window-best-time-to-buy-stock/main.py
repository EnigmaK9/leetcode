i# Creation Date: 2026-05-17
# Last Modified: 2026-05-17
# Description: calculate maximum profit from buying and selling a stock using two pointers
# Author: enigmak9

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize left pointer to day 0 and right pointer to day 1
        l, r = 0, 1
        maxP = 0
        
        # iterate through the list until the right pointer reaches the end
        while r < len(prices):
            # if the price on the left day is less than the price on the right day, it is profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # if the right day has a lower price, move the left pointer to the right pointer position
                l = r
            # always move the right pointer forward by one day
            r += 1
            
        return maxP
