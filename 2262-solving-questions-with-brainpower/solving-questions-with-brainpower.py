class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def solve(index):
            if index >= n:
                return 0

            skip = solve(index + 1)
            take = questions[index][0] + solve(index + questions[index][1] + 1)
            return max(skip, take)
        
        return solve(0)