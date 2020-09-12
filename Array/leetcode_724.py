class Solution:
    def pivotIndex(self, nums):
        if nums == []:
            return -1
        sumleft, sumright = 0, sum(nums) -nums[0]
        if sumleft == sumright:
            return 0
        for i in range(1,len(nums)):
            sumleft += nums[i -1]
            sumright -= nums[i]
            if sumleft == sumright:
                return i
        return -1
sol = Solution()
a = [-1,-1,-1,0,1,1]
print(sol.pivotIndex(a))