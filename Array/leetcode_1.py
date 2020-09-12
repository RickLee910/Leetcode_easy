class Solution:
    def twoSum(self, nums, target):
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i,j]

a=[3,2,4]
s = Solution()
print(s.twoSum(a, 6))