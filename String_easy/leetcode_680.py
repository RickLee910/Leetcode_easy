class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s, left, right):
            for i in range(left, right):
                if s[i] != s[right - 1]:
                    return False
                right -= 1
            return True
        for i in range(len(s)// 2):
            if s[i] == s[-i-1]:
                continue
            else:
                return palindrome(s,i+1, len(s) - i) or palindrome(s, i, len(s) - i - 1)
        return True
s = Solution()
a = "aba"
print(s.validPalindrome(a))