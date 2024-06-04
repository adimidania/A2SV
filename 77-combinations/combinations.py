class Solution:
    def combine(self, n, k):
        combinations = []
        combination = []
        def backtrack(start):
            if len(combination) == k:
                combinations.append(list(combination))
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1)
                combination.pop()

        backtrack(1)
        return combinations
        