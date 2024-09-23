class Solution:
    def maxDepth(self, s: str) -> int:
        max_nest = 0
        nest = 0
        for x in s:
            if x == '(':
                nest += 1
            elif x == ')':
                nest -= 1
            max_nest = max(nest, max_nest)
        return max_nest


        