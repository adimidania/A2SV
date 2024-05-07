class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [(float("-inf"),-1)]
        arr.append(float("-inf"))
        count = 0
        mod = 10**9 + 7
        for right , num in enumerate(arr):
            while stack [-1][0]> num:
                value, index = stack.pop()
                _ , left = stack[-1]
                count += value*(index - left)*(right - index)
            stack.append((num, right))
        return count % mod