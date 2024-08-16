class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n-1 and j == m-1 and obstacleGrid[i][j] == 0:
                return 1
            
            if obstacleGrid[i][j] == 1:
                return 0

            memo[(i, j)] = (solve(i+1, j) if i < n - 1 else 0) + (solve(i, j+1) if j < m - 1 else 0)

            return memo[(i, j)]
        
        return solve(0, 0)
        