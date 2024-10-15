class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = defaultdict(int)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        self.mergesort(indexed_nums)
        result = [self.count[key] for key in indexed_nums]
        return result

    def merge(self, left: List[tuple], right: List[tuple]) -> List[tuple]:
        i, j = 0, 0
        m, n = len(left), len(right)

        while i < m:
            while j < n and left[i][0] > right[j][0]:
                j += 1
            self.count[left[i]] += j
            i += 1

        i, j = 0, 0
        merged = []

        while i < m and j < n:
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                i += 1
            elif left[i][0] == right[j][0]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(right[j])
                j += 1

        while i < m:
            merged.append(left[i])
            i += 1
            
        while j < n:
            merged.append(right[j])
            j += 1

        return merged

    def mergesort(self, nums: List[tuple]) -> List[tuple]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merge(left, right)
