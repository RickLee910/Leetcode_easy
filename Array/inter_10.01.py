class Solution:
    def merge(self, A, m: int, B, n: int):
        temp = A[:m]
        res = temp + B
        res.sort()
        A = res
        return A
s = Solution()
a = [1,2,3,0,0,0]
b = [2,5,6]
m = 3
n = 3
print(s.merge(a,m,b,n))
