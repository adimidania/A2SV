class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        if n == 0 or n == 1:
            return n
        else:
            if n not in memo:
                memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
        