class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1

        for num, i in count.items():
            if i == 1:
                return num
        