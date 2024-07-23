class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        output = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                output += 1
                continue
            
            if maxDoubles == 0:
                output += target - 1
                break
            else:
                output += 1
                target -= 1
        return output
        