class Solution(object):
    def maxProfit(self, p):
        if not p:
            return 0
        t = 0
        for i in range(1, len(p)):
            if p[i] > p[i - 1]:
                t += p[i] - p[i - 1]
        return t


