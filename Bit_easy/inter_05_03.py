class Solution:
    def reverseBits(self, num: int) -> int:
        pre, cur =0, 0
        res = 1
        for i in range(32):
            if num & (1<<i):
                cur+=1
            else:
                res=max(res, pre+cur)
                pre = cur +1
                cur = 0
        res=max(res, pre+cur)
        return res

s = Solution()
a = 2147482622
print(s.reverseBits(a))