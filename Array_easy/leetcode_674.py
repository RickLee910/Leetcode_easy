
class Solution:
    def findLengthOfLCIS(self, nums):
        a = 1
        MaxLen = 1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if(nums[i] > nums[i - 1]):
                a += 1
            else:
                MaxLen = max(MaxLen,a)
                a = 1
        return max(MaxLen, a)

a = [1,3,5,7]
sol = Solution()
print(sol.findLengthOfLCIS(a))
