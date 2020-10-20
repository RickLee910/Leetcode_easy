class Solution:
    def moveZeroes1(self, nums):
        size = len(nums)
        for i in range(size):
            if nums[i] == 0:
                nums.append(0)
        count = 0
        while len(nums) != size:
            if nums[count] == 0:
                nums.pop(count)
            else:
                count+= 1
        return nums

    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
s = Solution()
a = [0,0,1]
print(s.moveZeroes(a))