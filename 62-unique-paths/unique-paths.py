class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dp(row, column):
            if (row, column) in memo:
                return memo[(row, column)]
            
            if row == m - 1 and column == n - 1:
                return 1
            
            if row + 1 < m and column + 1 < n:
                memo[(row, column)] = dp(row + 1, column) + dp(row, column + 1)
            elif row + 1 < m:  
                memo[(row, column)] = dp(row + 1, column)
            elif column + 1 < n:  
                memo[(row, column)] = dp(row, column + 1)
            
            return memo[(row, column)]
        
        return dp(0, 0)