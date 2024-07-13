class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        min_heap = [-pile for pile in piles]
        heapq.heapify(min_heap)
        
        for _ in range(k):
            n = -heapq.heappop(min_heap)
            h = n - n // 2
            heapq.heappush(min_heap, -h)

        return -sum(min_heap)