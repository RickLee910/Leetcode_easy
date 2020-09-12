class Solution:
    def removeElement(self, nums, val):
        size = len(nums)
        point = 0
        for i in range(size):
            if point > len(nums):
                break
            if nums[point] == val:
                nums[-1], nums[point] = nums[point], nums[-1]
                nums.pop()
            else:
                point += 1
        return len(nums)
sol = Solution()
a = [3,2,2,3]
print(sol.removeElement(a, 2))
