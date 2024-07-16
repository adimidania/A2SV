class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k  
        
        k -= numOnes
        output = numOnes
        
        if k <= numZeros:
            return output 
        
        k -= numZeros
        output -= k  
        
        return output