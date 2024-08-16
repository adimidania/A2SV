class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        for i in range(len(questions)-1, -1, -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + questions[i][1] + 1, 0),
                dp.get(i+1, 0)
            )

        return dp[0]