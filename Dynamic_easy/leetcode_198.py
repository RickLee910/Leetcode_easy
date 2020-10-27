class Solution:
    def rob(self, nums) -> int:
        temp = [0,0]
        for i in range(len(nums)):
            temp.append(max(temp[-1], temp[-2] + nums[i]))
        return max(temp)
s = Solution()
a = [2,1,4,5,3,1,1,3]
print(s.rob(a))