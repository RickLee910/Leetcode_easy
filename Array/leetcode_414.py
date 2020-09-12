class Solution:
    def thirdMax(self, nums) -> int:

        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return max(nums)
        return nums[-3]
s = Solution()
a = [1,1,2]
print(s.thirdMax(a))