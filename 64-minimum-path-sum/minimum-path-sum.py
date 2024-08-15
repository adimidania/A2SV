class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        
        def dp(row, column):
            if (row, column) in memo:
                return memo[(row, column)]
            
            if row == m - 1 and column == n - 1:
                return grid[row][column]
            
            if row + 1 < m and column + 1 < n:
                memo[(row, column)] = grid[row][column] + min(dp(row + 1, column), dp(row, column + 1))
            elif row + 1 < m:  
                memo[(row, column)] = grid[row][column] + dp(row + 1, column)
            elif column + 1 < n:  
                memo[(row, column)] = grid[row][column] + dp(row, column + 1)
            
            return memo[(row, column)]
        
        return dp(0, 0)
