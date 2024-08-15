class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                dp[i][j] = matrix[i][j]
                up = dp[i+1][j]
                left = dp[i+1][j-1] if j > 0 else float('inf')
                right = dp[i+1][j+1] if j < n - 1 else float('inf')
                dp[i][j] += min(up, left, right)

        return min(dp[0])
