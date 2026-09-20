class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        head = 0
        p = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                p = max(p, (prices[j] - prices[i]))
        return p 
        