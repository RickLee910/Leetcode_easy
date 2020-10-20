class Solution:
    def createTargetArray(self, nums, index):
        temp = []
        for i in range(len(nums)):
            temp.insert(index[i], nums[i])
        return temp