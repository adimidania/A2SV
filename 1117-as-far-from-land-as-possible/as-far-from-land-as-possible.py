class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue =  deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    queue.append([r, c])

        answer = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while queue:
            r, c = queue.popleft()
            answer = grid[r][c]
            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if min(newr, newc) >= 0 and max(newr, newc) < n and grid[newr][newc] == 0:
                    queue.append([newr, newc])
                    grid[newr][newc] = grid[r][c] + 1
        return answer - 1 if answer > 1 else -1
        
        