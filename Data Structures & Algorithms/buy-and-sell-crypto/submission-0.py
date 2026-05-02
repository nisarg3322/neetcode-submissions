class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        buy = prices[0]
        sell = 0
        profits = []
        for price in prices:
            if price < buy:
                buy = price
            else:
                profit = price - buy
                profits.append(profit)
        
        return max(profits)
            
        