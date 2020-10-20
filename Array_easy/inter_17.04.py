import collections
class Solution:
    def missingNumber(self, nums):
        temp = collections.Counter(nums)
        for i in range(len(nums) + 1):
            if i not in temp:
                return i
s = Solution()
a = [1,2,3,4,5]
print(s.missingNumber(a))