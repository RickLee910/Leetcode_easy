class Solution:
    def rotatedDigits(self, N: int) -> int:
        def gooddigits(n):
            must_have = '2569'
            may_have = '018'
            count = 0
            for i in str(n):
                if i in must_have:
                    count = 1
                elif i in may_have:
                    continue
                else:
                    return False
            return count == 1
        count = 0
        for i in range(1,N + 1):
            if gooddigits(i):
                count += 1
        return count
s =Solution()
a = 100
print(s.rotatedDigits(a))