class Solution:
    def minLength(self, s: str) -> int:
        while True:
            n = len(s)
            s = s.replace('AB', '').replace('CD', '')
            if n == len(s):
                break
        return len(s)