class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            res = max(res, prices[i] - minPrice)
        
        return res