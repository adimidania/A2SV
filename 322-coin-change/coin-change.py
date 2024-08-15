class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(target, index):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if index >= len(coins):
                return float('inf')
            if (target, index) in memo:
                return memo[(target, index)]
            
            take = dp(target - coins[index], index)
            skip = dp(target, index + 1)

            memo[(target, index)] = min(take + 1, skip)
            return memo[(target, index)]

        answer = dp(amount, 0)
        return -1 if answer == float('inf') else answer
