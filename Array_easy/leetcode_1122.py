class Solution:
    def relativeSortArray(self, arr1, arr2):
        temp = {}
        for i,x in enumerate(arr2):
            temp[x] = 0
        for i,y in enumerate(arr1):
            temp[y] = temp.get(y, 0) + 1
        count = 0
        temp1 = []
        for i in temp:
            if i not in arr2:
                while temp[i] > 0:
                    temp1.append(i)
                    temp[i] -= 1
                    arr1.pop()
            while temp[i] > 0:
                arr1[count] =i
                count += 1
                temp[i] -= 1
        temp1.sort()
        return arr1 + temp1
s = Solution()
a1 = []
a2 = []
print(s.relativeSortArray(a1, a2))