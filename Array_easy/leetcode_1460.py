import collections
class Solution:
    def canBeEqual(self, target, arr):
        temp_t = collections.Counter(target)
        temp_a = collections.Counter(arr)
        for i in list(temp_t.keys()):
            if temp_t[i] != temp_a[i]:
                return False
        return True
