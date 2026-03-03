import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            sr = []
            for j in range(i+1):
                sr.append(math.comb(i, j))
            result.append(sr)
                
                    
                    
        return result


