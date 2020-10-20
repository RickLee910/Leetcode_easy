class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = bin(N)[2:]
        b_new = ''
        for i in b:
            if i == '0':
                b_new += '1'
            else:
                b_new += '0'
        return int(b_new,2)
s = Solution()
a = 10
print(s.bitwiseComplement(a))
