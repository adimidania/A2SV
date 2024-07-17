class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, j = len(nums), 0
        
        for i in range(n):
            if i > j:
                break
            j = max(j, i + nums[i])

        return j >= n-1