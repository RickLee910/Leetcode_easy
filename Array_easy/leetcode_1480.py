class Solution:
    def runningSum(self, nums):
        temp = []
        for i in range(len(nums)):
            temp.append(sum(nums[0:i + 1]))
        return temp
