class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left, right = 0, len(S) - 1
        s = list(S)
        St = "QWERTYUIOPASDFGHJKLZXCVBNM"
        st = "qwertyuiopasdfghjklzxcvbnm"
        while left < right:
            if s[left] in St or s[left] in st:
                if s[right] in St or s[right] in st:
                    s[left], s[right] = s[right],s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(s[:])
s =Solution()
a ="Test1ng-Leet=code-Q!"
print(s.reverseOnlyLetters(a))