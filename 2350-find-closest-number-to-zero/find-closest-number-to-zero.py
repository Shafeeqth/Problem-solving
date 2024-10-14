class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        max_val = float('inf')
        val = float('-inf')
        for x in nums:
            absolute = abs(x) 
            if absolute == max_val and val < x:
                val = x
            elif absolute < max_val:
                max_val = absolute
                val = x
        return val

        