class Solution:
    #节省了空间，利用list.extend的巧妙用法，将表头设为0后，每次添加±i(前面利用数的位运算进行折半)
    def sumZero(self, n):
        res = []
        a = (n >> 1) + 1
        if 1 == n % 2:
            res.append(0)
        for i in range(1, a):
            res.extend([i, -i])
        return res
    #个人
    def sumZero1(self, n):
        def sumZero(self, n):
            res = []
            a = n // 2
            if n % 2 == 1:
                for i in range(n):
                    res.append(i - a)
            else:
                for i in range(n):
                    res.append(i - a)
                res[-a] = a
            return res
sol = Solution()
print(sol.sumZero(13))