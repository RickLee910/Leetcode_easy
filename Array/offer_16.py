class Solution:

    #动态规划
    def maxSubArray1(self, nums):
        if nums == []:
            return 0
        else:
            for i in range(1, len(nums)):
                nums[i] = max(nums[i] + nums[i - 1], nums[i])
            return max(nums)


sol = Solution()
a = [1,-1,-2,3]
print(sol.maxSubArray(a))

