class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)
        count = 0
        for i in list(temp):
            if i == '1':
                count += 1
        return count