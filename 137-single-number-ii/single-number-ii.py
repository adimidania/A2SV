class Solution:
    def singleNumber(self, nums):
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            if freq == 1:
                return num
        
        return -1