class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    perimeter += 4 
                    if grid[i-1][j] == 1 and i > 0:
                        perimeter -= 2
                    if grid[i][j-1] and j > 0:
                        perimeter -= 2
        return perimeter
        