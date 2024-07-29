class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = 0, len(costs) - 1
        heap = []
        
        for _ in range(candidates):
            heapq.heappush(heap, (costs[i], i))
            if i == j:
                i += 1
                break
            heapq.heappush(heap, (costs[j], j))
            j -= 1
            i += 1
            if i > j:
                break
        
        total_cost = 0
        for _ in range(k):
            cost, index = heapq.heappop(heap)
            total_cost += cost
            if index > j and j >= i:
                heapq.heappush(heap, (costs[j], j))
                j -= 1
            if index < i and i <= j:
                heapq.heappush(heap, (costs[i], i))
                i += 1
        
        return total_cost
