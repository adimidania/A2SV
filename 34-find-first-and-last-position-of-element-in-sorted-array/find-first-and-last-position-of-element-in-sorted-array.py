class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstIndex(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        end = mid - 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        def findLastIndex(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        return [findFirstIndex(nums, target), findLastIndex(nums, target)]