class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_dif = abs(arr[0] - arr[1])
        temp = []
        for i in range(len(arr) - 2):
            min_dif = min(min_dif , abs(arr[i + 2] - arr[i + 1]))
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == min_dif:
                temp.append([arr[i],arr[i+1]])
        return temp

s= Solution()
a = [1,3,6,10,15]
print(s.minimumAbsDifference(a))