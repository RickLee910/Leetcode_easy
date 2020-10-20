class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = bin(n)
        for i in range(len(temp) - 1):
            if temp[i] == temp[i+1]:
                return False
        return True