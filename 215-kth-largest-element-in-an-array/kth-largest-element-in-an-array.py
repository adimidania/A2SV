class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        for i in range(k):
            output = -1* heappop(max_heap)
        return output