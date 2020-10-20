class Solution:
    def checkIfExist(self, arr) -> bool:
        temp = {}
        for i,x in enumerate(arr):
            temp[x*2] = temp.get(x*2,0) + 1
        if 0 in temp:
            if temp[0] > 1:
                return True
            else:
                del temp[0]
        for i in range(len(arr)):
            if arr[i] in temp:
                return True
        return False
s =Solution()
a =[10,2,5,3]
print(s.checkIfExist(a))