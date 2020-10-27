class Solution:
    def maxSubArray(self, nums) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            if dp[-1] >0:
                dp.append(dp[-1] + nums[i])
            else:
                dp.append(nums[i])
        return max(dp)
s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(a))
