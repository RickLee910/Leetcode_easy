class Solution:
    def binaryGap(self, n: int) -> int:
        temp = list(bin(n))[2:]
        l = []
        i = 0
        while i < len(temp):
            if temp[i] == '1':
                l.append(i)
            i += 1
        if len(l) == 1:
            return 0
        maxl = 0
        for i in range(len(l) - 1):
            maxl = max(l[i + 1]-l[i],maxl)
        return maxl