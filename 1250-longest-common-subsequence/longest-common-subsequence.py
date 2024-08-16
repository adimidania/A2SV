class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1)+1, len(text2)+1
        dp = [[0 for j in range(n2)] for i in range(n1)]
        for i in range(n1-2, -1, -1):
            for j in range(n2-2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]