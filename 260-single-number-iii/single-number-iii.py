class Solution:
    def singleNumber(self, arr: List[int]) -> List[int]:
        combined_xor = 0
        for value in arr:
            combined_xor ^= value
        
        diff_bit = combined_xor & -combined_xor
        
        first_unique = 0
        second_unique = 0
        for value in arr:
            if value & diff_bit:
                first_unique ^= value
            else:
                second_unique ^= value
        
        return [first_unique, second_unique]
