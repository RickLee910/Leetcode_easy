class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = list(str(x))
        return temp == temp[::-1]