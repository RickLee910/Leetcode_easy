class Solution:
    def arrayRankTransform(self, arr):
        temp = arr.copy()
        temp = list(set(temp))
        temp.sort()
        temp1 ={}
        for i,x in enumerate(temp):
            temp1[x] = i + 1

        return [temp1[i] for i in arr]

s = Solution()
a = [37,12,28,9,100,56,80,5,12]
print(s.arrayRankTransform(a))