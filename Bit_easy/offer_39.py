import collections
class Solution:
    def majorityElement(self, nums) -> int:
        temp = collections.Counter(nums)
        for i in list(temp.keys()):
            if temp[i] > len(nums) // 2:
                return i
s = Solution()
a = [8,8,7,7,7]
print(s.majorityElement(a))