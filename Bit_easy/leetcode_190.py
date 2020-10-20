class Solution:
    def reverseBits(self, n: int) -> int:
        temp = list(bin(n))[2:]
        temp = ['0'] * (32 - len(temp)) + temp
        return int(''.join(temp[::-1]),2)
