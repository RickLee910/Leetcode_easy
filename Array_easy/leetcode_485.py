class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        l, r = 0 , 0
        l_found = False
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and not l_found:
                l = i
                l_found = True
            if nums[i] == 0 and l_found:
                r = i
                count = max(r - l, count)
                l_found = False
            if i == len(nums) - 1 and l_found:
                r = i + 1
                count = max(r - l, count)
        return count
s = Solution()
a = [1,1,0,1,1,1,1,1,0,1,1,1,1]
print(s.findMaxConsecutiveOnes(a))

