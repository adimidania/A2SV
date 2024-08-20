class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robbing(start, end):
            memo = [None] * n
            def dp(index):
                if index >= end:
                    return 0
                if memo[index] is None:
                    memo[index] = max(dp(index + 1), dp(index + 2) + nums[index])
                return memo[index]
            return dp(start)
        
        # Case 1: Rob from the first house to the second-to-last house
        case1 = robbing(0, n-1)
        # Case 2: Rob from the second house to the last house
        case2 = robbing(1, n)
        
        # Return the maximum of the two cases
        return max(case1, case2)
