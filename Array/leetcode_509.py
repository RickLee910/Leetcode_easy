class Solution:
    def fib(self, N):
        if N == 0 or N == 1:
            return N
        temp = [0, 1]
        for i in range(2,N+1):
            temp.append(temp[i -1 ] + temp[i - 2])
        return temp[-1]
s = Solution()
print(s.fib(4))