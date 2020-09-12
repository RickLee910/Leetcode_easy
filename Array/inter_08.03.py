import bisect
class Solution:
    def findMagicIndex(self, nums) -> int:
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1

s = Solution()
a = [1,1 ,3, 3, 4, 5]
print(s.findMagicIndex(a))