class Solution:
    def isPalindrome(self, x: int) -> bool:
        return ''.join(list(reversed(list(str(x))))) == str(x)
        