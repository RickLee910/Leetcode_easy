class Solution:
    def containsNearbyDuplicate(self, nums, k):
        temp = {}
        size = len(nums)
        for i,x in enumerate(nums):
            if x in temp:
                return True
            temp[x] = i
            if i + 1 > k:
                del temp[nums[i - k]]
        return False
s = Solution()
a =[1,2,3,1,2,3]
print(s.containsNearbyDuplicate(a,2))