class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            x = c
            c = a + b + c
            a, b, c = b, x, c
        return a
        