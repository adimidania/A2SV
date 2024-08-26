class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        hold = float('-inf')
        sold = cooldown = 0
        
        for price in prices:
            new_sold = hold + price
            new_hold = max(hold, cooldown - price)
            cooldown = max(cooldown, sold)
            
            sold = new_sold
            hold = new_hold
        
        return max(sold, cooldown)
