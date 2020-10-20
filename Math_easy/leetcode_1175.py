class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        def fac(n):
            if n == 1:
                return n
            return n * fac(n - 1)
        z = 0
        fz = 1
        for i in range(2,n + 1):
            temp = 2
            found_fz = False
            while i > temp:
                if i % temp == 0:
                    fz += 1
                    found_fz = True
                    break
                temp += 1
            if not found_fz:
                z += 1
        return fac(z) * fac(fz)
s = Solution()
a = 100
print(s.numPrimeArrangements(a))
