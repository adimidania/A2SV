class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        
        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:  
                heappop(heap)

        return [num for freq, num in heap]