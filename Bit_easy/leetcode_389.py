import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp1 = collections.Counter(list(s))
        temp2 = collections.Counter(list(t))
        for i in list(temp2.keys()):
            if i not in list(temp1.keys()) or temp1[i] != temp2[i]:
                return i

s = Solution()
a = "abcd"
b ="abcde"
print(s.findTheDifference(a,b))