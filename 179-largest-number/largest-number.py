class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return (y + x > x + y) - (y + x < x + y)
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        
        return '0' if nums[0] == '0' else ''.join(nums)