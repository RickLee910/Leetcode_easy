class Solution:
    def findComplement(self, num: int) -> int:
        temp = bin(num)[2:]

        return num ^ int(('1' * len(temp)),2)