class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            ones = zeros = 0
            for j in range(i):
                if s[j] == '0':
                    zeros += 1
            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1
            max_score = max(max_score, ones + zeros)
        return max_score
        