class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        SUM = 0
        for i in range(0,len(nums), 2):
            SUM += nums[i]
        return SUM
s = Solution()
a = [1,4,4,4,3,2,4,1]
print(s.arrayPairSum(a))
