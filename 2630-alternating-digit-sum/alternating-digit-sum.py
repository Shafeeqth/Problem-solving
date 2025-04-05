class Solution:
    def alternateDigitSum(self, n: int) -> int:
        strN = str(n)
        return sum(-int(strN[x]) if x % 2 else int(strN[x]) for x in range(len(strN)))
        