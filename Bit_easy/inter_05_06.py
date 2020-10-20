class Solution:
    def convertInteger(self, A: int, B: int) -> int:

        return list(bin(A&0xffffffff ^ B&0xffffffff)).count('1')