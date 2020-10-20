class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1 = len(num1)
        s2 = len(num2)
        n1, n2 = 0, 0
        j = 1
        for i in num1:
            n1 += int(i) * 10 ** (s1 - j)
            j += 1
        j = 1
        for i in num2:
            n2 += int(i) * 10 ** (s2 - j)
            j += 1
        return str(n1 + n2)
s = Solution()
a = '9'
b = '99'
print(s.addStrings(a,b))