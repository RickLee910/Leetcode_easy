class Solution:
    def plusOne(self, digits):
        l = len(digits)
        num= 0
        for i in range(l):
            num += digits[i] * (10 ** (l - 1 - i))
        num += 1
        ans = [int(x) for x in str(num)]
        return ans

s =Solution()
a = [0]
print(s.plusOne(a))