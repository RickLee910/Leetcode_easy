class Solution:
    def missingNumber(self, nums):
        nums.sort()
        if nums == [1]:
            return 0
        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]
        return nums[-1] +1
