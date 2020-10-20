class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        res = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)
        return res

sol = Solution()
a = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(a))