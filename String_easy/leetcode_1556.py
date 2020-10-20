class Solution:
    def thousandSeparator(self, n: int) -> str:
        count = len(str(n)) // 3
        rem = len(str(n)) % 3
        if rem == 0:
            ans = str(n)[:3]
            for i in range(1,count):
                ans += '.' + str(n)[i * 3:(i+1) * 3]
        else:
            ans = str(n)[:rem]
            for i in range(count):
                ans += '.' + str(n)[rem + i * 3:rem + (i+1) * 3]
        return ans
s = Solution()
a = 7891231231231
print(s.thousandSeparator(a))