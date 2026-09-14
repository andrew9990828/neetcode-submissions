class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0

        for i, p in enumerate(prices):
            if p < prices[l]:
                l = i
            
            if p > prices[l]:
                best = max(best, p - prices[l])
        
        return best
            