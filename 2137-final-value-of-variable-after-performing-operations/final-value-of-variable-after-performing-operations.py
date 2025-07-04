class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([ 1 if "++" in val else -1 for val in operations ])
        