class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        currentSum = 1  
        patches = 0    
        index = 0    
        while currentSum <= n:
            if index < len(nums) and nums[index] <= currentSum:
                currentSum += nums[index]  
                index += 1
            else:
                currentSum += currentSum
                patches += 1

        return patches