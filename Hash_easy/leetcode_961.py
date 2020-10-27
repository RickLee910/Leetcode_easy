class Solution:
    def repeatedNTimes(self, A) -> int:
        temp = {}
        for i,x in enumerate(A):
            temp[x] = temp.get(x, 0) + 1
            if temp[x]>1:
                return x