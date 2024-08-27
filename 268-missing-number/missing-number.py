class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(1, n + 1):
            answer ^= i
        for num in nums:
            answer ^= num
        return answer