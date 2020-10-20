class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        S_pra = sum(nums)
        S_org = (len(nums) * (1 + len(nums)))// 2
        dif = S_org - S_pra
        for i in range(len(nums)- 1):
            if nums[i] == nums[i+1]:

                return [nums[i],nums[i] + dif]
s = Solution()
a = [2,2]
print(s.findErrorNums(a))

