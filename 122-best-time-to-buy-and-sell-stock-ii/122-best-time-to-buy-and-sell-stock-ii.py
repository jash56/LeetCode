class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start = prices[0]
        profit = 0
        for end in prices:            
            if end > start:
                profit += end - start
            start = end
        return profit