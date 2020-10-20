import collections
class Solution:
    def isUnique(self, astr: str) -> bool:
        temp = collections.Counter(astr)
        for i in list(temp.values()):
            if i > 1:
                return False
        return True
s = Solution()
a = 'ltcode'
print(s.isUnique(a))