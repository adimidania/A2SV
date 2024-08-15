class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(target, index):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if index >= len(coins):
                return 0
            if (target, index) in memo:
                return memo[(target, index)]
            
            # Calculate number of ways by taking or skipping the current coin
            take = dp(target - coins[index], index)
            skip = dp(target, index + 1)

            # Store the result in memo
            memo[(target, index)] = take + skip
            return memo[(target, index)]

        return dp(amount, 0)
