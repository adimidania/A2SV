class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_sum = [0] * (n+1)
        
        for j in range(n-1, -1, -1):
            prefix_sum[j] = prefix_sum[j+1] + int(s[j])
        
        max_sum = 0
        zeros = 0

        for i in range(n-1): 
            if s[i] == '0':
                zeros += 1
            current_score = zeros + prefix_sum[i+1]
            max_sum = max(max_sum, current_score)
        
        return max_sum
