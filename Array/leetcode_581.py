class Solution:
    def findUnsortedSubarray(self, nums):
        size = len(nums)
        left,right = 0,-1
        max_num = nums[0]
        min_num = nums[-1]
        for i in range(size):
            if nums[i] < max_num:
                right = i
            else:
                max_num = nums[i]
            if nums[size - i - 1] > min_num:
                left = size - i - 1
            else:
                min_num = nums[size - i - 1]
        return right - left + 1
s = Solution()
a = [1,2,3,4]
print(s.findUnsortedSubarray(a))
