class Solution:
    def prefixesDivBy5(self, A):
        temp = []
        flag = 0
        for i in range(len(A)):
            flag = (flag << 1) + A[i]
            if flag % 5 == 0:
                temp.append(True)
            else:
                temp.append(False)
        return temp

s =Solution()
a = [0,1,1,1,1,1]
print(s.prefixesDivBy5(a))