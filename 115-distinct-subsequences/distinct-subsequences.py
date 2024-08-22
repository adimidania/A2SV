class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def countDistinct(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(t):
                return 1 
            if i == len(s):
                return 0 

            if s[i] == t[j]:
                memo[(i, j)] = countDistinct(i + 1, j + 1) + countDistinct(i + 1, j)
            else:
                memo[(i, j)] = countDistinct(i + 1, j)
            
            return memo[(i, j)]

        return countDistinct(0, 0)


