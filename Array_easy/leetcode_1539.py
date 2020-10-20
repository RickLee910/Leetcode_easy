class Solution:
    def findKthPositive(self, arr, k):
        temp = []
        num = 1
        for i in range(len(arr)):
            while arr[i] != num:
                temp.append(num)
                num+= 1
                if len(temp) == k:
                    return temp[-1]
            num+= 1
        for j in range(k - len(temp)):
            temp.append(num)
            num+= 1
        return temp[-1]
s= Solution()
a = [1,2,3,4]
print(s.findKthPositive(a,16))