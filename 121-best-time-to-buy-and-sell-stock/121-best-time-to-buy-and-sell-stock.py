class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)): 
            if min_price > prices[i]:
                min_price = prices[i]
            elif max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit