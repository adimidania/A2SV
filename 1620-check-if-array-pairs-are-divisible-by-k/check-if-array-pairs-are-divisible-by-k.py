class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k

        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

        for r in range(1, k):
            if remainder_count[r] != remainder_count[k - r]:
                return False

        if remainder_count[0] % 2 != 0:
            return False
        
        return True