class Solution:
    def CheckPermutation(self, s1, s2):
        temp1, temp2 = {}, {}
        if len(s1) != len(s2):
            return False
        for i, x in enumerate(s1):
            temp1[x] = temp1.get(x, 0) + 1
        for j,y in enumerate(s2):
            temp2[y] = temp2.get(y,0) + 1
        if temp1 == temp2:
            return True
        else:
            return False

a= ''
b=''
sol = Solution()
print(sol.CheckPermutation(a,b))