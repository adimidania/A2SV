class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        largest_p = 0

        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                largest_p = max(largest_p, sum(nums[i:i+3]))

        return largest_p