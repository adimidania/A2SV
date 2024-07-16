class Solution(object):
    def isTriangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def largestPerimeter(self, nums):
        nums.sort()
        largest_p = 0

        for i in range(len(nums)-2):
            if self.isTriangle(nums[i], nums[i+1], nums[i+2]):
                largest_p = max(largest_p, sum(nums[i:i+3]))

        return largest_p