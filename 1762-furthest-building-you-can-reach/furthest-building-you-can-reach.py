class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []

        for i in range(len(heights) - 1):
            height_diff = heights[i + 1] - heights[i]
            if height_diff > 0:
                bricks -= height_diff
                heappush(max_heap, -height_diff)

                if bricks < 0:
                    if ladders == 0:
                        return i
                    
                    ladders -= 1
                    bricks -= heappop(max_heap)

        return len(heights) - 1