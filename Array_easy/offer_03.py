import collections
class Solution:
    def findRepeatNumber(self, nums) -> int:
        temp = collections.Counter(nums)
        for i in list(temp.keys()):
            if temp[i] > 1:
                return i