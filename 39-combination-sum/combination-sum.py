class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(index, current_combination, total):
            if total == target:
                combinations.append(current_combination.copy())
                return
            if index >= len(candidates) or total > target:
                return

            current_combination.append(candidates[index])
            backtracking(index, current_combination, total + candidates[index])
            current_combination.pop()
            backtracking(index+1, current_combination, total)
        backtracking(0, [], 0)
        return combinations
        