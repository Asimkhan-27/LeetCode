import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = np.array(nums)

        seen = {}
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
                
            
            seen[num] = i
        return []
            
        