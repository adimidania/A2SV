class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def solve(currentValue):
            if currentValue == 0:
                return 0
            
            if currentValue < 0:
                return float('inf')
            
            if currentValue in memo:
                return memo[currentValue]
            
            min_coins = float('inf')
            
            for coin in coins:
                min_coins = min(min_coins, 1 + solve(currentValue - coin))
            
            memo[currentValue] = min_coins
            
            return min_coins

        result = solve(amount)
        return result if result != float('inf') else -1
