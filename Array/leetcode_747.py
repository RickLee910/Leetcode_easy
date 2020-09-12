class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        temp = nums.copy()
        temp.sort()
        if temp[-1] >= 2 * temp[-2]:
            return nums.index(temp[-1])
        else:
            return -1
s = Solution()
a = [1]
print(s.dominantIndex(a))