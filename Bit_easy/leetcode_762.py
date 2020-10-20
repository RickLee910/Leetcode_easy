class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        temp = [2,3,5,7,11,13,17,19]
        count = 0
        for i in range(L,R+1):
            if bin(i).count('1') in temp:
                count += 1
        return count