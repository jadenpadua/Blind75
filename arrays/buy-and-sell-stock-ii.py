class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if prices is None or len(prices) == 0:
            return 0
        
        minPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit
