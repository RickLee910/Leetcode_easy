import collections

class Solution:
    def containsDuplicate1(self, nums):
        size = len(nums)
        temp = set(nums)
        if size == len(temp):
            return False
        else:
            return True
    #hash
    def containsDuplicate(self, nums):
        temp = collections.Counter(nums)
        for i in list(temp.values()):
            if i > 1:
                return True
        return False


s = Solution()
a = [1,2,3]
print(s.containsDuplicate1(a))