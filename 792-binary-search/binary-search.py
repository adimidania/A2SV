class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1  
            else:
                start = middle + 1  
        return -1


        
        