class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        temp = [start]
        ans = start
        for i in range(1,n):
            temp.append(start + 2 * i)
            ans ^= temp[i]
        return ans
s = Solution()
a = 4
print(s.xorOperation(a,3))