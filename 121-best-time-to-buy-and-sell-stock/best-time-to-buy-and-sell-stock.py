class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            min_ = prices[0]
            max_profit = 0
            for i in range(1, len(prices)):
                max_profit = max(max_profit, prices[i] - min_)
                min_ = min(prices[i], min_)
            return max_profit
            
        