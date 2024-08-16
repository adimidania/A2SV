class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1)-1, len(text2)-1
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > n1 or j > n2:
                return 0
            if text1[i] == text2[j]:
                return 1 + solve(i+1, j+1)
            else:
                memo[(i, j)] = max(solve(i, j+1), solve(i+1, j))  
                return memo[(i, j)]

        return solve(0, 0)      