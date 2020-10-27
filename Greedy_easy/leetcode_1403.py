class Solution:
    def minSubsequence(self, nums):

        S = sum(nums)
        nums.sort()
        temp = 0
        for i in range(len(nums)):
            temp += nums[len(nums) - i - 1]
            if temp >S - temp:
                if temp == S:
                    return nums
                return nums[:len(nums) - i - 2:-1]
s = Solution()
a =[8,8]
print(s.minSubsequence(a))
